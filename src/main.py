from patients import register_patient, display_patients
from doctors import add_doctor, display_doctors
from appointments import (
    schedule_appointment,
    cancel_appointment,
    display_appointments
)
from history import display_patient_history


def main():

    while True:

        print("\n========================================")
        print("   HOSPITAL APPOINTMENT MANAGEMENT - APPOINTMENTS")
        print("========================================")
        print("1. Register Patient")
        print("2. View Patients")
        print("3. Add Doctor")
        print("4. View Doctors")
        print("5. Schedule Appointment")
        print("6. View Appointments")
        print("7. Cancel Appointment")
        print("8. View Patient Appointment History")
        print("9. Exit")
        print("========================================")

        choice = input("Enter your choice: ")

        # Patient Registration
        if choice == "1":

            patient_id = input("Enter patient ID: ")
            name = input("Enter patient name: ")

            try:
                age = int(input("Enter patient age: "))
            except ValueError:
                print("Age must be a number.")
                continue

            phone = input("Enter phone number: ")

            register_patient(
                patient_id,
                name,
                age,
                phone
            )

        # Display Patients
        elif choice == "2":

            display_patients()

        # Add Doctor
        elif choice == "3":

            doctor_id = input("Enter doctor ID: ")
            name = input("Enter doctor name: ")
            specialization = input("Enter specialization: ")

            add_doctor(
                doctor_id,
                name,
                specialization
            )

        # Display Doctors
        elif choice == "4":

            display_doctors()

        # Schedule Appointment
        elif choice == "5":

            appointment_id = input("Enter appointment ID: ")
            patient_id = input("Enter patient ID: ")
            doctor_id = input("Enter doctor ID: ")
            date = input("Enter appointment date: ")
            time = input("Enter appointment time: ")

            schedule_appointment(
                appointment_id,
                patient_id,
                doctor_id,
                date,
                time
            )

        # Display Appointments
        elif choice == "6":

            display_appointments()

        # Cancel Appointment
        elif choice == "7":

            appointment_id = input("Enter appointment ID: ")

            cancel_appointment(appointment_id)

        # Patient History
        elif choice == "8":

            patient_id = input("Enter patient ID: ")

            display_patient_history(patient_id)

        # Exit
        elif choice == "9":

            print("Thank you for using the Hospital Appointment Management System.")
            break

        else:

            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()