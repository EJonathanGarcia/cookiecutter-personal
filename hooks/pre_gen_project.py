import os
import sys

project_slug = "{{ cookiecutter.project_slug }}"

ERROR_COLOR = "\033[91m"
MESSAGE_COLOR = "\033[93m"
RESET_ALL = "\033[0m"

if project_slug.startswith("x"):
    print(
        f"{ERROR_COLOR}ERROR: {project_slug=} cannot start with 'cookiecutter-'. Please choose a different name.{RESET_ALL}"
    )
    sys.exit(1)
    
print(f"{MESSAGE_COLOR} Let's do it! You are going to create something amazing! {RESET_ALL}")
print(f"{MESSAGE_COLOR}Project slug is valid: {project_slug}{RESET_ALL}")