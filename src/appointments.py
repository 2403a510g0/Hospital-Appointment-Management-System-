appointments = []


def schedule_appointment(appointment_id, patient_id, doctor_id, date, time):
    appointment = {
        "id": appointment_id,
        "patient_id": patient_id,
        "doctor_id": doctor_id,
        "date": date,
        "time": time,
        "status": "Scheduled"
    }

    appointments.append(appointment)

    print("Appointment scheduled successfully.")
    return appointment


def cancel_appointment(appointment_id):
    for appointment in appointments:
        if appointment["id"] == appointment_id:
            appointment["status"] = "Cancelled"
            print("Appointment cancelled successfully.")
            return

    print("Appointment not found.")


def display_appointments():
    if not appointments:
        print("No appointments found.")
        return

    print("\n--- Appointment List ---")

    for appointment in appointments:
        print("Appointment ID:", appointment["id"])
        print("Patient ID:", appointment["patient_id"])
        print("Doctor ID:", appointment["doctor_id"])
        print("Date:", appointment["date"])
        print("Time:", appointment["time"])
        print("Status:", appointment["status"])
        print("------------------------")