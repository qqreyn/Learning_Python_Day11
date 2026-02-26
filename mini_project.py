students = {}
next_id = 1

def add_student():
    global next_id

    name = input("Enter name: ")
    age = input("Enter age: ")
    grade = input("Enter grade: ")
    city = input("Enter city: ")

    students[str(next_id)] = {
        "name": name,
        "age": age,
        "grade": grade,
        "city": city
    }

    print(f"Student added with ID {next_id}")
    next_id += 1

def update_student():
    student_id = input("Enter student ID to update: ")

    student = students.get(student_id)
    
    if not student:
        print("Student not found.")
        return
    
    print("What do you want to update?")
    print("1. Name")
    print("2. Age")
    print("3. Grade")
    print("4. City")

    choice = input("Choose option: ")

    if choice == "1":
        student["name"] = input("New name: ")
    elif choice == "2":
        student["age"] = input("New age: ")
    elif choice == "3":
        student["grade"] = input("New grade: ")
    elif choice == "4":
        student["city"] = input("New city: ")
    else:
        print("Invalid option.")
        return

def show_student():
    student_id = input("Enter student ID: ")

    student = students.get(student_id)

    if not student:
        print("Student not found.")
        return
    
    print("\n--- Student Info ---")
    print(f"ID: {student_id}")
    print(f"Name: {student.get('name', 'N/A')}")
    print(f"Age: {student.get('age', 'N/A')}")
    print(f"Grade: {student.get('grade', 'N/A')}")
    print(f"City: {student.get('city', 'N/A')}")
    print("--------------------\n")

def show_all_students():
    if not students:
        print("No students in database.")
        return
    
    for student_id, info in students.items():
        print("\n--- Student Info ---")
        print(f"ID: {student_id}")
        print(f"Name: {info.get('name', 'N/A')}")
        print(f"Age: {info.get('age', 'N/A')}")
        print(f"Grade: {info.get('grade', 'N/A')}")
        print(f"City: {info.get('city', 'N/A')}")
        print("--------------------")

while True:
    print("\nStudent Database Manager")
    print("1. Add student")
    print("2. Update student")
    print("3. Show one student")
    print("4. Show all students")
    print("5. Exit")

    choice = input("Choose option: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        update_student()
    elif choice == "3":
        show_student()
    elif choice == "4":
        show_all_students()
    elif choice == "5":
        print("Exiting program.")
        break
    else:
        print("Invalid choice. Try again.")