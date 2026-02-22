# GYMAPPS
A Command Line Interface (CLI) based Gym Management System built using Python and Object-Oriented Programming (OOP).

This application simulates a real-world gym management system including membership handling, personal trainer booking, schedule validation, and administrative control.

1. Features
2. 
Member Features:
-User Registration & Login (max 5 attempts)
-Membership Creation & Extension
-Automatic Expiration Calculation
-Daily Check-In (no double check-in)
-PT Booking with Schedule Validation
-FIFO-based PT Usage Logic
-Cancel / Reschedule PT
-Edit Profile

Admin Features:
-View All Users & Memberships
-Manage Trainers (Add / Edit / Delete)
-View Top PT Member (based on usage)
-Protected Main Admin Account

2. System Design
Instead of using simple counters for PT sessions,
this system stores bookings as structured data:

self.pt_bookings = []

Each booking contains:
-Trainer name
-Schedule (datetime)
-Status ("Booked" / "Used")

Why this approach?
-Prevent session mismatch
-Maintain data integrity
-Support FIFO session usage
-Prevent duplicate schedule conflicts

4. Architecture
/GymApps
├── README.md                                     # Project documentation
├── LICENSE.md                                    # Project license
├── main.py                                       # User Interface (CLI interaction)
├── gym_system.py                                 # Main Controller
├── member.py                                     # Membership entity
└── trainer.py                                    # Trainer entity

5. Validation Rules
UserID: 6–20 characters (must contain letters & numbers)

Password: minimum 8 characters (uppercase, lowercase, digit, special char)

Max 5 login attempts

PT schedule:
-Cannot be in the past
-Must be between 06:00–22:00
-No schedule conflicts
-FIFO session usage

