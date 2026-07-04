import os
import subprocess

MESSAGE_COLOR = "\033[93m"
RESET_ALL = "\033[0m"

print(f"{MESSAGE_COLOR}Initializating a git repository...{RESET_ALL}")

subprocess.run(["git", "init"], check=True)
subprocess.run(["git", "add", "."], check=True)
subprocess.run(["git", "commit", "-m", "Initial commit"], check=True)

print(f"{MESSAGE_COLOR}Git repository initialized successfully!{RESET_ALL}")