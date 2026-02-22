from member import Member
from trainer import Trainer
class GymSystem:
    
    def __init__(self):
        self.users = {}
        self.memberships = {}
        self.trainers = {
            "T001": Trainer("T001", "Andi Pratama", "Strength Training", 150000),
            "T002": Trainer("T002", "Rina Wijaya", "Fat Loss & Cardio", 140000),
            "T003": Trainer("T003", "Kevin Santoso", "Bodybuilding", 170000),
            "T004": Trainer("T004", "Dewi Lestari", "Yoga & Mobility", 130000),
            "T005": Trainer("T005", "Adi Saputra", "Functional Training", 160000),
            "T006": Trainer("T006", "Salsa Putri", "HIIT & Conditioning", 155000),
        }

        self.users["admin01"] = {
            "uid": "admin01",
            "password": "Admin@123",
            "name": "Administrator",
            "role": "admin"
        }
        
    # Validation
    
    def validate_userid(self, uid):
        if len(uid) < 6 or len(uid) > 20:
            return False
        if uid in self.users:
            return False
        
        has_letter = has_digit = False
        
        for char in uid:
            if not (char.isalnum() or char in "._"):
                return False
            if char.isalpha():
                has_letter = True
            if char.isdigit():
                has_digit = True
        
        return has_letter and has_digit
    
    def validate_password(self,pw):
        if len(pw) < 8:
            return False

        
        special = "/.,@#$%"
        up = low = digit = spec = False
        
        for c in pw:
            if c.isupper(): up = True
            if c.islower(): low = True
            if c.isdigit(): digit = True
            if c in special: spec = True 
        
        return up and low and digit and spec
    
    def validate_trainer_id(self, trainer_id):

        if len(trainer_id) < 3:
            return False

        if not trainer_id.isalnum():
            return False

        return True
    
    # Authentication
    
    def register(self):
        print("\n=== REGISTER ===")
          
        while True: 
            uid = input("UserID: ")
            if self.validate_userid(uid):
                break
            print("Invalid or already exist")
            
        while True: 
            pw = input("Password: ")
            if self.validate_password(pw):
                break
            print("Password not valid")
            
        name = input("Name: ")
        
        self.users[uid] = {
            "uid": uid,
            "password": pw,
            "name": name,
            "role": "member"
        }
    
        print("Registrations successful!")
        
    def login(self):
        
        attempts = 0
        
        while attempts < 5:
            uid = input("UserID: ")
            pw = input("Password: ")
        
            if uid not in self.users:
                print("User not found")
                attempts += 1
                continue
        
            if self.users[uid]["password"] != pw:
                attempts += 1
                print(f"Wrong password. Remaining attempts: {5 - attempts}")
                continue
            
            print ("Login successful!")
            return self.users[uid]
        
        print("Too many failed attempts. Account locked temporarily.")
        return None
    
    # Member Action
    
    def create_membership (self, uid):
        if uid in self.memberships:
            print("Membership already exists")
            return
        
        package = input("Choose package (Bulanan/Tahunan): ").lower()
        
        if package not in ["bulanan", "tahunan"]:
            print ("Invalid package")
            return
        
        try: 
            duration = int(input("How many (months/years)?: "))
            if duration <= 0:
                print ("Duration must be positive")
                return
        except ValueError:
            print ("Invalid duration")
            return
        
        self.memberships[uid] = Member(self.users[uid], package, duration)
        print("Membership created!")
    
    def view_membership (self, uid):
        if uid not in self.memberships:
            print("No membership found")
            return
        
        print(self.memberships[uid].info())
        
    
    def extend_membership(self, uid):
        if uid not in self.memberships:
            print("No membership found")
            return
        
        package = input("Extend package (Bulanan/Tahunan): ").lower()
        
        if package not in ["bulanan", "tahunan"]:
            print("Invalid package")
            return
        
        try:
            duration = int(input("How many (months/years)?"))
        except ValueError:
            print("Invalid duration")
            return
        
        
        self.memberships[uid].extend(package, duration)
        
    def check_in(self, uid):
        if uid not in self.memberships:
            print("No membership found")
            return
    
        self.memberships[uid].check_in()
        
    # ===== PT =====


    def rent_pt(self, uid):
        if uid not in self.memberships:
            print("No membership found.")
            return

        member = self.memberships[uid]

        if member.status() == "Expired":
            print("Membership expired.")
            return

        if not self.trainers:
            print("No trainers available.")
            return

        print("\n===== TRAINER LIST =====")
        for trainer in self.trainers.values():
            print(trainer.info())

        trainer_id = input("Choose Trainer ID: ")

        if trainer_id not in self.trainers:
            print("Invalid trainer ID.")
            return

        try:
            sessions = int(input("Number of PT sessions: "))
            if sessions <= 0:
                print("Invalid session amount.")
                return
        except ValueError:
            print("Invalid input.")
            return

        trainer = self.trainers[trainer_id]

        print("\nEnter schedule for each session:")
        date_list = []

        for i in range(sessions):
            date = input(f"Session {i+1} (YYYY-MM-DD HH:MM): ")
            date_list.append(date)

        member.rent_pt_with_schedule(sessions, trainer, date_list)

    def use_pt(self, uid):
        if uid not in self.memberships:
            print("No membership found")
            return

        member = self.memberships[uid]
        
        if member.status() == "Expired":
            print("Membership expired.")
            return
        
        member.use_pt()   

    def cancel_pt(self, uid):
        if uid not in self.memberships:
            print("No membership found")
            return

        self.memberships[uid].cancel_pt()


    def reschedule_pt(self, uid):
        if uid not in self.memberships:
            print("No membership found")
            return

        self.memberships[uid].reschedule_pt()
        
    def edit_profile(self, uid):
        if uid not in self.users:
            print("User not found")
            return

        user = self.users[uid]

        print("\n=== EDIT PROFILE ===")
        print("Press Enter to skip.\n")

        print(f"Current Name: {user['name']}")
        new_name = input("New Name: ")
        if new_name:
            user["name"] = new_name

        new_pw = input("New Password: ")
        if new_pw:
            if self.validate_password(new_pw):
                user["password"] = new_pw
            else:
                print("Invalid password. Not updated")

        print("Profile updated successfully!")
    
    
    # ===== ADMIN =====

    def admin_view_all(self):
        print("\n=== USERS ===")
        for uid, data in self.users.items():
            print(f"{uid} - {data['name']} - {data['role']}")

        print("\n=== MEMBERSHIPS ===")
        for m in self.memberships.values():
            print(m.info())

    def admin_delete_user(self):
        uid = input("UserID to delete: ")

        if uid == "admin01":
            print("Cannot delete main admin")
            return

        if uid in self.users:
            del self.users[uid]
            if uid in self.memberships:
                del self.memberships[uid]
            print("User deleted!")
        else:
            print("User not found")
    
    def admin_view_trainers(self):
        if not self.trainers:
            print("No trainers available")
            return
    
        print("\n=== TRAINER LIST ===")
        for trainer in self.trainers.values():
            print(trainer.info())
    
    def admin_add_trainer(self):

        trainer_id = input("Trainer ID: ").upper()

        if not self.validate_trainer_id(trainer_id):
            print("Invalid Trainer ID format.")
            return

        if trainer_id in self.trainers:
            print("Trainer already exists.")
            return

        name = input("Trainer Name: ")
        specialist = input("Specialist: ")

        try:
            price = int(input("Price per session: "))
            if price <= 0:
                print("Price must be greater than 0.")
                return
        except ValueError:
            print("Invalid price.")
            return

        self.trainers[trainer_id] = Trainer(
            trainer_id, name, specialist, price
        )

        print("Trainer added successfully!")
    
    def admin_manage_trainer(self):

        if not self.trainers:
            print("No trainers available.")
            return

        print("\n=== TRAINER LIST ===")
        for trainer in self.trainers.values():
            print(trainer.info())

        trainer_id = input("Enter Trainer ID to manage: ").upper()

        if trainer_id not in self.trainers:
            print("Trainer not found.")
            return

        trainer = self.trainers[trainer_id]

        print("\n1. Edit Trainer")
        print("2. Delete Trainer")
        choice = input("Choose action: ")

        # ================= EDIT =================
        if choice == "1":

            print("Press Enter to skip.\n")

            new_name = input("New Name: ")
            if new_name:
                trainer.name = new_name

            new_specialist = input("New Specialist: ")
            if new_specialist:
                trainer.specialist = new_specialist

            new_price = input("New Price per session: ")
            if new_price:
                try:
                    new_price = int(new_price)
                    if new_price <= 0:
                        print("Price must be greater than 0.")
                        return
                    trainer.price_per_session = new_price
                except ValueError:
                    print("Invalid price.")
                    return

            print("Trainer updated successfully!")

        # ================= DELETE =================
        elif choice == "2":

            confirm = input("Are you sure you want to delete this trainer? (y/n): ").lower()

            if confirm == "y":
                del self.trainers[trainer_id]
                print("Trainer deleted successfully!")
            else:
                print("Deletion cancelled.")

        else:
            print("Invalid choice.")
        
    def admin_top_pt_member(self):
        if not self.memberships:
            print("No data available")
            return
        
        if all(len(m.pt_history) == 0 for m in self.memberships.values()):
            print("No PT usage yet")
            return

        top_member = None
        max_used = 0

        for m in self.memberships.values():
            used = len(m.pt_history)
            if used > max_used:
                max_used = used
                top_member = m

        if top_member:
            print("\n=== TOP PT MEMBER ===")
            print(top_member.info())
        else:
            print("No PT usage yet")
            
                  
        