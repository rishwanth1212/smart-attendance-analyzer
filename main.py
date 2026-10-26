import csv
import os

def analyze_attendance(input_filename="attendance.csv", output_filename="attendance_summary.csv", threshold=75.0):
    print("=" * 65)
    print("          SMART ATTENDANCE ANALYZER - REPORT          ")
    print("=" * 65)
    
    if not os.path.exists(input_filename):
        print(f"Error: Could not find '{input_filename}'. Please make sure the file exists.")
        return

    records = []
    low_attendance_count = 0

    with open(input_filename, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            name = row['StudentName']
            total = int(row['TotalClasses'])
            attended = int(row['ClassesAttended'])
            
            percentage = (attended / total) * 100 if total > 0 else 0.0
            status = "Safe" if percentage >= threshold else "Shortage (< 75%)"
            
            if status.startswith("Shortage"):
                low_attendance_count += 1
                
            records.append({
                'StudentName': name,
                'TotalClasses': total,
                'ClassesAttended': attended,
                'Percentage': round(percentage, 2),
                'Status': status
            })

    # Print results formatted to the console
    print(f"{'Student Name':<25} | {'Total':<6} | {'Attended':<8} | {'%':<6} | {'Status'}")
    print("-" * 65)
    for r in records:
        print(f"{r['StudentName']:<25} | {r['TotalClasses']:<6} | {r['ClassesAttended']:<8} | {r['Percentage']}% | {r['Status']}")
    
    print("-" * 65)
    print(f"Total Students Analyzed: {len(records)}")
    print(f"Students with Attendance Shortage: {low_attendance_count}")
    print("=" * 65)

    # Save the summary report to a new CSV file
    with open(output_filename, mode='w', newline='', encoding='utf-8') as outfile:
        fieldnames = ['StudentName', 'TotalClasses', 'ClassesAttended', 'Percentage', 'Status']
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()
        for r in records:
            writer.writerow(r)
            
    print(f"Summary report successfully exported to '{output_filename}'\n")

if __name__ == "__main__":
    analyze_attendance()