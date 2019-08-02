# Pushing large files to XSA

## Prerequisites
1. You have to have XSA cli runnable through the command `xs`
2. Python runtime should be installed on XSA. Project is set to version 3.6.5. You can adjust this setting in `requirement.txt` if you have different runtime version. Some changes may be required in `server.py`, but it may not be necessary .

## Testing
Run `bash run.sh` this will generate 850Mb file and try to push it to XSA. You may set the target space before pushing `xs t -s <SPACE>`.