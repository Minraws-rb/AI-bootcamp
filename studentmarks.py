students = {}

for i in range(5):
    name = input("Enter student name: ")
    marks = int(input("Enter student marks: "))
    students[name] = marks 

highest_marks = max(students.values())
lowest_marks = min(students.values())

for name, marks in students.items():
    if marks == highest_marks:
        topper = name
        break

# Calculating average
average = sum(students.values()) / len(students)

# Printing result
print("\nTopper:", topper, "(", highest_marks, ")")
print("Average Marks:", average)
print("Lowest Marks:", lowest_marks)