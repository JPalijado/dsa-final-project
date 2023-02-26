import sys
import csv

# For font styles (public declaration as of the moment)
bold = '\033[1m'
default = '\033[m'

def loadStudentDataBase():
    studentDataBase = []
    with open("StudentDetails.csv") as file:
        studentDetails = csv.reader(file)
        # Skip the header
        next(studentDetails)

        for row in studentDetails:
            studentDataBase.append(row)
    return studentDataBase

# Start Function
def startFeature():
    # Displays the selection for student level
    print(bold + "Select The Student Level:")
    print(default + "==================================================")
    print("(U) Undergraduate")
    print("(G) Graduate")
    print("(B) Both")
    print("==================================================")
    # Initiates the while loop of selecting student level
    isSelectingLevel = True
    # Loops until the selection of student level is done
    while isSelectingLevel:
        # Initializes empty lists for data holders
        level = []
        degree = []
        # Ask input for level selection
        levelSelection = verifyInput(str, bold + "Enter Your Selection: " + default, default + "Try again, please input a string.\n")
        if levelSelection == "U":
            # Stops the while loop
            isSelectingLevel = False
            # Cancels the searching for Graduate Degree
            isSearchingGraduateDegree = False
            # Set the student level to just Undergraduate
            level = ["U", ""]
        elif levelSelection == "G" or levelSelection == "B":
            # Stops the while loop
            isSelectingLevel = False
            # Indicates that the user is searching for Graduate Degree
            isSearchingGraduateDegree = True
            if levelSelection == "G":
                # Set the student level to just Graduate
                level = ["G", ""]
            elif levelSelection == "B":
                # Set the student level to both Undergraduate and Graduate
                level = ["U", "G"]
            # Displays the additional selection for Graduate and Both
            print("(M) Master")
            print("(D) Doctorate")
            print("(B0) Both")
            print("==================================================")
            # Initiates the while loop of selecting student degree
            isSelectingDegree = True
            # Loops until the searching for the desired degree is done
            while isSelectingDegree:
                graduateLevelSelection =  verifyInput(str, bold + "Enter Your Selection: " + default, default + "Try again, please input a string.\n")
                if graduateLevelSelection == "M":
                    # Stops the while loop
                    isSelectingDegree = False
                    # Set the degrees to be searched, BS1 is included just in case the user wants both Undergraduate and Graduate Data
                    degree = ["M1", "M2", "BS1", ""]
                elif graduateLevelSelection == "D":
                    # Stops the while loop
                    isSelectingDegree = False
                    # Set the degrees to be searched, BS1 is included just in case the user wants both Undergraduate and Graduate Data
                    degree = ["D1", "BS1", "", ""]
                elif graduateLevelSelection == "B0":
                    # Stops the while loop
                    isSelectingDegree = False
                    # Set the degrees to be searched, BS1 is included just in case the user wants both Undergraduate and Graduate Data
                    degree = ["M1", "M2", "D1", "BS1"]
                else:
                    # Tells the user that the selection is out of range
                    print("Not a valid selection. Please try again.")
        else:
            # Tells the user that the selection is out of range
            print("Not a valid selection. Please try again.")
    # Returns the student level, student degree, and if the user is searching for graduate degree
    return level, degree, isSearchingGraduateDegree

# Main Menu Function
def menuFeature():
    print(bold + "\nStudent Transcript Generation System")
    print(default + "==================================================")
    print("1. Student details")
    print("2. Statistics")
    print("3. Transcript based on major courses")
    print("4. Transcript based on minor courses")
    print("5. Full transcript")
    print("6. Previous transcript request")
    print("7. Select another student")
    print("8. Terminate the system")
    print("==================================================")
    choice = verifyInput(int, bold + "Enter Your Feature: " + default, default + "Try again, please input an integer.\n")
    return choice

def selectMenuFeature(studentData):
    while True:
        choice = menuFeature()
        if choice == 1:
            detailsFeature(studentData)
        elif choice == 8:
            terminateFeature()
        else:
            print("Selection out of range. Please try again.")

def initializeMenu():
    studentLevel, studentDegree, isSearchingGraduateDegree = startFeature()
    studentDataBase = loadStudentDataBase()
    isSearching = True
    check = -1
    # Initializes a studentData list where the matched data from the stdID, level, and degree will be stored 
    studentData = []
    while isSearching:
        stdID  = verifyInput(int, "\nEnter Student ID: ", "Try again, please input an integer.\n")
        for i in range(len(studentDataBase)):
            if stdID == int(studentDataBase[i][1]) and (studentLevel[0] == studentDataBase[i][5] or studentLevel[1] == studentDataBase[i][5]):
                    if isSearchingGraduateDegree:
                        if studentDegree[0] == studentDataBase[i][6] or studentDegree[1] == studentDataBase[i][6] or studentDegree[2] == studentDataBase[i][6] or studentDegree[3] == studentDataBase[i][6]:
                            studentData.append(studentDataBase[i])
                            check = i
                    else:
                        studentData.append(studentDataBase[i])
                        check = i
        if check == -1:
            print("Student ID does not exist in the selected student level. Please try again")
        else:
            isSearching = False
    selectMenuFeature(studentData)

def detailsFeature(studentData):
    # Displays a "Student Details" text
    print(bold + "\nStudent Details" + default)
    # Reads all levels
    levels = ""
    for i in range(len(studentData)):
        if i == 0:
            # Concatinates the first data
            levels += studentData[i][5]
        # Checks if the data not the same as the previous one to avoid repetition
        if i != 0 and studentData[i][5] != studentData[i-1][5]:
            # Adds a coma to the next data
            levels += ", " + studentData[i][5]

    # Reads all number of terms
    terms = ""
    for i in range(len(studentData)):
        if i == 0:
            # Concatinates the first data
            terms += studentData[i][9]
        # Adds a coma to the next data
        if i != 0:
            terms += ", " + studentData[i][9]

    # Reads all colleges
    colleges = ""
    for i in range(len(studentData)):
        if i == 0:
            # Concatinates the first data
            colleges += studentData[i][3]
        # Checks if the data not the same as the previous one to avoid repetition
        if i != 0 and studentData[i][3] != studentData[i-1][3]:
            # Adds a coma to the next data
            colleges += ", " + studentData[i][3]
    
    # Reads all colleges
    departments = ""
    for i in range(len(studentData)):
        if i == 0:
            # Concatinates the first data
            departments += studentData[i][4]
        # Checks if the data not the same as the previous one to avoid repetition
        if i != 0 and studentData[i][4] != studentData[i-1][4]:
            # Adds a coma to the next data
            departments += ", " + studentData[i][4]

    print(f"Name: {studentData[0][2]}")
    print(f"stdID: {studentData[0][1]}")
    print(f"Level(s): {levels}")
    print(f"Number of terms: {terms}")
    print(f"College(s): {colleges}")
    print(f"Departments: {departments}")

# Function that verifies the input of the user
def verifyInput(dataType, Inputmessage, Errormessage):
    inputMode = True
    while inputMode:
        try:
            # Reads the desired integer
            n = dataType(input(Inputmessage))
            # Stops the input process
            inputMode = False
        except ValueError:
            # Asks the user to input an integer
            print(Errormessage)
    # returns the valid integer
    return n

def terminateFeature():
    sys.exit("\nTerminating the system, thank you...")

initializeMenu()