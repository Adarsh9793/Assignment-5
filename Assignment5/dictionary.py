Student_marks = {"Adarsh" :85 , "Ravi": 90, "Suresh": 78, "Priya": 92, "Anita": 88}

name = input("Enter the student's name:")

if name in Student_marks:
    print(f"{name}'s marks are: {Student_marks[name]}")
else:
    print("Student not found.")