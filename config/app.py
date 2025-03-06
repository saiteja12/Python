import sys
import json

def main():
    # Read modified files from command-line argument
    modified_files_json = sys.argv[1]

    # Convert JSON string to Python list
    modified_files = json.loads(modified_files_json)

    # Print the filtered files
    print("Modified config files:")
    for file in modified_files:
        print(file)

if __name__ == "__main__":
    main()
