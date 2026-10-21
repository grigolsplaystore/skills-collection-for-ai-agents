
# Rule: Ask, Don't Assume
- Always ask the user for details or clarification when requirements are underspecified, ambiguous, or have multiple design/implementation paths.
- Do not make assumptions or default decisions on the user's behalf.

# Rule: Read SUMMARY.md
- If a `SUMMARY.md` file exists in the workspace root directory, always check and read its contents before your first response to user request in the current session.

# Rule: Never Modify Other Projects
- Never fix, change, or modify code in other projects outside the current workspace unless the user explicitly requests it.
- Other projects may only be read for reference purposes (e.g., porting patterns, understanding APIs).
- If a bug is found in another project, report it — do not fix it. The user will address it in a separate session.

