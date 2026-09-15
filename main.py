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



# /===== Data Models =====/
# Flight Data:
flightHeaders = ["Flight ID", "Departure Time", "Arrival Time", "Flying From", "Heading To", "Plane", "Flight Type", "Price"]
flightData = [
    ["B-JAK-DEN-2026/09/24", "2026/09/24 07:25", "2026/09/24 11:40", "Jakarta, Indonesia", "Denpasar, Indonesia", "Boeing 747", "Business", 6_500_000],
    ["E-JAK-BAN-2026/09/30", "2026/09/15 09:30", "2026/09/16 11:40", "Jakarta, Indonesia", "Bandung, Indonesia", "Airbus 300", "Economy", 3_000_000]
]

# Booking Data:
bookHeaders = ["Booked Flight", "Full Name", "Date of Birth", "Email", "Approval"]
bookList = []



# /===== Feature Program =====/
def isValid(prompt, validator, error):
    while True:
        val = input(prompt).strip()
        try:
            if validator(val):
                return val
        except (ValueError, IndexError):
            pass
        print(f">> Invalid format. {error}")


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
            if flightData == None:
                print("No flights available.")
            else:
                print(tabulate(flightData, headers=flightHeaders, tablefmt="grid"))
                print()
        elif selectMenu == "2":
            checkMenu2 = True
            while checkMenu2:
                found = False
                searchID = input("Enter flight ID: ")
                for i in range(len(flightData)):
                    if flightData[i][0] == searchID:
                        print(tabulate([flightData[i]], headers=flightHeaders, tablefmt="grid"))
                        print()
                        found = True
                        break
                if found:
                    checkMenu2 = False
                else:
                    print("Flight not found")
                    tryAgain = input("Would you like to search again? (y/n): ")
                    if tryAgain == "n":
                        checkMenu2 = False
        
        elif selectMenu == "3":
            return 0
        else:
            print("Option is not valid.")


