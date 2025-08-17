Copilot instructions for this repo
==================================

When updating lessons, include a very short code change in one of the example files so I can understand.

Rules for lesson updates:

- Each lesson that includes a hands-on change, modify those parts and ask for running the next command.
- Use the example files under `examples/`.
- Prefer single-line, clear edits to create merge conflicts (for example change a numeric constant or string literal).
- Aflways include both the PowerShell git commands and the exact VS Code steps to perform the same actions.

Examples of safe edits:

- Change `DEFAULT_ROWS = 5` to `DEFAULT_ROWS = 7` in `examples/stars.py`.
- Change `EXTRA_SOUND = "Meow!"` to `EXTRA_SOUND = "Purr!"` in `examples/animals.py`.

Always make changes to code files directly.

Don't attempt to edit code using terminal commands. Only use terminal commands when needed.
