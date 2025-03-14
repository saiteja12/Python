import os
import sys

def process_file(file_path):
    print(f"Processing file: {file_path}")

if __name__ == "__main__":
    files = os.getenv("MODIFIED_FILES").split('\n')  # Get files passed from GitHub Actions
    DRY_RUN = os.getenv("DRY_RUN")
    if DRY_RUN == 'true':
        print('DRY_RUN is set')
    else:
        print('Not set')
    print('executing')
    print(files)

    if not files:
        print("No modified files provided.")
        sys.exit(0)

    # Filter files that are inside the 'config/' directory
    config_files = [file for file in files if file.startswith("config/")]

    if not config_files:
        print("No modified files in the 'config/' folder.")
        sys.exit(0)

    for file in config_files:
        process_file(file)
