# read_sample.py

try:
    # 1. Open file using with -> automatically closes the file
    with open("sample.txt", "r") as file:
        print("Reading file content:\n")

        # 2. Read line by line and print with line numbers
        line_number = 1
        for line in file:
            print(f"Line {line_number}: {line.strip()}")
            line_number += 1

except FileNotFoundError:
    # 3. Handle the case where sample.txt does not exist
    print("Error: The file 'sample.txt' was not found.")
except Exception as e:
    # 4. Catch any other unexpected errors
    print(f"An unexpected error occurred: {e}")
