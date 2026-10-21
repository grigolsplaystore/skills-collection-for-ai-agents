---
name: summarize
description: >-
  Summarize the current session/workspace context and write it to SUMMARY.md in the current directory for the agent.
---

# Summarize Session

## Overview
This skill allows the agent to automatically summarize the active workspace, session history, files modified, and next steps, and persist it to `SUMMARY.md`. In future sessions for the agent as a backround information, a global startup hook will automatically locate and read this file to instantly restore context.

## Dependencies
None

## Quick Start
To trigger this skill, the user can ask the agent to summarize the current session. The agent will then generate a comprehensive summary of the work done and write it to `SUMMARY.md` in the workspace root directory.

## Workflow
When the user asks you to summarize the session or workspace, perform the following steps:
1. Check if a `SUMMARY.md` file already exists in the active workspace directory. If it does, read it to preserve the historical context, project background, and previous milestones.
2. Analyze the conversation transcript (from the artifact directory or memory) and identify the new changes made to files, current status, and planned next steps in this session.
3. Formulate a consolidated, clear, concise, and structured summary that merges the existing project history from `SUMMARY.md` with the new updates.
4. Analyze and refine. Clean up and remove irrelevant, old stuff. Keep only what's needed. Especially are needed: file locations, information about generated and helpful scripts, URLs, credential locations, resource locations.
5. Make summary as short as possible with maximum efficiency for the agent.
6. Overwrite `SUMMARY.md` in the current workspace directory with this updated, consolidated summary.
7. **Mandatory Git Repository Check & Commit Protocol**:
   - Check if a git repository exists in the workspace by running `git status`.
   - If there are modified, deleted, or untracked files:
     a. Ensure all project-specific pre-commit rules (such as targeted version bumping, linting, tests) have been satisfied.
     b. Stage all relevant modified, untracked, and deleted files, including `SUMMARY.md` (`git add <files>...` or `git add .`).
     c. Create a clear, conventional commit (e.g., `feat: ...`, `fix: ...`, `chore: update session summary and project docs`).
     d. Run `git status` to verify the working tree is clean.
8. Inform the user that the session has been summarized, `SUMMARY.md` has been updated, and report the commit hash and committed files.

## Common Mistakes
- **Writing to a different filename**: Always write exactly to `SUMMARY.md` in the active workspace directory.
- **Forgetting to update**: Always rewrite or update `SUMMARY.md` when the user requests a summary, ensuring the latest progress is captured.
- **Skipping Git Commit**: Never conclude the summary task leaving unstaged or uncommitted changes in the repository. Always check `git status`, stage all files (including `SUMMARY.md`), commit them, and verify that the working tree is clean.
- **Missing Project Pre-Commit Rules**: Always check and respect workspace-specific guidelines (such as targeted component version bumping) prior to committing.
