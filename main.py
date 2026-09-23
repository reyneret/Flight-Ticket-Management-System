# ===================================
# NgeFly: Flight Ticket Management System
# ===================================
# Developed by Reyner Elazaro Tampubolon
# JCDSBSD - 34



# /===== Library Imports & Global Variables=====/
import pwinput
from tabulate import tabulate
import sys
import copy
from datetime import datetime
import re
loginUsername = None
waitList = []



# /===== Data Models =====/
# Flight Data:
flightHeaders = ["Flight ID", "Departure Time", "Arrival Time", "Flying From", "Heading To", "Plane", "Flight Type", "Price"]
flightData = [
    ["B-JAK-DEN-2026/09/24", "2026/09/24 07:25", "2026/09/24 11:40", "Jakarta, Indonesia", "Denpasar, Indonesia", "Boeing 747", "Business", 6_500_000],
    ["E-JAK-BAN-2026/09/30", "2026/09/15 09:30", "2026/09/16 11:40", "Jakarta, Indonesia", "Bandung, Indonesia", "Airbus 300", "Economy", 3_000_000]
]
# Booking Data:
bookHeaders = ["Booked Flight", "Full Name", "Date of Birth", "Email", "Approval"]
bookList = [
    ["B-JAK-DEN-2026/09/24", "Doni Simatupang", "2002/03/21", "dontupang@gmail.com", "Approved"],
    ["B-JAK-DEN-2026/09/24", "Jessica Kumala", "1999/07/14", "jessicakumala@yahoo.com", "Denied"]
]



# /===== Formatting Inputs =====/
def inputDate(prompt="Date (YYYY/MM/DD): "):
    while True:
        val = input(prompt).strip()
        try:
            datetime.strptime(val, "%Y/%m/%d")
            return val
        except ValueError:
            print(">> Invalid date. Use format YYYY/MM/DD (e.g. 2026/09/24).")


def inputTime(prompt="Time (HH:MM, 24-hr): "):
    while True:
        val = input(prompt).strip()
        try:
            datetime.strptime(val, "%H:%M")
            return val
        except ValueError:
            print(">> Invalid time. Use 24-hour format HH:MM (e.g. 14:30).")


def inputLocation(prompt="Location (City, Country): "):
    while True:
        val = input(prompt).strip()
        if re.match(r"^[^,]+,\s*[^,]+$", val):
            return val.title()
        print(">> Invalid format. Must be 'City, Country' (e.g. Jakarta, Indonesia).")


def inputPlane(prompt="Plane Name: "):
    while True:
        val = input(prompt).strip()
        if val:
            return val
        print(">> Plane name cannot be empty.")


def inputFlightType(prompt="Flight Type (Economy/Business/First Class): "):
    valid = {"economy", "business", "first class"}
    while True:
        val = input(prompt).strip().lower()
        if val in valid:
            return val.title()
        print(">> Invalid type. Options: Economy, Business, First Class.")


def inputPrice(prompt="Price (RP): "):
    while True:
        val = input(prompt).strip()
        if val.isdigit() and int(val) > 0:
            return int(val)
        print(">> Price must be a whole number greater than 0.")


def inputName(prompt="Full Name: "):
    while True:
        val = input(prompt).strip()
        if len(val) >= 2:
            return val.title()
        print(">> Name must be at least 2 characters long.")


def inputEmail(prompt="Email: "):
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    while True:
        val = input(prompt).strip().lower()
        if re.match(pattern, val):
            return val
        print(">> Invalid email address (e.g. user@example.com).")



