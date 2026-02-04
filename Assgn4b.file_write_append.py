# file_write_append.py

# Step 1: Write input to file (overwrites existing file)
text = input("Enter text to write to the file: ")
with open("output.txt", "w", encoding="utf-8") as file:
    file.write(text)
print("Data successfully written to output.txt.\n")

# Step 2: Append additional input to the same file
extra_text = input("Enter additional text to append: ")
with open("output.txt", "a", encoding="utf-8") as file:
    file.write("\n" + extra_text)
print("Data successfully appended.\n")

# Step 3: Read and display the final content
print("Final content of output.txt:")
with open("output.txt", "r", encoding="utf-8") as file:
    for line in file:
        print(line, end="")