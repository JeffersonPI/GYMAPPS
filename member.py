from datetime import datetime, timedelta

class Member:
    def __init__(self, user, package, duration):
        self.user = user
        self.package = package.lower()
        self.join_date = datetime.now()
        self.duration = duration
        self.checkin_history = []
        
        if self.package == "bulanan":
            days = 30 * duration
            self.price = 300000 * duration
        elif self.package == "tahunan":
            days = 365 * duration
            self.price = 3000000 * duration
        else:
            raise ValueError("Invalid package")
        
        self.expired = self.join_date + timedelta(days=days)
        self.total_payment = self.price
        
        #PT System
        self.pt_bookings = []
        self.pt_price = 150000
        self.pt_history = []
        
        
    def status (self):
        return "Expired" if datetime.now() > self.expired else "Active"
    
    def extend (self, package, duration):
        package = package.lower()
        
        if package == "bulanan":
            days = 30 * duration 
            price = 300000 * duration
        elif package == "tahunan":
            days = 365 * duration
            price = 3000000 * duration
        else: 
            print ("invalid package")
            return
    
        if datetime.now() > self.expired: 
            self.expired = datetime.now() + timedelta(days=days)
        else: 
            self.expired += timedelta(days=days)
        
        self.total_payment += price
        print("Membership extended successfully")
    
    def check_in(self):
        if self.status() == "Expired":
            print("Membership expired. Cannot check in.")
            return
        
        now = datetime.now()
        today_str = now.strftime("%Y-%m-%d")
        
        #Gak boleh double check in
        for check in self.checkin_history:
            if check.strftime("%Y-%m-%d") == today_str:
                print("Already checked in today.")
                return
        
        self.checkin_history.append(now)
        print(f"Check-in successful at {now.strftime('%Y-%m-%d %H:%M')}")
    #PT System
            
    def use_pt(self):

        if self.status() == "Expired":
            print("Membership expired.")
            return

        # cari session paling awal
        available_sessions = [
            b for b in self.pt_bookings if b["status"] == "Booked"
        ]

        if not available_sessions:
            print("No PT sessions available.")
            return

        # ambil yang paling dekat
        session = sorted(
            available_sessions,
            key=lambda x: x["schedule"]
        )[0]

        session["status"] = "Used"

        self.pt_history.append({
            "trainer": session["trainer"],
            "used_at": datetime.now()
        })

        print("\nPT session used!")
        print(f"Trainer : {session['trainer']}")
        print(f"Scheduled: {session['schedule'].strftime('%Y-%m-%d %H:%M')}")
        
    def cancel_pt(self):

        booked_sessions = [
            b for b in self.pt_bookings if b["status"] == "Booked"
        ]

        if not booked_sessions:
            print("No PT schedule found")
            return

        print("\nYour PT Schedules:")
        for i, booking in enumerate(booked_sessions, 1):
            print(f"{i}. {booking['trainer']} - "
                f"{booking['schedule'].strftime('%Y-%m-%d %H:%M')}")

        try:
            choice = int(input("Choose schedule to cancel: "))
            if 1 <= choice <= len(booked_sessions):
                session = booked_sessions[choice - 1]
                self.pt_bookings.remove(session)
                print("Schedule cancelled successfully!")
            else:
                print("Invalid choice")
        except ValueError:
            print("Invalid input")
            
    def reschedule_pt(self):

        booked_sessions = [
            b for b in self.pt_bookings if b["status"] == "Booked"
        ]

        if not booked_sessions:
            print("No PT schedule found")
            return

        print("\nYour PT Schedules:")
        for i, booking in enumerate(booked_sessions, 1):
            print(f"{i}. {booking['trainer']} - "
                f"{booking['schedule'].strftime('%Y-%m-%d %H:%M')}")

        try:
            choice = int(input("Choose schedule to reschedule: "))
            if not (1 <= choice <= len(booked_sessions)):
                print("Invalid choice")
                return
        except ValueError:
            print("Invalid input")
            return

        new_date = input("Enter new schedule (YYYY-MM-DD HH:MM): ")

        try:
            new_time = datetime.strptime(new_date, "%Y-%m-%d %H:%M")
        except ValueError:
            print("Invalid format")
            return

        if new_time < datetime.now():
            print("Cannot reschedule to past")
            return

        if not (6 <= new_time.hour < 22):
            print("Gym operational hours: 06:00 - 22:00")
            return

        # check conflict
        for booking in self.pt_bookings:
            if booking["schedule"] == new_time:
                print("Schedule conflict!")
                return

        booked_sessions[choice - 1]["schedule"] = new_time
        print("Schedule updated successfully!")
        
    def rent_pt_with_schedule(self, sessions, trainer, date_list):

        if self.status() == "Expired":
            print("Membership expired. Cannot book PT")
            return
        
        if len(date_list) != sessions:
            print("Schedule count does not match session count.")
            return

        total_cost = sessions * trainer.price_per_session
        temp_schedules = []

        for date_str in date_list:

            try:
                schedule_time = datetime.strptime(date_str, "%Y-%m-%d %H:%M")
            except ValueError:
                print(f"Invalid format: {date_str}")
                return

            if schedule_time < datetime.now():
                print("Cannot schedule in the past")
                return

            if not (6 <= schedule_time.hour < 22):
                print("Gym operational hours: 06:00 - 22:00")
                return
            
            for booking in self.pt_bookings:
                if booking["schedule"] == schedule_time:
                    print("Schedule conflict detected")
                    return

            # Cek duplicate dalam input
            if schedule_time in temp_schedules:
                print("Duplicate schedule in input.")
                return

            temp_schedules.append(schedule_time)

        # PT Save
        for sched in temp_schedules:
            self.pt_bookings.append({
            "trainer": trainer.name,
            "schedule": sched,
            "status": "Booked"
            })

        self.total_payment += total_cost

        print("\nPT successfully booked!")
        print(f"Trainer : {trainer.name}")
        print(f"Sessions : {sessions}")
        print(f"Total    : Rp {total_cost}")
        print("Schedules:")
        for sched in temp_schedules:
            print(f"- {sched.strftime('%Y-%m-%d %H:%M')}")
    
    def info(self):
        booked = [
            b for b in self.pt_bookings if b["status"] == "Booked"
        ]

        if booked:
            schedules = "\n              ".join(
                f"{b['trainer']} - "
                f"{b['schedule'].strftime('%Y-%m-%d %H:%M')}"
                for b in booked
            )
        else:
            schedules = "No schedule"

        return f"""
Name        : {self.user['name']}
UserID      : {self.user['uid']}
Package     : {self.package}
Duration    : {self.duration}
Expired     : {self.expired.strftime('%Y-%m-%d')}
Status      : {self.status()}
PT Sessions : {len(booked)}
PT Used     : {len(self.pt_history)}
Schedules   : {schedules}
Total Paid  : Rp {self.total_payment}
"""