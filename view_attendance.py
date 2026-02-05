def view_attendance(attendance):
    print("\n--- Attendance Report ---")
    for name, status in attendance.items():
        print(name, ":", status)
