doctors = []


def add_doctor(doctor_id, name, specialization):
    doctor = {
        "id": doctor_id,
        "name": name,
        "specialization": specialization
    }

    doctors.append(doctor)
    print("Doctor added successfully.")
    return doctor


def display_doctors():
    if not doctors:
        print("No doctors available.")
        return

    print("\n--- Doctor List ---")

    for doctor in doctors:
        print("ID:", doctor["id"])
        print("Name:", doctor["name"])
        print("Specialization:", doctor["specialization"])
        print("--------------------")