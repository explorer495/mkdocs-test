
awk -f pull_cmdref.awk ../CommandStation-EX/DCCEXCommands.h | out-file -encoding UTF8 docs/reference/serial_commands.md