# /===== Feature Program =====/
def read():
    check = True
    while check:
        print("""
        Menu:
        1. Display all flights
        2. Display specific flights
        3. Return to main menu

        """)
        selectMenu = input("Select menu number: ")
        if selectMenu == "1":
            print()
            if flightData == None:
                print("\nNo flights available.\n")
            else:
                print(tabulate(flightData, headers=flightHeaders, tablefmt="grid"))
                print()
        elif selectMenu == "2":
            print()
            checkMenu2 = True
            while checkMenu2:
                found = False
                searchID = input("Enter flight ID: ")
                print()
                for i in range(len(flightData)):
                    if flightData[i][0] == searchID:
                        print(tabulate([flightData[i]], headers=flightHeaders, tablefmt="grid"))
                        print()
                        found = True
                        break
                if found:
                    checkMenu2 = False
                else:
                    print("Flight not found\n")
                    tryAgain = input("Would you like to search again? (y/n): ")
                    print()
                    if tryAgain == "n":
                        checkMenu2 = False
        
        elif selectMenu == "3":
            return 0
        else:
            print("\nOption is not valid.\n")


def add():
    while True:
        print("""
        Menu:
        1. Add flight
        2. Return to main menu

        """)
        selectMenu = input("Select menu number: ")

        if selectMenu == "1":
            print()
            while True:
                depDate = inputDate("Departure Date (YYYY/MM/DD): ")
                depHour = inputTime("Departure Time (HH:MM, 24-hour scale): ")
                arrDate = inputDate("Arrival Date (YYYY/MM/DD): ")
                arrHour = inputTime("Arrival Time (HH:MM, 24-hour scale): ")
                depPlace = inputLocation("Flying From (City, Country): ")
                arrPlace = inputLocation("Heading To (City, Country): ")
                plane = inputPlane()
                flightType = inputFlightType()
                price = inputPrice()

                depTime = f"{depDate} {depHour}"
                arrTime = f"{arrDate} {arrHour}"
                depCode = depPlace.split(",")[0].strip().upper()[:3]
                arrCode = arrPlace.split(",")[0].strip().upper()[:3]
                newFlightID = f"{flightType[0].upper()}-{depCode}-{arrCode}-{depDate}"

                isExist = any(f[0] == newFlightID for f in flightData)
                if isExist:
                    print(f"Flight with ID {newFlightID} already exists.\n")
                    tryAgain = input("Would you like to try again? (y/n): ").strip().lower()
                    print()
                    if tryAgain == "y":
                        continue
                    break

                newFlight = [newFlightID, depTime, arrTime, depPlace, arrPlace, plane, flightType, price]
                print()
                print(tabulate([newFlight], headers=flightHeaders, tablefmt="grid"))
                print()

                save = input("Save new flight? (y/n): ").strip().lower()
                if save == "y":
                    print()
                    flightData.append(newFlight)
                    print("Flight has been added.")
                else:
                    print()
                    print("Flight canceled.")
                break
        elif selectMenu == "2":
            print()
            return 0
        else:
            print("\nPilihan menu tidak valid.\n")


def edit():
    check = True
    while check:
        print("""
        Menu:
        1. Edit flight
        2. Return to main menu

        """)
        selectMenu = input("Select menu number: ")
        if selectMenu == "1":
            print()
            tempList = []
            checkMenu1 = True
            while checkMenu1:
                editID = input("Enter flight ID: ")
                print()
                
                isExist = False
                i = 0
                for i in range(len(flightData)):
                    if flightData[i][0] == editID:
                        isExist = True
                        break

                if isExist:
                    print("Current flight data:")
                    print(tabulate([flightData[i]], headers=flightHeaders, tablefmt="grid"))
                    proceedEdit = input("Proceed to edit? (y/n): ")
                    if proceedEdit == "y":
                        print()

                        newData = None
                        print("""
Select which column to edit:
    1. Departure Date & Time
    2. Arrival Date & Time
    3. Flying From
    4. Heading To
    5. Plane
    6. Type
    7. Price

                        """)
                        unvalidColumn = True
                        while unvalidColumn:
                            selectCol = int(input("Select column number: "))
                            if (selectCol >= 1) & (selectCol <= 7):
                                print()
                                print(f"Changing {flightHeaders[selectCol]}")
                                print(f"Current {flightHeaders[selectCol]}: {flightData[i][selectCol]}")
                                newData = input(f"New {flightHeaders[selectCol]}: ")
                                unvalidColumn = False
                                break
                            else:
                                print("\nColumn number is not valid\n")

                        tempList = copy.deepcopy(flightData)
                        tempList[i][selectCol] = newData

                        print()
                        print(tabulate([tempList[i]], headers=flightHeaders, tablefmt="grid"))
                        saveEdit = input("Save edit? (y/n): ")
                        if saveEdit == "n":
                            print()
                            checkMenu1 = False
                            break
                        else:
                            print("\nFlight edit saved.\n")

                        flightData[i][selectCol] = newData
                        print("Flight data edited")
                        print()
                        checkMenu1 = False
                        break

                    elif proceedEdit == "n":
                        print()
                        checkMenu1 = False
                        break   
                        

                else:
                    print("Flight ID not found.")
                    print()
                    tryAgain = input("Would you like to try again? (y/n): ")
                    if tryAgain == "y":
                        print()
                        continue
                    elif tryAgain == "n":
                        print()
                        break


        elif selectMenu == "2":
            print()
            check = False
            return 0
        else:
            print("\nOption is not valid.\n")


