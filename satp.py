total_classes = int(input("Enter the total number of classes held: "))
attended_classes = int(input("Enter the number of classes attended: "))
if total_classes == 0:
    print("Total classes cannot be zero.")
else:
    attendance_percent = (attended_classes / total_classes) * 100
    print("\nAttendance Report")
    print("-----------------")
    print(f"Classes Held: {total_classes}")
    print(f"Classes Attended: {attended_classes}")
    print(f"Attendance: {attendance_percent:.2f}%")
    if attendance_percent >= 75:
        print("Status:Eligible for exams")
    else:
        print("Status:Not eligible for exams")