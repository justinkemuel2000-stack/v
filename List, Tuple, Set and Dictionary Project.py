# ==============================
# STUDENT CLUB & SUBJECT MANAGER
# ==============================

# ------------------------------
# 1️⃣ List Operations
# ------------------------------
Student_Name = ["Jayson", "Justin", "Hannah", "Joy", "Allyn"]
print("List of Students:", Student_Name)

# Display first and last
print("First Student:", Student_Name[0])
print("Last Student:", Student_Name[-1])

# Append, Insert, Remove
Student_Name.append("Jewel")
Student_Name.insert(3, "Kyle")
Student_Name.remove("Jewel")

# Count
Name_Count = Student_Name.count("Jayson")
print("Count of 'Jayson':", Name_Count)

# Reverse, Sort, Extend
Student_Name.reverse()
print("Reverse List:", Student_Name)

Student_Name.sort()
print("Sorted List:", Student_Name)

Another_List = ["Josh", "Arnold", "Mond"]
Student_Name.extend(Another_List)
print("Extended List:", Student_Name)

# Delete item by index
del Student_Name[2]
print("After Deletion:", Student_Name)

# Clear list
Student_Name.clear()
print("Cleared List:", Student_Name)


# ------------------------------
# 2️⃣ Tuple Operations
# ------------------------------
Courses = ("BSCS", "BSIT", "BS-PSYCHOLOGY", "BS-CRIMINOLOGY", "BSMB")
print("\nOriginal Tuple:", Courses)

# Convert tuple to list to update
Courses_list = list(Courses)
Courses_list[2] = "BS-Psychology"
print("Updated List:", Courses_list)

# Convert back to tuple
Courses = tuple(Courses_list)
print("Updated Tuple:", Courses)


# ------------------------------
# 3️⃣ Set Operations
# ------------------------------
Clubs = {"Basketball Club", "Volleyball Club", "Music Club", "Arts Club", "Taekwondo Club"}
print("\nOriginal Clubs:", Clubs)

# Add, Update, Discard
Clubs.add("Science Club")
Clubs.update(["Boxing Club", "Badminton Club", "Math Club", "Spelling Bee Club"])
Clubs.discard("Boxing Club")
print("Updated Clubs:", Clubs)

# Another set
Another_Club = {"Biology Club", "Engineering Club", "Chemistry Club"}

# Union
Union_Clubs = Clubs.union(Another_Club)
print("Union of Clubs:", Union_Clubs)

# Intersection
Intersect_Clubs = Clubs.intersection(Another_Club)
print("Intersection of Clubs:", Intersect_Clubs)

# Symmetric Difference
Symmetric_Clubs = Clubs.symmetric_difference(Another_Club)
print("Symmetric Difference:", Symmetric_Clubs)


# ------------------------------
# 4️⃣ Dictionary Operations
# ------------------------------
Student_info1 = {
    "name": "Ryan",
    "age": 24,
    "course": "BS Mathematics",
    "club": "Football Club"
}

Student_info2 = {
    "name": "Jiem",
    "age": 24,
    "course": "BS Statistics",
    "club": "Artery Club"
}

print("\nStudent Info 1:", Student_info1)
print("Student Info 2:", Student_info2)

# Update value
Student_info1["age"] = 25
Student_info2["course"] = "BS Applied Math"

# Pop
Student_info2.pop("club")
Student_info1.popitem()  # removes last inserted key-value pair

# Keys and Values
print("Keys of Student 1:", Student_info1.keys())
print("Values of Student 1:", Student_info1.values())

# List of dictionaries
List_of_Dict = [Student_info1, Student_info2]
print("List of Student Dictionaries:", List_of_Dict)
