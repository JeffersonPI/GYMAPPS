# GYMAPPS

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![OOP](https://img.shields.io/badge/Concept-OOP-green)
![CLI](https://img.shields.io/badge/Interface-CLI-orange)
![Status](https://img.shields.io/badge/Project-Completed-brightgreen)

A Command Line Interface (CLI) based **Gym Management System** built using **Python** and **Object-Oriented Programming (OOP)** principles.

This project simulates a real-world gym system including membership management, personal trainer booking, schedule validation, and administrative controls.

---

# Key Features

## Member Features
- Secure User Registration & Login (Max 5 attempts)
- Membership Creation & Extension
- Automatic Membership Expiration Calculation
- Daily Check-In (No double check-in)
- Personal Trainer (PT) Booking with Schedule Validation
- FIFO-Based PT Session Usage
- Cancel / Reschedule PT Sessions
- Edit Profile

---

## Admin Features
- View All Users & Membership Details
- Manage Trainers (Add / Edit / Delete)
- View Top PT Member (Based on Usage)
- Protected Main Admin Account

---

# System Design Concept

Instead of using simple counters for PT sessions, the system stores booking data in structured format:

```python
self.pt_bookings = []
```

Each booking contains:
- Trainer Name
- Schedule (datetime object)
- Status ("Booked" / "Used")

### Why This Approach?
- Prevent session mismatches
- Maintain strong data integrity
- Enable FIFO session usage logic
- Avoid duplicate schedule conflicts

---

# Project Structure

```
GYMAPPS/
│── README.md        # Project documentation
│── LICENSE.md       # Project license
│── main.py          # CLI Interface
│── gym_system.py    # Main system controller
│── member.py        # Member entity class
│── trainer.py       # Trainer entity class
```

---

# Validation Rules

## User ID
- 6–20 characters
- Must contain letters & numbers

## Password
- Minimum 8 characters
- Must include:
  - Uppercase letter
  - Lowercase letter
  - Digit
  - Special character

## Login Security
- Maximum 5 login attempts

## PT Booking Rules
- Cannot book past schedules
- Allowed between 06:00 – 22:00
- No schedule conflicts
- FIFO session consumption logic

---

# How to Run

```bash
python main.py
```

---

# System Flow Overview

```
User → Register/Login
      ↓
Membership Validation
      ↓
PT Booking System
      ↓
Schedule Validation
      ↓
Session Usage (FIFO)
      ↓
Admin Monitoring & Reports
```

---

# Technologies Used
- Python 3
- Object-Oriented Programming (OOP)
- Datetime Module
- CLI-based Interaction

---

# Future Improvements
- Data persistence using database (SQLite / MySQL)
- Graphical User Interface (GUI) version
- Web-based deployment (Flask / Django)
- Payment integration simulation
- Reporting & analytics dashboard

---

# Author
Jefferson Iskandar  
Computer Science Student  
Project Type: Academic / Portfolio

---

# License
This project is licensed under the terms described in the LICENSE file.