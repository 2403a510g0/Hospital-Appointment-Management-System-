patients = []


def register_patient(patient_id, name, age, phone):
    patient = {
        "id": patient_id,
        "name": name,
        "age": age,
        "phone": phone
    }

    patients.append(patient)
    print("Patient registered successfully.")

    return patient


def display_patients():
    if not patients:
        print("No patients registered.")
        return

    print("\n--- Patient List ---")

    for patient in patients:
        print("Patient ID:", patient["id"])
        print("Name:", patient["name"])
        print("Age:", patient["age"])
        print("Phone:", patient["phone"])
        print("--------------------")