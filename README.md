## Python CRUD Application for Flight Ticket Management System (NgeFly)

A comprehensive Python CLI application for managing flight schedules and passenger bookings with Create, Read, Update, and Delete (CRUD) operations.

## Business Understanding

This project caters to airline operations and travel agencies by providing a terminal-based solution for managing flight schedules. Efficient flight and booking management ensures accurate itinerary tracking, avoids schedule conflicts, and standardizes booking validation.

**Benefits:**

* Improved schedule accuracy: Real-time flight tracking reduces scheduling errors and provides clear itinerary visibility.
* Enhanced booking fulfillment: Structured booking collection and administrative review ensure smooth passenger processing.
* Role-based workflow: Clear distinction between administrative controls and customer self-service actions.
* Formatted data visualization: Tabular terminal outputs powered by `tabulate` simplify record inspection.

**Target Users:**

This application is designed for flight operations officers and airline administrative staff to manage flight inventory and ticket approvals, as well as customers looking to browse schedules, search flights, and reserve seats.

## Features

* **Create:**
    * Add new flight schedules with automatic unique Flight ID generation based on cabin class, origin, destination, and departure date (e.g., `B-JAK-DEN-2026/09/24`).
    * Implement strict input validation for dates (`YYYY/MM/DD`), 24-hour departure/arrival times (`HH:MM`), locations (`City, Country`), flight cabin classes, and positive integer pricing.
    * Prevent duplicate flight records before appending them to the database.
    * Allow passengers to create ticket reservations with full name, date of birth, and email.
* **Read:**
    * Display all available flights in structured ASCII tables.
    * Retrieve specific flights by unique Flight ID.
    * Search flights dynamically across specific attributes (departure date, arrival date, origin, destination, aircraft model, flight class, or price).
    * View passenger booking records and tracking statuses.
* **Update:**
    * Modify existing flight attributes including schedule times, routes, aircraft model, cabin type, or ticket price.
    * Provide a deep-copied preview of changes with explicit confirmation before saving updates.
    * Review customer bookings with administrative approval and rejection controls.
* **Delete:**
    * Cancel and remove scheduled flights by Flight ID with confirmation prompts.
* **Authentication & Access Control:**
    * Gateway login supporting masked password entry via `pwinput`.
    * Role separation directing `admin` to the administrative control suite and all other users to the passenger booking interface.

## Installation

1. **Prerequisites:**
    * Python version 3.7 or later
    * Additional dependencies:
        * `pip install tabulate`
        * `pip install pwinput`

2. **Installation:**
    ```bash
    git clone [https://github.com/reyneret/Flight-Ticket-Management-System.git](https://github.com/reyneret/Flight-Ticket-Management-System.git)
    cd Flight-Ticket-Management-System
    pip install tabulate pwinput
    ```

## Usage

1. **Run the application:**
    ```bash
    python main.py
    ```

2. **Authentication:**
    * **Admin Access:** Login with username `admin` and password `123` to access flight scheduling, modification, cancellation, and booking moderation.
    * **Passenger Access:** Enter any user credentials to browse flights, perform multi-attribute searches, and book tickets.

3. **CRUD Operations:**
    * **Create:** Add new flight itineraries (Admin) or reserve flight seats (User).
    * **Read:** View complete flight tables, look up schedules by Flight ID, or search by route/date/type.
    * **Update:** Edit flight details or process reservation approvals (`Approved` / `Denied`).
    * **Delete:** Cancel scheduled flights from the system.

## Data Model

This project utilizes in-memory nested list structures to store flight and reservation data during runtime.

* **Flight Data (`flightData`):**
    * `Flight ID` (String, Unique): Auto-generated unique identifier (e.g., `B-JAK-DEN-2026/09/24`).
    * `Departure Time` (String): Scheduled departure date and time (`YYYY/MM/DD HH:MM`).
    * `Arrival Time` (String): Scheduled arrival date and time (`YYYY/MM/DD HH:MM`).
    * `Flying From` (String): Origin location formatted as `City, Country`.
    * `Heading To` (String): Destination location formatted as `City, Country`.
    * `Plane` (String): Aircraft model name.
    * `Flight Type` (String): Cabin class category (`Economy`, `Business`, or `First Class`).
    * `Price` (Integer): Ticket price in Indonesian Rupiah (IDR).

* **Booking Data (`bookList`):**
    * `Booked Flight` (String): Flight ID associated with the reservation.
    * `Full Name` (String): Passenger's full name.
    * `Date of Birth` (String): Passenger's date of birth (`YYYY/MM/DD`).
    * `Email` (String): Contact email address.
    * `Approval` (String): Reservation status (`Waiting Approval`, `Approved`, or `Denied`).