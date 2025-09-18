
import subprocess
import sys
import argparse
from pathlib import Path
# Default repository URL
repo = "https://github.com/birds-audiovisuel/Interface-RSK-V1.0.0.git"




# Return false if an error occurs
def install_rsk():
    try:
        print("Installing RSK...")
        python_exe = sys.executable # Use the same Python executable that is running this script
        result = subprocess.run([python_exe, '-m', 'pip', 'install', 'robot-soccer-kit[gc]'],
                              capture_output=True, text=True)
        if result.returncode != 0:
            print(f"Error installing RSK: {result.stderr}")
            return False
        print("RSK successfully installed.")
        return True
    except Exception as e:
        print(f"Error during RSK installation: {str(e)}")
        return False

def start_application():
    try:
        print("Starting application...")
        start_script = Path(__file__).parent / 'start.py'
        if not start_script.exists():
            print("Error: start.py not found")
            return False
        subprocess.Popen([sys.executable, str(start_script)])
        return True
    except Exception as e:
        print(f"Error starting application: {str(e)}")
        return False

def main():
    args = parse_arguments()
    if args.repo:
        global repo
        repo = args.repo
    if not args.no_clone:
        if not clone_repository():
            sys.exit(1)
    if not args.no_install:
        if not install_rsk():
            sys.exit(1)
    if not args.no_start:
        if not start_application():
            sys.exit(1)
    sys.exit(0)

if __name__ == "__main__":
    main()