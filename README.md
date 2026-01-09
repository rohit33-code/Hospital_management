# 🏥 Hospital Management System 

This is a **Python-based Hospital Management System** designed as a **command-line interface (CLI) project**. It allows managing doctors, patients, and appointments in a hospital using simple text files for storage.

---

##  Features

* **Doctor Management:**

  * Add new doctors
  * View all doctors
  * Search doctor by ID or Name

* **Patient Management:**

  * Add new patients
  * View all patients
  * Search patient by ID or Name

* **Appointment Management:**

  * Schedule patient appointments
  * View all appointments

* **File-Based Storage:**

  * Doctors, patients, and appointments are stored in separate `.txt` files



##  Project Structure

```
Hospital-Management-System/
│
├── hospital.py        # Main application script
├── doctor.txt         # Stores doctor information
├── patient.txt        # Stores patient information
├── appointment.txt    # Stores appointments
└── README.md          # Project documentation
```


## 📋 Application Menus

### Main Menu

```
1. Add Doctor
2. View Doctors
3. Search Doctor
4. Add Patient
5. View Patients
6. Search Patient
7. Add Appointment
8. View Appointments
9. Exit
```

### Sample Output

```
ID:1 | Name: Dr. John | Dept: Cardiology | Phone: 1234567890
ID:1 | Name: Alice | Age:30 | Gender: Female | Disease: Flu | Phone:9876543210
ID:1 | Patient:1 | Doctor:1 | Date:12-01-2026 | Time:10:00 AM
```

