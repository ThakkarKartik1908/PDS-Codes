#3.2
import csv

# Create CSV file with nop need to closed without with need
with open("students.csv", "w", newline="") as file:
    writer = csv.writer(file)

    # Write header
    writer.writerow(["Name", "Roll No", "CGPA"])

    # Write student records one by one
    writer.writerow(["Amit", 101, 8.2])
    writer.writerow(["Neha", 102, 7.1])
    writer.writerow(["Rahul", 103, 9.0])
    writer.writerow(["Priya", 104, 7.8])
    writer.writerow(["Karan", 105, 6.9])

print("CSV file created successfully.")

# Read CSV file and display students with CGPA > 7.5
print("\nStudents with CGPA > 7.5:")

with open("students.csv", "r") as file:
    reader = csv.reader(file)

    # Skip header
    next(reader)

    for row in reader:
        if float(row[2]) > 7.5:
            print("Name:", row[0])
            print("Roll No:", row[1])
            print("CGPA:", row[2])
            print()