def cancel():
    check = True
    while check:
        print("""
        Menu:
        1. Cancel flight
        2. Return to main menu

        """)
        selectMenu = input("Select menu number: ")
        if selectMenu == "1":
            print()
            checkMenu1 = True
            while checkMenu1:

                deleteID = input("Enter flight ID: ")
                isExist = False
                i = 0

                for i in range(len(flightData)):
                    if flightData[i][0] == deleteID:
                        isExist = True
                        targetIdx = i
                        break

                if isExist:
                    print()
                    print("Current flight data:")
                    print(tabulate([flightData[i]], headers=flightHeaders, tablefmt="grid"))
                    print()
                    proceedDelete = input("Proceed to delete? (y/n): ")
                    if proceedDelete == "y":
                        print()
                        flightData.pop(targetIdx)
                        print("Flight has been removed \n")
                        checkMenu1 = False
                        break
                    elif proceedDelete == "n":
                        checkMenu1 = False
                        break
                        
                else:
                    print("\nFlight ID not found.\n")
                    tryAgain = input("Would you like to try again? (y/n): ")
                    if tryAgain == "y":
                        print()
                        continue
                    if tryAgain == "n":
                        print()
                        checkMenu1 = False
                        break


        elif selectMenu == "2":
            check = False
            return 0
        else:
            print("\nOption is not valid.\n")


def booking():
    check = True
    while check:
        print("""
        Menu:
        1. Manage Bookings
        2. Return to main menu

        """)
        selectMenu = input("Select menu number: ")
        if selectMenu == "1":
            print()
            checkMenu1 = True
            while checkMenu1:
                print(tabulate(bookList, headers=bookHeaders, tablefmt="grid"))
                print()
                
                counterApproved = 0
                counterDenied = 0
                counterWaiting = 0
                for i in range(len(bookList)):
                    if bookList[i][4] == "Waiting Approval":
                        counterWaiting += 1
                        waitList.append(i)
                    elif bookList[i][4] == "Approved":
                        counterApproved += 1
                    else:
                        counterDenied += 1 
                
                print(f"""
                Booking Details:
                > {counterApproved} bookings approved.
                > {counterDenied} bookings denied.
                > {counterWaiting} bookings awaiting approval.
                
                Menu:
                1. Approve/Deny Booking
                2. Return to Booking menu

                """)
                
                subMenuCheck = True
                while subMenuCheck:
                    selectSubMenu = input("Select menu number: ")
                    if selectSubMenu == "1":
                        print()
                        if counterWaiting > 0:
                            for i in range(len(waitList)):
                                print(f"Flight ID: {bookList[waitList[i]][0]}")
                                print(f"Full Name: {bookList[waitList[i]][1]}")
                                print(f"Date of Birth: {bookList[waitList[i]][2]}")
                                print(f"Email: {bookList[waitList[i]][3]}")
                                print()
                                approveCheck = input("Verdict (a/d): ")
                                if approveCheck == "a":
                                    bookList[waitList[i]][4] = "Approved"
                                    waitList.pop(i)
                                    subMenuCheck = False
                                    break
                                if approveCheck == "d":
                                    bookList[waitList[i]][4] = "Denied"
                                    waitList.pop(i)
                                    subMenuCheck = False
                                    break
                        else:
                            print("\nThere are no bookings waiting for approval.\n")
                            continue
                    elif selectSubMenu == "2":
                        checkMenu1 = False
                        subMenuCheck = False
                        break
                    else:
                        print("\nOption is not valid.\n")
            

        elif selectMenu == "2":
            check = False
            break
        else:
            print("\nOption is not valid.\n")


