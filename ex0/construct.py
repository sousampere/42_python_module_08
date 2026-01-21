#!/usr/bin/python3

import sys
import os
import site


def matrix_status(is_venv: bool, python: str, package: str,
                  env_path: str) -> None:
    """Prints the env, if it is a venv or not"""
    if (is_venv):
        status = "Welcome to the construct"
    else:
        status = "You're still plugged in"
    print(f'MATRIX STATUS: {status}\n')
    print(f'Current Python: {python}')
    if (not is_venv):
        print("Virtual Environment: None detected\n")
        print("WARNING: You're in the global environment!")
        print("The machines can see everything you install.\n")
        print("""To enter the construct, run:
python -m venv matrix_env
source matrix_env/bin/activate # On Unix
matrix_env
Scripts
activate # On Windows
Then run this program again.""")
    else:
        print(f"Virtual Environment: {os.path.basename(env_path)}")
        print(f'Environment Path: {env_path}')
        print("""\nSUCCESS: You're in an isolated environment!
Safe to install packages without affecting
the global system.\n
Package installation path:\n""" + package)


if __name__ == '__main__':
    if 'VIRTUAL_ENV' in os.environ:
        is_venv = True
        venv_name = os.path.basename(sys.prefix)
    else:
        is_venv = False
        venv_name = None
    python = sys.executable
    path = site.getsitepackages()[0]
    matrix_status(is_venv, python, path, sys.prefix)
