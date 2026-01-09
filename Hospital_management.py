# ================== HOSPITAL MANAGEMENT SYSTEM ==================

class FileHelper:
    @staticmethod
    def get_next_id(filename):
        try:
            with open(filename, "r") as file:
                lines = file.readlines()
                if not lines:
                    return 1
                last_id = int(lines[-1].split(",")[0])
                return last_id + 1
        except FileNotFoundError:
            return 1


# ------------------ DOCTOR ------------------
class Doctor:
    FILE = "doctor.txt"

    def add_doctor(self):
        doc_id = FileHelper.get_next_id(self.FILE)
        name = input("Enter doctor name: ")
        specialize = input("Enter specialization: ")
        phone = input("Enter phone number: ")

        with open(self.FILE, "a") as file:
            file.write(f"{doc_id},{name},{specialize},{phone}\n")

        print("Doctor added successfully!")

    def view_all(self):
        try:
            with open(self.FILE, "r") as file:
                for line in file:
                    d = line.strip().split(",")
                    print(f"ID:{d[0]} | Name:{d[1]} | Dept:{d[2]} | Phone:{d[3]}")
        except FileNotFoundError:
            print("No doctors found")

    def search_doctor(self):
        key = input("Enter Doctor ID or Name: ").lower()
        try:
            with open(self.FILE, "r") as file:
                for line in file:
                    Id, name, spec, phone = line.strip().split(",")
                    if key == Id or key == name.lower():
                        print(f"\nID:{Id}\nName:{name}\nDept:{spec}\nPhone:{phone}")
                        return
                print("Doctor not found")
        except FileNotFoundError:
            print("No doctors available")


# ------------------ PATIENT ------------------
class Patient:
    FILE = "patient.txt"

    def add_patient(self):
        pid = FileHelper.get_next_id(self.FILE)
        name = input("Enter patient name: ")
        age = input("Enter age: ")
        gender = input("Enter gender (Male/Female): ")
        disease = input("Enter disease: ")
        phone = input("Enter phone number: ")

        with open(self.FILE, "a") as file:
            file.write(f"{pid},{name},{age},{gender},{disease},{phone}\n")

        print("Patient added successfully!")

    def view_all(self):
        try:
            with open(self.FILE, "r") as file:
                for line in file:
                    p = line.strip().split(",")
                    print(f"ID:{p[0]} | Name:{p[1]} | Age:{p[2]} | Gender:{p[3]} | Disease:{p[4]} | Phone:{p[5]}")
        except FileNotFoundError:
            print("No patients found")

    def search_patient(self):
        key = input("Enter Patient ID or Name: ").lower()
        try:
            with open(self.FILE, "r") as file:
                for line in file:
                    p = line.strip().split(",")
                    if key == p[0] or key == p[1].lower():
                        print(f"\nID:{p[0]}\nName:{p[1]}\nAge:{p[2]}\nGender:{p[3]}\nDisease:{p[4]}\nPhone:{p[5]}")
                        return
                print("Patient not found")
        except FileNotFoundError:
            print("No patients available")


# ------------------ APPOINTMENT ------------------
class Appointment:
    FILE = "appointment.txt"

    def add_appointment(self):
        aid = FileHelper.get_next_id(self.FILE)
        pid = input("Enter Patient ID: ")
        did = input("Enter Doctor ID: ")
        date = input("Enter date (DD-MM-YYYY): ")
        time = input("Enter time: ")

        with open(self.FILE, "a") as file:
            file.write(f"{aid},{pid},{did},{date},{time}\n")

        print("Appointment added successfully!")

    def view_all(self):
        try:
            with open(self.FILE, "r") as file:
                for line in file:
                    a = line.strip().split(",")
                    print(f"ID:{a[0]} | Patient:{a[1]} | Doctor:{a[2]} | Date:{a[3]} | Time:{a[4]}")
        except FileNotFoundError:
            print("No appointments found")


# ------------------ MAIN MENU ------------------
def hospital_management():
    while True:
        print("\n=== HOSPITAL MANAGEMENT SYSTEM ===")
        print("1.Add Doctor\n2.View Doctors\n3.Search Doctor")
        print("4.Add Patient\n5.View Patients\n6.Search Patient")
        print("7.Add Appointment\n8.View Appointments\n9.Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            Doctor().add_doctor()
        elif choice == "2":
            Doctor().view_all()
        elif choice == "3":
            Doctor().search_doctor()
        elif choice == "4":
            Patient().add_patient()
        elif choice == "5":
            Patient().view_all()
        elif choice == "6":
            Patient().search_patient()
        elif choice == "7":
            Appointment().add_appointment()
        elif choice == "8":
            Appointment().view_all()
        elif choice == "9":
            print("Thank you for visiting the hospital")
            break
        else:
            print("Invalid choice")


hospital_management()