def book():
    check = True
    while check:
        print("""
        Menu:
        1. Book flights
        2. View bookings
        3. Return to main menu

        """)
        selectMenu = input("Select menu number: ")
        if selectMenu == "1":
            print()
            tempList = []
            checkMenu1 = True
            while checkMenu1:

                bookID = input("Enter flight ID: ")
                isExist = False
                i = 0

                for i in range(len(flightData)):
                    if flightData[i][0] == bookID:
                        isExist = True
                        break

                if isExist:
                    print()
                    bookNum = int(input("How many bookings will be done? "))
                    counter = 1
                    while bookNum > 0:
                        print()
                        bookName = inputName(f"Enter person {counter}'s full name: ")
                        bookDOB = inputDate(f"Enter person {counter}'s date of birth (YYYY/MM/DD): ")
                        bookEmail = inputEmail(f"Enter person {counter}'s email: ")
                        print()

                        newBook = [bookID, bookName, bookDOB, bookEmail, "Waiting Approval"]
                        tempList.append(newBook)
                        print(tabulate([tempList[counter - 1]], headers=bookHeaders, tablefmt="grid"))
                        print()
                        proceedBook = input("Are you sure to book? (y/n): ")
                        if proceedBook == "y":
                            print()
                            bookList.append(newBook)
                            bookNum = bookNum - 1
                            counter = counter + 1
                        elif proceedBook == "n":
                            print()
                            bookNum = bookNum - 1
                            counter = counter + 1
                            tempList.pop()
                            continue
                    print("\nBooking finished.\n")
                    checkMenu1 = False
                    break
                else:
                    print("\nFlight ID not found.\n")
                    tryAgain = input("Would you like to try again? (y/n): ")
                    if tryAgain == "y":
                        print()
                        continue
                    elif tryAgain == "n":
                        print()
                        checkMenu1 = False
                        break

        elif selectMenu == "2":
            print()
            print(tabulate(bookList, headers=bookHeaders, tablefmt="grid"))
            print()
            continue
        elif selectMenu == "3":
            print()
            check = False
            break
        else:
            print("\nOption is not valid.\n")


def search():
    check = True
    while check:
        print("""
        Menu:
        1. Search flights
        2. Return to main menu

        """)
        selectMenu = input("Select menu number: ")
        if selectMenu == "1":
            tempList = []
            checkMenu1 = True
            while checkMenu1:
                print("""
                Search Schedule Based-On:
                1. Departure Date
                2. Arrival Date
                3. Flying From
                4. Heading To
                5. Plane
                6. Type
                7. Price

                """)
                checkSubMenu = True
                while checkSubMenu:
                    selectSubMenu = int(input("Select menu number: "))
                    if (selectSubMenu >= 1) & (selectSubMenu <= 7):
                        print()
                        print(f"Searching in {flightHeaders[selectSubMenu]}")
                        userSearch = input(f"Search {flightHeaders[selectSubMenu]}: ")

                        isExist = False
                        for i in range(len(flightData)):
                            if flightData[i][selectSubMenu] == userSearch:
                                tempList.append(flightData[i])
                                isExist = True
                                checkSubMenu = False
                                checkMenu1 = False
                    
                        if isExist:
                            print("\nSearch found.\n")
                            print(tabulate(tempList, headers=flightHeaders, tablefmt="grid"))
                            checkSubMenu = False
                            break
                        else:
                            print("\nSearch not found.\n")
                            tryAgain = input("Would you like to try again? (y/n): ")
                            if tryAgain == "y":
                                print()
                                checkSubMenu = False
                                break
                            elif tryAgain == "n":
                                print()
                                checkMenu1 = False
                                break
                    else:
                        print("\nOption is not valid.\n")
        elif selectMenu == "2":
            print()
            check = False
            break
        else:
            print("\nOption is not valid.\n")



