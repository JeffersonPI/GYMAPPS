from gym_system import GymSystem

def main():
    system = GymSystem()

    while True:
        print("\n=== GYM MANAGEMENT SYSTEM ===")
        print("1. Register")
        print("2. Login")
        print("3. Exit")

        choice = input("Choose: ")

        if choice == "1":
            system.register()

        elif choice == "2":
            user = system.login()

            if user:

                if user["role"] == "admin":
                    while True:
                        print("\n=== ADMIN MENU ===")
                        print("1. View All Data")
                        print("2. Delete User")
                        print("3. Top PT Member")
                        print("4. View Trainers")
                        print("5. Add Trainer")
                        print("6. Manage Trainer")
                        print("7. Logout")

                        admin_choice = input("Choose: ")

                        if admin_choice == "1":
                            system.admin_view_all()
                        elif admin_choice == "2":
                            system.admin_delete_user()
                        elif admin_choice == "3":
                            system.admin_top_pt_member()
                        elif admin_choice == '4':
                            system.admin_view_trainers()
                        elif admin_choice == '5':
                            system.admin_add_trainer()
                        elif admin_choice == '6':
                            system.admin_manage_trainer()
                        elif admin_choice == "7":
                            break
                        else: 
                            print("Invalide choice.")

                else:
                    while True:
                        print("\n=== MEMBER MENU ===")
                        print("1. Create Membership")
                        print("2. View Membership")
                        print("3. Extend Membership")
                        print("4. Rent PT")
                        print("5. Use PT Session")
                        print("6. Cancel PT")
                        print("7. Reschedule PT")
                        print("8. Edit Profile")
                        print("9. Check In")
                        print("10. Logout")
                        

                        menu = input("Choose: ")

                        if menu == "1":
                            system.create_membership(user["uid"])
                        elif menu == "2":
                            system.view_membership(user["uid"])
                        elif menu == "3":
                            system.extend_membership(user["uid"])
                        elif menu == "4":
                            system.rent_pt(user["uid"])
                        elif menu == "5":
                            system.use_pt(user["uid"])
                        elif menu == "6":
                            system.cancel_pt(user["uid"])
                        elif menu == "7":
                            system.reschedule_pt(user["uid"])
                        elif menu == "8":
                            system.edit_profile(user["uid"])
                        elif menu == "9":
                            system.check_in(user["uid"])
                        elif menu == "10":
                            break
                        else: 
                            print("Invalid choice.")
        elif choice == "3":
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()