class AttendanceTracker:
    def __init__(self):
        self.attendance = {}

    def mark_attendance(self, name):
        if name in self.attendance:
            print(f"{name} is already marked present.")
        else:
            self.attendance[name] = True
            print(f"{name} marked present.")

    def check_attendance(self, name):
        if name in self.attendance:
            print(f"{name} is present.")
        else:
            print(f"{name} is absent.")

    def list_attendance(self):
        if not self.attendance:
            print("No one is present.")
        else:
            print("List of attendees:")
            for name in self.attendance:
                print(name)

    def clear_attendance(self):
        self.attendance.clear()
        print("Attendance has been cleared.")

# Example usage:
tracker = AttendanceTracker()

while True:
    print("\nAttendance Tracker Menu:")
    print("1. Mark Attendance")
    print("2. Check Attendance")
    print("3. List All Attendees")
    print("4. Clear Attendance")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        name = input("Enter name to mark attendance: ")
        tracker.mark_attendance(name)
    elif choice == '2':
        name = input("Enter name to check attendance: ")
        tracker.check_attendance(name)
    elif choice == '3':
        tracker.list_attendance()
    elif choice == '4':
        tracker.clear_attendance()
    elif choice == '5':
        print("Exiting the Attendance Tracker.")
        break
    else:
        print("Invalid choice! Please enter a valid option.")
