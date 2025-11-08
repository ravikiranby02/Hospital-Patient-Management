from datetime import datetime

class Doctor:
    def  __init__(self,doctor_id,name,specialty):
        self.doctor_id = doctor_id
        self.name = name
        self.specialty = specialty
        self.schedule = []

    def view_schedule(self):
        if not self.schedule:
           print(f"Dr. {self.name} has no appointments scheduled.")
        else:
            print(f"Schedule for Dr. {self.name}:")
            for date_time in self.schedule:
                print(f" - {date_time}")
           

    def is_available(self,date_time):
        return date_time not in self.schedule

class Patient:
    def __init__(self,patient_id,name,ailment):
        self.patient_id = patient_id
        self.name = name
        self.ailment = ailment

    def view_appointments(self):
        print(f"Patient {self.name} can view appointments through Hospital system.")
        


class Appointment:
    def __init__(self,appointment_id,doctor,patient,date_time):
        self.appointment_id = appointment_id
        self.doctor = doctor
        self.patient = patient
        self.date_time = date_time

    def view_details(self):
        print(f"Appointment ID: {self.appointment_id}")
        print(f"Doctor: Dr.{self.doctor.name} ({self.doctor.specialty})")
        print(f"Patient: {self.patient.name} (Ailment: {self.patient.ailment})")
        print(f"Date & Time: {self.date_time}")
        

class Hospital:
    def __init__(self):
        self.doctors = {}
        self.patients = {}
        self.appointments = {}

    def add_doctor(self,doctor_id,name,specialty):
        self.doctors[doctor_id] = Doctor(doctor_id,name,specialty)
        print(f"Doctor {name} added successfully")

    def add_patient(self,patient_id,name,ailment):
        self.patients[patient_id] = Patient(patient_id,name,ailment)
        print(f"Patient {name} added successfully")

    def book_appointment(self,appointment_id,doctor_id,patient_id,date_time):
        if doctor_id not in self.doctors:
            print("Doctor not found")
            return

        if patient_id not in self.patients:
            print("Patient not found")
            return
        
        doctor = self.doctors[doctor_id]
        patient = self.patients[patient_id]

        if date_time in doctor.schedule:
            print(f"Doctor {doctor.name} already has an appointment at {date_time}.")
            return
        
        appointment = Appointment(appointment_id,doctor,patient,date_time)
        self.appointments[appointment_id] = appointment
        doctor.schedule.append(date_time)
        print(f"Appointment booked: Dr. {doctor.name} with {patient.name} on {date_time}.")

    def view_doctors(self):
        if not self.doctors:
            print("No doctors registered.")
        else:
            print("Registered Doctors:")
            for doc in self.doctors.values():
                print(f"ID: {doc.doctor_id}, Name: Dr.{doc.name}, Specialty: {doc.specialty}")

    def view_patients(self):
        if not self.patients:
            print("No patients registered.")
        else:
            print("Registered Patients:")
            for pat in self.patients.values():
                print(f"ID: {pat.patient_id}, Name: {pat.name}, Ailment: {pat.ailment}")

    def view_appointment(self):
        if not self.appointments:
            print("No appointments scheduled.")
        else:
            print("All Appointments:")
            for app in self.appointments.values():
                print(f"ID: {app.appointment_id}, Doctor: {app.doctor.name},"f"Patient: {app.patient.name}, Date: {app.date_time}")

    def cancel_appointment(self,appointment_id):
        if appointment_id not in self.appointments:
            print("Appointmnet not found.")
            return
        

        appointment = self.appointments.pop(appointment_id)
        doctor = appointment.doctor

        if appointment.date_time in doctor.schedule:
            doctor.schedule.remove(appointment.date_time)

    def check_doctor_availability(self,doctor_id,date_time,verbose=True):
        if doctor_id not in self.doctors:
            if doctor_id not in self.doctors:
                if verbose:
                    print("Doctor not found.")
                return False
        
        doctor = self.doctors[doctor_id]
        available = doctor.is_available(date_time)

        if verbose:
            print(f"Doctor {doctor.name} is {'available' if available else 'not available'} at {date_time}.")
    

def menu():
        print("\n === Hospital Management System ===")
        print("1. Add Doctor")
        print("2. Add Patient")
        print("3. Book Appointment")
        print("4. View Doctors")
        print("5. View Patients")
        print("6. View Appointments")
        print("7. Cancel Appointment")
        print("8. Check Doctor Availability")
        print("9. Exit")
hospital = Hospital()

while True:
    menu()
        
    choice = int(input("Enter your choice (1-9): "))

    if choice == 1:
        doctor_id = input("Enter Doctor ID: ")
        name = input("Enter Doctor Name: ")
        specialty = input("Enter Specialty: ")
        hospital.add_doctor(doctor_id,name,specialty)

    elif choice == 2:
        patient_id = input("Enter Patient ID: ")
        name = input("Enter Patient Name: ")
        ailment = input("Enter Ailment: ")
        hospital.add_patient(patient_id,name,ailment)

    elif choice == 3:
        appointment_id = input("Enter Appointment ID: ")
        doctor_id = input("Enter Doctor ID: ")
        patient_id = input("Enter Patient ID: ")
        date_str = input("Enter Date & Time (YYYY-MM-DD HH:MM): ")
        try:
            date_time = datetime.strptime(date_str, "%Y-%m-%d %H:%M")
            hospital.book_appointment(appointment_id,doctor_id,patient_id,date_time)
        except ValueError:
            print(" Invalid date format. Use YYYY-MM-DD HH:MM")

    elif choice == 4:
        hospital.view_doctors()

    elif choice == 5:
        hospital.view_patients()

    elif choice ==6:
        hospital.view_appointment()

    elif choice == 7:
        appointment_id = input("Enter Appointment ID to cancle: ")
        hospital.cancel_appointment(appointment_id)

    elif choice == 8:
        doctor_id = input("Enter Doctor ID: ")
        date_str = input("Enter Date & Time (YYYY-MM-DD HH:MM): ")
        try:
            date_time = datetime.strptime(date_str, "%Y-%m-%d %H:%M")
            hospital.check_doctor_availability(doctor_id,date_time)
        except ValueError:
            print(" Invalid date format. Use YYYY-MM-DD HH:MM")

    elif choice ==9:
        print(" Exiting the system. Goodbye!")
        break

    else:
        print(" Invalid choice! Please try again")