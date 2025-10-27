"""
ASSIGNMENT 4:
Task 2: Write and Append Data to a File

Problem Statement: Write a Python program that:
1.   Takes user input and writes it to a file named output.txt.
2.   Appends additional data to the same file.
3.   Reads and displays the final content of the file.


"""
# Step 1: Take user input and write it to a file
text_to_write = input("Enter text to write to the file: ")

with open("output.txt", "w") as file:
    file.write(text_to_write + "\n")

print("Data successfully written to output.txt.\n")

# Step 2: Append additional data
text_to_append = input("Enter additional text to append: ")

with open("output.txt", "a") as file:
    file.write(text_to_append + "\n")

print("Data successfully appended.\n")

# Step 3: Read and display the final content
print("Final content of output.txt:")
with open("output.txt", "r") as file:
    print(file.read().strip())
