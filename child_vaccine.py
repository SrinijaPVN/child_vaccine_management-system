class Child:
    def __init__(self, name, dob):
        self.name = name
        self.dob = dob
        self.vaccinations = {}

    def add_vaccination(self, vaccine_name, date):
        self.vaccinations[vaccine_name] = date

    def view_vaccinations(self):
        print(f"Vaccination records for {self.name}:")
        for vaccine, date in self.vaccinations.items():
            print(f"Vaccine: {vaccine} | Date: {date}")

    def set_appointment_reminder(self, vaccine_name, appointment_date):
        print(f"Reminder: {vaccine_name} vaccine appointment is on {appointment_date}")

if __name__ == "__main__":
    # Taking dynamic input for child's details
    name = input("Enter child's name: ")
    dob = input("Enter child's date of birth (yyyy-mm-dd): ")

    child = Child(name, dob)

    # Adding vaccination records dynamically
    while True:
        vaccine_name = input("Enter vaccine name (or type 'exit' to stop): ")
        if vaccine_name.lower() == 'exit':
            break
        date = input("Enter vaccination date (yyyy-mm-dd): ")
        child.add_vaccination(vaccine_name, date)

    # Viewing vaccination records
    child.view_vaccinations()

    # Setting an appointment reminder
    reminder_vaccine = input("Enter vaccine name for reminder: ")
    appointment_date = input("Enter appointment date (yyyy-mm-dd): ")
    child.set_appointment_reminder(reminder_vaccine, appointment_date)
