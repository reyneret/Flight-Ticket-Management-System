# ===================================
# NgeFly: Flight Ticket Management System
# ===================================
# Developed by Reyner Elazaro Tampubolon
# JCDSBSD - 34


# /************************************/

# /===== Library Imports =====/
import pwinput

# /===== Data Model =====/
# Basic Info, Departure Time, Arrival Time, Departure Place, Arrival Place, Plane, Flight Type, Price
flightSchedule = [
    ["Business Flight: Jakarta - Denpasar", " 24 September 2026 07:25", "24 September 2026 11:40", "Jakarta", "Denpasar", "Boeing 747", "Business", 6_500_000]
]


# /===== Feature Program =====/
def read():
    """Function for read the data
    """
    return

def create():
    """Function for create the data
    """
    return

def update():
    """Function for update the data
    """
    return

def delete():
    """Function for delete the data
    """
    return

def adminPanel():
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
    inputUser = input("Select menu number: ")

# /===== Main Program =====/
# Create your main program here
def main():
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

    input_user = input("Select menu number: ")
    if input_user == "1":
        read()
    elif input_user == "2":
        create()
    elif input_user == "3":
        update()
    elif input_user == "4":
        delete()
    else:
        print("Input is not valid !")


if __name__ == "__main__":
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
    
        Login
        """)
    loginUsername = input("Enter username: ")
    loginPassword = pwinput.pwinput(prompt="Enter password: ", mask="*")
    if loginUsername == "Admin01" and loginPassword == "Admin123":
        adminPanel()
    else:
        main()