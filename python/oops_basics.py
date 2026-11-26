# Write information into a file
with open("student.txt", "w") as file:
    file.write("Name: Kumaran\n")
    file.write("Course: AI and Data Science\n")

# Read information from the file
with open("student.txt", "r") as file:
    content = file.read()
    print("Student Details:")
    print(content)

# Append new information
with open("student.txt", "a") as file:
    file.write("College: SKCET\n")

print("New information added.")
