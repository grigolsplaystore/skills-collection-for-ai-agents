import sys
import os
import json
import traceback

def main():
    try:
        # Read stdin
        input_data = sys.stdin.read()
        if not input_data.strip():
            print(json.dumps({}))
            return

        try:
            data = json.loads(input_data)
        except json.JSONDecodeError as e:
            sys.stderr.write(f"Error parsing stdin JSON: {e}\n")
            print(json.dumps({}))
            return

        conversation_id = data.get("conversationId")
        workspace_paths = data.get("workspacePaths", [])

        if not conversation_id or not workspace_paths:
            print(json.dumps({}))
            return

        # Check session log to ensure we only run once per session
        log_path = os.path.expanduser("~/.gemini/antigravity-cli/scratch/summarize_sessions.json")
        
        # Ensure scratch directory exists
        os.makedirs(os.path.dirname(log_path), exist_ok=True)
        
        sessions = []
        if os.path.exists(log_path):
            try:
                with open(log_path, "r", encoding="utf-8") as f:
                    sessions = json.load(f)
                    if not isinstance(sessions, list):
                        sessions = []
            except Exception as e:
                sys.stderr.write(f"Error reading sessions log: {e}\n")

        if conversation_id in sessions:
            # Already injected for this session
            print(json.dumps({}))
            return

        # Record this session
        sessions.append(conversation_id)
        # Keep last 100 sessions
        sessions = sessions[-100:]
        try:
            with open(log_path, "w", encoding="utf-8") as f:
                json.dump(sessions, f)
        except Exception as e:
            sys.stderr.write(f"Error writing sessions log: {e}\n")

        # Search for SUMMARY.md in workspace paths
        summary_content = None
        for path in workspace_paths:
            summary_file = os.path.join(path, "SUMMARY.md")
            if os.path.exists(summary_file):
                try:
                    with open(summary_file, "r", encoding="utf-8") as f:
                        summary_content = f.read()
                    break # Found and read successfully
                except Exception as e:
                    sys.stderr.write(f"Error reading {summary_file}: {e}\n")

        if not summary_content:
            print(json.dumps({}))
            return

        # Inject the SUMMARY.md content
        inject_message = (
            "=== Workspace Summary from SUMMARY.md ===\n"
            "Here is the summary of the project state from the previous session. "
            "Please read this to understand context, progress, and next steps:\n\n"
            f"{summary_content}\n"
            "========================================"
        )
        
        result = {
            "injectSteps": [
                {
                    "ephemeralMessage": inject_message
                }
            ]
        }
        print(json.dumps(result))

    except Exception as e:
        sys.stderr.write(f"Unhandled exception in hook: {e}\n")
        traceback.print_exc(file=sys.stderr)
        print(json.dumps({}))

if __name__ == "__main__":
    main()
