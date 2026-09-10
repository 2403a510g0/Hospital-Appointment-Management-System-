from appointments import appointments


def display_patient_history(patient_id):
    print("\n--- Patient Appointment History ---")

    found = False

    for appointment in appointments:
        if appointment["patient_id"] == patient_id:
            found = True

            print("Appointment ID:", appointment["id"])
            print("Doctor ID:", appointment["doctor_id"])
            print("Date:", appointment["date"])
            print("Time:", appointment["time"])
            print("Status:", appointment["status"])
            print("------------------------")

    if not found:
        print("No appointment history found.")