# /===== Admin Program =====/
def adminPanel():
    while True:
        for i in bookList:
            if i[4] == "Waiting Approval":
                msg = "! You have bookings waiting approval !"
            else:
                msg = ""

        print(f"""
        =====================================================
         __    _  _______  _______  _______  ___      __   __ 
        |  |  | ||       ||       ||       ||   |    |  | |  |
        |   |_| ||    ___||    ___||    ___||   |    |  |_|  |
        |       ||   | __ |   |___ |   |___ |   |    |       |
        |  _    ||   ||  ||    ___||    ___||   |___ |_     _|
        | | |   ||   |_| ||   |___ |   |    |       |  |   |  
        |_|  |__||_______||_______||___|    |_______|  |___|  
        ======================================================
                           ||ADMIN PANEL||
        
        {msg}
        
        Menu:
        1. View flights
        2. Add flights
        3. Edit flights
        4. Cancel flights
        5. Bookings
        6. Log Out
        7. Exit Program
        
        """)
        check = True
        while check:
            userInput = input("Select menu number: ")
            if userInput == "1":
                check = False
                read()
            elif userInput == "2":
                check = False
                add()
            elif userInput == "3":
                check = False
                edit()
            elif userInput == "4":
                check = False
                cancel()
            elif userInput == "5":
                check = False
                booking()
            elif userInput == "6":
                check = False
                print("Logging out.")
                loginGateway()
            elif userInput == "7":
                check = False
                print("Exiting program.")
                sys.exit()
            else:
                print("Option is not valid.")
        


# /===== User Program =====/
def userPanel():
    while True:
        print(f"""
        =====================================================
         __    _  _______  _______  _______  ___      __   __ 
        |  |  | ||       ||       ||       ||   |    |  | |  |
        |   |_| ||    ___||    ___||    ___||   |    |  |_|  |
        |       ||   | __ |   |___ |   |___ |   |    |       |
        |  _    ||   ||  ||    ___||    ___||   |___ |_     _|
        | | |   ||   |_| ||   |___ |   |    |       |  |   |  
        |_|  |__||_______||_______||___|    |_______|  |___|  
        ======================================================
                 Flight Ticket Management System
        
        Welcome, {loginUsername}!
        
        Menu:
        1. View flights
        2. Search flights
        3. Book flights
        4. Log Out
        5. Exit program
        
        """)
        
        userInput = input("Select menu number: ")
        if userInput == "1":
            read()
        elif userInput == "2":
            search()
        elif userInput == "3":
            book()
        elif userInput == "4":
            print("Logging out.")
            loginGateway()
        elif userInput == "5":
            print("Exiting program.")
            sys.exit()
        else:
            print("Input is not valid !")



# /===== Login =====/
def loginGateway():
    print("""
        =====================================================
         __    _  _______  _______  _______  ___      __   __ 
        |  |  | ||       ||       ||       ||   |    |  | |  |
        |   |_| ||    ___||    ___||    ___||   |    |  |_|  |
        |       ||   | __ |   |___ |   |___ |   |    |       |
        |  _    ||   ||  ||    ___||    ___||   |___ |_     _|
        | | |   ||   |_| ||   |___ |   |    |       |  |   |  
        |_|  |__||_______||_______||___|    |_______|  |___|  
        ======================================================
                 Flight Ticket Management System
        """)
    global loginUsername
    loginUsername = input("Enter username: ")
    loginPassword = pwinput.pwinput(prompt="Enter password: ", mask="*")
    if loginUsername == "admin" and loginPassword == "123":
        adminPanel()
    else:
        userPanel()

if __name__ == "__main__":
    loginGateway()