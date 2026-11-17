from db import connection
def delete_student():
    cursor = connection.cursor()
    student_id = int(input("Enter student id to delete: "))
    confirm = input("Are you sure? (y/n): ")
    if confirm.lower() != "y":
     print("Deletion Cancelled.")
     cursor.close()
     return
    query = "DELETE FROM students1 WHERE id = %s"
    cursor.execute(query, (student_id,))
    connection.commit()
    if cursor.rowcount > 0:
        print("✅ Student Deleted Successfully!")   
    else:
        print("❌ Student ID not found.")
    cursor.close()