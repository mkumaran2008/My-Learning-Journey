student = {
    "name": "Kumaran",
    "age": 18,
    "course": "AI and Data Science"
}

print("Student Name:", student["name"])
print("Age:", student["age"])
print("Course:", student["course"])

# Add a new detail
student["college"] = "SKCET"

# Update age
student["age"] = 19

print("Updated Student Details:", student)

# Display all keys
print("Keys:", student.keys())
