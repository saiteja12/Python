import sys

def process_file(file_path):
    print(f"Processing file: {file_path}")

if __name__ == "__main__":
    files = sys.argv[1:]  # Get files passed from GitHub Actions

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
