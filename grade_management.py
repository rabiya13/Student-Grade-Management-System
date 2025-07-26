import csv
import os

FILENAME = "students.csv"

# Initialize the file if it doesn't exist
def initialize_file():
    if not os.path.exists(FILENAME):
        with open(FILENAME, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["RollNo", "Name", "Grade"])

# Add a student record
def add_student():
    roll = input("Enter Roll Number: ")
    name = input("Enter Name: ")
    grade = input("Enter Grade: ")
    
    with open(FILENAME, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([roll, name, grade])
    print("✅ Student added successfully.\n")

# View all students
def view_students():
    with open(FILENAME, mode='r') as file:
        reader = csv.reader(file)
        data = list(reader)

    if len(data) <= 1:
        print("⚠️ No student data found.\n")
        return

    print("\n📋 Student List:")
    for row in data:
        print(", ".join(row))
    print()

# Update student grade
def update_grade():
    roll = input("Enter Roll Number to update: ")
    updated = False

    with open(FILENAME, mode='r') as file:
        rows = list(csv.reader(file))

    for row in rows:
        if row and row[0] == roll:
            new_grade = input(f"Enter new grade for {row[1]}: ")
            row[2] = new_grade
            updated = True
            break

    if updated:
        with open(FILENAME, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(rows)
        print("✅ Grade updated successfully.\n")
    else:
        print("❌ Student not found.\n")

# Delete student record
def delete_student():
    roll = input("Enter Roll Number to delete: ")
    deleted = False

    with open(FILENAME, mode='r') as file:
        rows = list(csv.reader(file))

    new_rows = [row for row in rows if row and row[0] != roll]

    if len(rows) != len(new_rows):
        with open(FILENAME, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(new_rows)
        print("✅ Student deleted successfully.\n")
    else:
        print("❌ Student not found.\n")

# Main menu
def main():
    initialize_file()

    while True:
        print("------ Student Grade Management System ------")
        print("1. Add Student")
        print("2. View Students")
        print("3. Update Grade")
        print("4. Delete Student")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            add_student()
        elif choice == '2':
            view_students()
        elif choice == '3':
            update_grade()
        elif choice == '4':
            delete_student()
        elif choice == '5':
            print("👋 Exiting program. Goodbye!")
            break
        else:
            print("⚠️ Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main()
