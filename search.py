from db import connection

def search_student():

    cursor = connection.cursor()

    print("\n===== SEARCH STUDENT =====")
    print("1. Search by ID")
    print("2. Search by Name")
    print("3. Search by Branch")
    print("4. Search by CGPA")
    print("5. Search by Age")
    print("6. Back")

    choice = int(input("\nEnter Choice: "))

    if choice == 1:
        student_id = int(input("Enter Student ID: "))
        query = "SELECT * FROM students1 WHERE id = %s"
        cursor.execute(query, (student_id,))
        students = cursor.fetchall()

    elif choice == 2:
        name = input("Enter Student Name: ")
        query = "SELECT * FROM students1 WHERE name = %s"
        cursor.execute(query, (name,))
        students = cursor.fetchall()

    elif choice == 3:
        branch = input("Enter Student Branch: ")
        query = "SELECT * FROM students1 WHERE branch = %s"
        cursor.execute(query, (branch,))
        students = cursor.fetchall()

    elif choice == 4:
        cgpa = float(input("Enter Student CGPA: "))
        query = "SELECT * FROM students1 WHERE cgpa = %s"
        cursor.execute(query, (cgpa,))
        students = cursor.fetchall()

    elif choice == 5:
        age = int(input("Enter Student Age: "))
        query = "SELECT * FROM students1 WHERE age = %s"
        cursor.execute(query, (age,))
        students = cursor.fetchall()

    elif choice == 6:
        cursor.close()
        return

    else:
        print("Invalid Choice!")
        cursor.close()
        return

    if students:

        print("\n========== STUDENT DETAILS ==========\n")

        for student in students:
            print(f"ID      : {student[0]}")
            print(f"Name    : {student[1]}")
            print(f"Age     : {student[2]}")
            print(f"Branch  : {student[3]}")
            print(f"CGPA    : {student[4]}")
            print("----------------------------------")

    else:
        print("\nStudent not found.")

    cursor.close()