import mark_attendance
import view_attendance

attendance_data = {}

while True:
    print("\n1. Mark Attendance")
    print("2. View Attendance")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter student name: ")
        status = input("Enter Present/Absent: ")
        attendance_data = mark_attendance.mark_attendance(name, status)

    elif choice == "2":
        view_attendance.view_attendance(attendance_data)

    elif choice == "3":
        print("Exiting program")
        break

    else:
        print("Invalid choice")