def add():
    while True:
        print("""
        Menu:
        1. Add flight
        2. Return to main menu
        """)
        selectMenu = input("Select menu number: ").strip()

        if selectMenu == "1":
            while True:
                depDate = isValid(
                    "Departure Date (YYYY/MM/DD): ",
                    lambda x: datetime.strptime(x, "%Y/%m/%d"),
                    "Use the format YYYY/MM/DD (Example: 2026/09/24)",
                )
                depHour = isValid(
                    "Departure Time (HH:MM, 24-hour scale): ",
                    lambda x: datetime.strptime(x, "%H:%M"),
                    "Use the 24-hour format of HH:MM (Example: 21:30)",
                )
                arrDate = isValid(
                    "Arrival Date (YYYY/MM/DD): ",
                    lambda x: datetime.strptime(x, "%Y/%m/%d"),
                    "Use the format YYYY/MM/DD (Example: 2026/09/24)",
                )
                arrHour = isValid(
                    "Arrival Time (HH:MM, 24-hour scale): ",
                    lambda x: datetime.strptime(x, "%H:%M"),
                    "Use the 24-hour format HH:MM (Example: 21:30)",
                )
                depPlace = isValid(
                    "Flying From (City, Country): ",
                    lambda x: re.match(r"^[^,]+,\s*[^,]+$", x),
                    "Use the format 'City, Country' (contoh: Berlin, Germany)",
                )
                arrPlace = isValid(
                    "Heading To (City, Country): ",
                    lambda x: re.match(r"^[^,]+,\s*[^,]+$", x),
                    "Use the format 'City, Country' (contoh: Berlin, Germany)",
                )
                plane = isValid(
                    "Plane Name: ",
                    lambda x: len(x) > 0,
                    "Name of the plane can't be empty",
                )
                valid_types = {"economy", "business", "first class"}
                f_type_raw = isValid(
                    "Flight Type (Economy/Business/First Class): ",
                    lambda x: x.lower() in valid_types,
                    "Types are only: Economy, Business, First Class",
                )
                f_type = f_type_raw.title()
                price_str = isValid(
                    "Price (RP): ",
                    lambda x: int(x) > 0,
                    "Price has to be an integer of more than 0",
                )
                price = int(price_str)

                depTime = f"{depDate} {depHour}"
                arrTime = f"{arrDate} {arrHour}"

                depCode = depPlace.split(",")[0].strip().upper()[:3]
                arrCode = arrPlace.split(",")[0].strip().upper()[:3]
                newFlightID = f"{f_type[0].upper()}-{depCode}-{arrCode}-{depDate}"

                isExist = any(f[0] == newFlightID for f in flightData)
                if isExist:
                    print(f"\nFlight dengan ID {newFlightID} sudah ada.")
                    tryAgain = input("Would you like to try again? (y/n): ").strip().lower()
                    if tryAgain == "y":
                        continue
                    break

                newFlight = [newFlightID, depTime, arrTime, depPlace, arrPlace, plane, f_type, price]
                print()
                print(tabulate([newFlight], headers=flightHeaders, tablefmt="grid"))
                print()

                save = input("Save new flight? (y/n): ").strip().lower()
                if save == "y":
                    flightData.append(newFlight)
                    print("Flight has been added.")
                else:
                    print("Flight canceled.")
                break

        elif selectMenu == "2":
            return 0
        else:
            print("Pilihan menu tidak valid.")


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
            tempList = []
            checkMenu1 = True
            while checkMenu1:

                editID = input("Enter flight ID: ")

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
                                print(f"Changing {flightHeaders[selectCol]}")
                                print(f"Current {flightHeaders[selectCol]}: {flightData[i][selectCol]}")
                                newData = input(f"New {flightHeaders[selectCol]}: ")
                                unvalidColumn = False
                                break
                            else:
                                print("Column number is not valid")

                        tempList = copy.deepcopy(flightData)
                        tempList[i][selectCol] = newData

                        print()
                        print(tabulate([tempList[i]], headers=flightHeaders, tablefmt="grid"))
                        saveEdit = input("Save edit? (y/n): ")
                        if saveEdit == "n":
                            checkMenu1 = False
                            break

                        flightData[i][selectCol] = newData
                        print("Flight data edited")
                        print()
                        checkMenu1 = False
                        break

                    elif proceedEdit == "n":
                        checkMenu1 = False
                        break   
                        

                else:
                    print("Flight ID not found.")
                    tryAgain = input("Would you like to try again? (y/n): ")
                    if tryAgain == "y":
                        continue
                    elif tryAgain == "n":
                        break


        elif selectMenu == "2":
            check = False
            return 0
        else:
            print("Option is not valid.")


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
            checkMenu1 = True
            while checkMenu1:

                deleteID = input("Enter flight ID: ")
                isExist = False
                i = 0

                for i in range(len(flightData)):
                    if flightData[i][0] == deleteID:
                        isExist = True
                        break

                if isExist:
                    print("Current flight data:")
                    print(tabulate([flightData[i]], headers=flightHeaders, tablefmt="grid"))
                    proceedDelete = input("Proceed to delete? (y/n): ")
                    if proceedDelete == "y":
                        clearRow = 0
                        while clearRow == 0:
                            for i in range(len(flightData)):
                                if flightData[i][0] == deleteID:
                                    clearRow = i
                                    flightData.pop(clearRow)
                                    print("Flight has been removed.")
                                    checkMenu1 = False
                                    break
                    elif proceedDelete == "n":
                        checkMenu1 = False
                        break
                        
                else:
                    print("Flight ID not found.")
                    tryAgain = input("Would you like to try again? (y/n): ")
                    if tryAgain == "y":
                        continue
                    if tryAgain == "n":
                        checkMenu1 = False
                        break


        elif selectMenu == "2":
            check = False
            return 0
        else:
            print("Option is not valid.")


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
            checkMenu1 = True
            while checkMenu1:
                print(tabulate(bookList, headers=bookHeaders, tablefmt="grid"))
                print()
                
                counterApproved = 0
                counterDenied = 0
                counterWaiting = 0
                waitList = []
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
                        for i in range(len(waitList)):
                            print(f"Flight ID: {bookList[waitList[i]][0]}")
                            print(f"Full Name: {bookList[waitList[i]][1]}")
                            print(f"Full Name: {bookList[waitList[i]][2]}")
                            print(f"Full Name: {bookList[waitList[i]][3]}")
                            print()
                            approveCheck = input("Verdict (a/d): ")
                            if approveCheck == "a":
                                bookList[waitList[i]][4] = "Approved"
                                subMenuCheck = False
                                break
                            if approveCheck == "b":
                                bookList[waitList[i]][4] == "Denied"
                                subMenuCheck = False
                                break
                    elif selectSubMenu == "2":
                        checkMenu1 = False
                        subMenuCheck = False
                        break
                    else:
                        print("Option is not valid.")
            

        elif selectMenu == "2":
            check = False
            break
        else:
            print("Option is not valid.")



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
                    bookNum = int(input("How many bookings will be done? "))
                    counter = 1
                    while bookNum > 0:
                        bookName = input(f"Enter person {counter}'s full name: ")
                        bookDOB = input(f"Enter person {counter}'s date of birth (YYYY/MM/DD): ")
                        bookEmail = input(f"Enter person {counter}'s email: ")
                        print()

                        newBook = [bookID, bookName, bookDOB, bookEmail, "Waiting Approval"]
                        tempList.append(newBook)
                        print(tabulate(tempList, headers=bookHeaders, tablefmt="grid"))
                        proceedBook = input("Are you sure to book? (y/n): ")
                        if proceedBook == "y":
                            bookList.append(newBook)
                            bookNum = bookNum - 1
                            counter = counter + 1
                        elif proceedBook == "n":
                            bookNum = bookNum - 1
                            continue
                    print("Booking finished.")
                    checkMenu1 = False
                    break
                else:
                    print("Flight ID not found.")
                    tryAgain = input("Would you like to try again? (y/n): ")
                    if tryAgain == "y":
                        continue
                    elif tryAgain == "n":
                        checkMenu1 = False
                        break

        elif selectMenu == "2":
            print(tabulate(bookList, headers=bookHeaders, tablefmt="grid"))
            continue
        elif selectMenu == "3":
            check = False
            break
        else:
            print("Option is not valid.")

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
                7. Price (Special)

                """)
                checkSubMenu = True
                while checkSubMenu:
                    selectSubMenu = int(input("Select menu number: "))
                    if (selectSubMenu >= 1) & (selectSubMenu <= 7):
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
                            print("Search found.")
                            print()
                            print(tabulate(tempList, headers=flightHeaders, tablefmt="grid"))
                            checkSubMenu = False
                            break
                        else:
                            print("Search not found.")
                            tryAgain = input("Would you like to try again? (y/n): ")
                            if tryAgain == "y":
                                checkSubMenu = False
                                break
                            elif tryAgain == "n":
                                checkMenu1 = False
                                break
                    else:
                        print("Option is not valid.")
        elif selectMenu == "2":
            check = False
            break
        else:
            print("Option is not valid.")



# /===== Main Program =====/

def adminPanel():
    while True:
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
                           ||ADMIN PANEL||
        
        ! You have [n] bookings awaiting approval !
        
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