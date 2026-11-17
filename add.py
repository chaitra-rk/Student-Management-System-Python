from db import connection

def add_student():

    cursor = connection.cursor()

    student_id = int(input("Enter ID: "))
    name = input("Enter Name: ")
    age = int(input("Enter Age: "))
    branch = input("Enter Branch: ")
    cgpa = float(input("Enter CGPA: "))

    query = """
    INSERT INTO students1(id, name, age, branch, cgpa)
    VALUES (%s, %s, %s, %s, %s)
    """

    values = (student_id, name, age, branch, cgpa)

    try:
        cursor.execute(query, values)
        connection.commit()
        print("\n✅ Student Added Successfully!")

    except Exception as e:
        print("\n❌", e)

    cursor.close()