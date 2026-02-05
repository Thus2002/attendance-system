print("Modify Attendance")

attendance = {}

# Step 1: Enter attendance
while True:
    name = input("\nEnter student name (or type 'done' to finish): ")

    if name.lower() == "done":
        break

    status = input("Enter Present/Absent: ")
    attendance[name] = status

# Step 2: Display current attendance
print("\n--- Current Attendance ---")
for name, status in attendance.items():
    print(name, ":", status)

# Step 3: Modify attendance
choice = input("\nDo you want to modify attendance? (yes/no): ")

if choice.lower() == "yes":
    name = input("Enter student name to modify: ")

    if name in attendance:
        new_status = input("Enter corrected status (Present/Absent): ")
        attendance[name] = new_status
        print("Attendance updated successfully.")
    else:
        print("Student not found.")

# Step 4: Final attendance report
print("\n--- Final Attendance Report ---")
for name, status in attendance.items():
    print(name, ":", status)
