# ===================================
# NgeFly: Flight Ticket Management System
# ===================================
# Developed by Reyner Elazaro Tampubolon
# JCDSBSD - 34



# /===== Library Imports & Global Variables=====/
import pwinput
from tabulate import tabulate
loginUsername = None

# /===== Data Model =====/
flightHeaders = ["Flight ID", "Departure Time", "Arrival Time", "Flying From", "Heading To", "Plane", "Flight Type", "Price"]
flightData = [
    ["B-JAK-DEN-2026/09/24", "2026/09/24 07:25", "2026/09/24 11:40", "Jakarta, Indonesia", "Denpasar, Indonesia", "Boeing 747", "Business", 6_500_000],
    ["E-JAK-BAN-2026/09/30", "2026/09/15 09:30", "2026/09/16 11:40", "Jakarta, Indonesia", "Bandung, Indonesia", "Airbus 300", "Economy", 3_000_000]
]

# # "grid", "fancy_grid", "pipe", or "orgtbl" are popular formats
# print(tabulate(data, headers=headers, tablefmt="fancy_grid"))

# /===== Feature Program =====/
def read():
    print(tabulate(flightData, headers=flightHeaders, tablefmt="grid"))
    print()

    print("""
        Menu:
        1. Return to main menu
        2. Exit program
    """)
    selectMenu = input("Select menu number:")
    if selectMenu == "1":
        print("Returning to main menu")
    elif selectMenu == "2":
        return 0

def add():
    newFlightDepDate = input("Departure Date (YYYY/MM/DD): ")
    newFlightDepHour = input("Departure Time (HH:MM, 24-hour scale): ")
    newFlightDepTime = newFlightDepDate + " " + newFlightDepHour
    newFlightArrDate = input("Arrival Date (YYYY/MM/DD): ")
    newFlightArrHour = input("Arrival Time (HH:MM, 24-hour scale): ")
    newFlightArrTime = newFlightArrDate + " " + newFlightArrHour
    newFlightDepPlace = input("Flying From (City, Country): ")
    newFlightArrPlace = input("Heading To (City, Country): ")
    newFlightPlane = input("Plane Name: ")
    newFlightType = input("Flight Type (Economy/Business/First Class): ")
    newFlightPrice = int(input("Price (RP): "))
    newFlightID = newFlightType.upper()[0] + "-" + newFlightDepPlace.upper()[:3] + "-" + newFlightArrPlace.upper()[:3] + "-" + newFlightDepDate

    newFlight = [newFlightID, newFlightDepTime, newFlightArrTime, newFlightDepPlace, newFlightArrPlace, newFlightPlane, newFlightType, newFlightPrice]
    flightData.append(newFlight)
    print("Flight has been added.")
    print()

    print("""
        Menu:
        1. Return to main menu
        2. Exit program
    """)
    selectMenu = input("Select menu number:")
    if selectMenu == "1":
        print("Returning to main menu")
    elif selectMenu == "2":
        return 0

def edit():
    userInput = input("Enter flight ID: ")
    for i in range(len(flightData)):
        if flightData[i][0] == userInput:
            print(tabulate([flightData[i]], headers=flightHeaders, tablefmt="grid"))
            print()
            print(f"Editing row index {i}:")
            editFlightDepDate = input("Departure Date (YYYY/MM/DD): ")
            editFlightDepHour = input("Departure Time (HH:MM, 24-hour scale): ")
            editFlightDepTime = editFlightDepDate + " " + editFlightDepHour
            editFlightArrDate = input("Arrival Date (YYYY/MM/DD): ")
            editFlightArrHour = input("Arrival Time (HH:MM, 24-hour scale): ")
            editFlightArrTime = editFlightArrDate + " " + editFlightArrHour
            editFlightDepPlace = input("Flying From (City, Country): ")
            editFlightArrPlace = input("Heading To (City, Country): ")
            editFlightPlane = input("Plane Name: ")
            editFlightType = input("Flight Type (Economy/Business/First Class): ")
            editFlightPrice = int(input("Price (RP): "))
            editFlightID = editFlightType.upper()[0] + "-" + editFlightDepPlace.upper()[:3] + "-" + editFlightArrPlace.upper()[:3] + "-" + editFlightDepDate

            flightData[i] = [editFlightID, editFlightDepTime, editFlightArrTime, editFlightDepPlace, editFlightArrPlace, editFlightPlane, editFlightType, editFlightPrice]
            print("Flight data altered.")
            print(tabulate([flightData[i]], headers=flightHeaders, tablefmt="grid"))
            print()

            print("""
            Menu:
            1. Return to main menu
            2. Exit program
            """)
            selectMenu = input("Select menu number:")
            if selectMenu == "1":
                print("Returning to main menu")
            elif selectMenu == "2":
                return 0
        else:
            print("Data not found.")


def cancel():
    pass

def booking():
    pass

def book():
    pass

def search():
    userDepDate = input("Departure Date (YYYY/MM/DD): ")
    userDepHour = input("Departure Time (HH:MM, 24-hour scale): ")
    userDepTime = userDepDate + " " + userDepHour
    userArrPlace = input("Heading to: ")
    userFlightType = input("Preferred flight type: ")


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
        6. Exit Program
        
        """)
        userInput = input("Select menu number: ")
        if userInput == "1":
            read()
        elif userInput == "2":
            add()
        elif userInput == "3":
            edit()
        elif userInput == "4":
            cancel()
        elif userInput == "5":
            booking()
        elif userInput == "6":
            print("Exiting program.")



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
        4. Exit program
        
        """)
        
        userInput = input("Select menu number: ")
        if userInput == "1":
            read()
        elif userInput == "2":
            search()
        elif userInput == "3":
            book()
        elif userInput == "4":
            print("Exiting program.")
            return 0
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
    if loginUsername == "Admin01" and loginPassword == "Admin123":
        adminPanel()
    else:
        userPanel()

if __name__ == "__main__":
    loginGateway()