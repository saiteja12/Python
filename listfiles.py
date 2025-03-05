import sys

def process_file(file_path):
    print(f"Processing file: {file_path}")
    # Add your file processing logic here

if __name__ == "__main__":
    files = sys.argv[1:]  # Get files passed from GitHub Actions
    if not files:
        print("No modified files provided.")
        sys.exit(0)

    for file in files:
        process_file(file)
