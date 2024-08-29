# ------------------------------------------------------------------------------------------ #
# Title: Assignment05
# Desc: This assignment demonstrates using dictionaries, files, and exception handling
# Change Log: (Who, When, What)
#   RRoot,1/1/2030,Created Script
#   Ogonna Anunoby, 08/24/2024, First attempt at Assignment05
# ------------------------------------------------------------------------------------------ #

# Define the Data Constants
MENU: str = """
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
"""
FILE_NAME: str = "Enrollments.csv"

# Define the Data Variables
student_first_name: str = ''  # Holds the first name of a student entered by the user.
student_last_name: str = ''  # Holds the last name of a student entered by the user.
course_name: str = ''  # Holds the name of a course entered by the user.
student_data: list = []  # one row of student data
students: list = []  # a table of student data
csv_data: str = ''  # Holds combined string data separated by a comma.
file = None  # Holds a reference to an opened file.
menu_choice: str  # Hold the choice made by the user.

# When the program starts, read the file data into table
# Extract the data from the CSV file into a list of dictionaries
try:
    file = open(FILE_NAME, "r")
    
    for row in file.readlines():
        # Transform the data from the file
        student_data = row.split(',')
        student_data = {"FirstName": student_data[0], 
                        "LastName": student_data[1], 
                        "CourseName": student_data[2].strip()}
        # Load it into our collection (list of lists)
        students.append(student_data)
        file.close()
except FileNotFoundError as e: 
    print("Text file must exist before running this script!\n")
    print("-- Technical Error Message -- ")
    print(e, e.__doc__, e.__str__(), type(e), sep="\n")
    print("Creating file...")
    file = open(FILE_NAME, "w")
except Exception as e: 
    print("There was a non-specific error!\n")
    print("-- Technical Error Message -- ")
    print(e, e.__doc__, e.__str__(), type(e), sep="\n")
finally:
    if not file.closed:
        file.close()

# Present and Process the data
while (True):

    # Present the menu of choices
    print(MENU)
    menu_choice = input("What would you like to do: ")

    # Input user data
    if menu_choice == "1":  # This will not work if it is an integer!
        try:
            # Input the data
            student_first_name = input("Enter the student's first name: ")
            if not student_first_name.isalpha(): # Check if only letters are entered
                raise ValueError("The first name should only contain letters.")

            student_last_name = input("Enter the student's last name: ")
            if not student_last_name.isalpha(): # Check if only letters are entered
                raise ValueError("The last name should only contain letters.")
        except ValueError as e:  # Catch value error exceptions
                print(e)  # Prints the custom message
                print("-- Technical Error Message -- ")
                print(e.__doc__)
                print(e.__str__())
                print(type(e))
        except Exception as e: # Catch general exceptions
            print("There was a non-specific error!\n")
            print("-- Technical Error Message -- ")
            print(e, e.__doc__, e.__str__(),type(e), sep="\n")
        else:
            course_name = input("Enter the name of the course: ")
            student_data = {"FirstName": student_first_name,"LastName": student_last_name, "CourseName" : course_name}
            students.append(student_data)
            print(f"You have registered {student_first_name} {student_last_name} for {course_name}.")
        continue

    # Present the current data
    elif menu_choice == "2":

        # Process the data to create and display a custom message
        print("-"*50)
        for student in students:
            print(f"Student {student['FirstName']} {student['LastName']} is enrolled in {student['CourseName']}")
        print("-"*50)
        continue

    # Save the data to a file
    elif menu_choice == "3":
        try:
            file = open(FILE_NAME, "w")
            for student in students:
                csv_data = f"{student['FirstName']},{student['LastName']},{student['CourseName']}\n"
                file.write(csv_data)
            file.close()
            print("The following data was saved to file!")
            for student in students:
                print(f"Student {student['FirstName']} {student['LastName']} is enrolled in {student['CourseName']}")
        except TypeError as e: # Catch type error exceptions
            print("Please check that the data is a compatable with CSV files\n")
            print("-- Technical Error Message -- ")
            print(e, e.__doc__, e.__str__(), type(e), sep="\n")
        except Exception as e: # Catch general exceptions
            print("There was a non-specific error!\n")
            print("-- Technical Error Message -- ")
            print(e, e.__doc__, e.__str__(), type(e), sep="\n")
        finally:
            if not file.closed:
                file.close()       
        continue

    # Stop the loop
    elif menu_choice == "4":
        break  # out of the loop
    else:
        print("Please only choose option 1, 2, or 3")

print("Program Ended")
