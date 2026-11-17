from db import connection
def update_student():
    cursor = connection.cursor()
    student_id = int(input("Enter Student ID to Update: "))
    name = input("Enter New Name: ")
    age = int(input("Enter New Age: "))
    branch = input("Enter New Branch: ")
    cgpa = float(input("Enter New CGPA: "))
    query = """
    UPDATE students1
    SET 
    name = %s,
    age = %s,
    branch = %s,
    cgpa = %s
    WHERE id = %s
    """
    cursor.execute(query, (name, age, branch, cgpa, student_id))
    connection.commit()
    if cursor.rowcount > 0:
     print("✅ Student Updated Successfully!")
    else:
     print("❌ Student ID not found.")
    cursor.close()