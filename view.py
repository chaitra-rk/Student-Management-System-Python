from db import connection

def view_students():

    cursor = connection.cursor()

    query = "SELECT * FROM students1"

    cursor.execute(query)

    students = cursor.fetchall()

    print("\n----- Student Records -----")

    for student in students:
        print(student)

    cursor.close()