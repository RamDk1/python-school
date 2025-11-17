#Ramses Rodriguez
#11/24/2024
# Given a list strings containing
#   department code, course number, course title, enrollment
# Print a series of tables in different formats
# Unfortunately, the spacing between each of these items was lost when
# each string was generated. You will have to deal with this in your program. 
#  
def main():
    # Read courses from the file
    with open("courses.txt", "r") as file:
        courses = [line.strip() for line in file]

    # Table 1: Print department code and course number
    print("Table 1")
    for aCourse in courses:
        dept_code = aCourse[:2]
        course_num = aCourse[2:5]
        print(f"{dept_code} {course_num}")
    print()

    # Table 2: Print all data with single space between components
    print("Table 2")
    for aCourse in courses:
        dept_code = aCourse[:2]
        course_num = aCourse[2:5]
        # Use regex to find the last digits (enrollment number)
        import re
        enroll = re.search(r'\d+$', aCourse).group()  # Extract the enrollment number
        title = aCourse[5:-len(enroll)]  # Title is everything between department + course + enrollment
        print(f"{dept_code} {course_num} {title} {enroll}")
    print()

    # Table 3: Truncate titles and align enrollments
    print("Table 3")
    total_enrollment = 0
    for aCourse in courses:
        dept_code = aCourse[:2]
        course_num = aCourse[2:5]
        enroll = int(re.search(r'\d+$', aCourse).group())  # Convert enrollment to integer
        title = aCourse[5:-len(str(enroll))]
        truncated_title = title[:24]  # Truncate to 24 characters
        print(f"{dept_code} {course_num} {truncated_title:<25} {enroll:3}")
        total_enrollment += enroll
    print(f"                     Total: {total_enrollment}")
    print()

    # Table 4: Sort courses and print aligned data
    print("Table 4")
    sorted_courses = sorted(courses, key=lambda x: x[:5])  # Sort by department code + course number
    max_title_length = max(len(aCourse[5:-len(str(re.search(r'\d+$', aCourse).group()))]) for aCourse in courses)  # Find the longest title length
    for aCourse in sorted_courses:
        dept_code = aCourse[:2]
        course_num = aCourse[2:5]
        enroll = int(re.search(r'\d+$', aCourse).group())
        title = aCourse[5:-len(str(enroll))]
        print(f"{dept_code}{course_num} {title:<{max_title_length}} {enroll:3}")

# Run the program
main()
