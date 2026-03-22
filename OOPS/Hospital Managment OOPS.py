class Person:
    def __init__(self, name, age, phone):
        self.name = name
        self.age = age
        self.phone = phone

    def __str__(self):
        return f"Name: {self.name} | Age: {self.age} | Phone: {self.phone}"

    def contact_info(self):
        print(f"{self.name} : {self.phone}")


class Doctor(Person):
    def __init__(self, name, age, phone, specialization, availability=True):
        super().__init__(name, age, phone)
        self.specialization = specialization
        self.availability = availability        # ✅ instance variable

    def set_availability(self, status):
        self.availability = status              # ✅ only this doctor

    def __str__(self):
        base = super().__str__()                # ✅ capture parent string
        return f"{base} | Specialization: {self.specialization} | Available: {self.availability}"


class Patient(Person):
    def __init__(self, name, age, phone, disease):
        super().__init__(name, age, phone)
        self.disease = disease
        self.__medical_record = []

    def add_record(self, note):
        self.__medical_record.append(note)

    @property
    def medical_record(self):                   # ✅ property decorator
        return self.__medical_record

    def __str__(self):
        base = super().__str__()                # ✅ capture parent string
        return f"{base} | Disease: {self.disease}"


class Hospital:
    total_hospitals = 0

    def __init__(self, hospital_name):
        self.name = hospital_name
        self.doctors = []
        self.patients = []                      # ✅ fixed typo
        Hospital.total_hospitals += 1

    def register_doctor(self, doctor):
        self.doctors.append(doctor)

    def register_patient(self, patient):
        self.patients.append(patient)

    def show_doctors(self):
        print(f"\n-- Doctors at {self.name} --")
        for doc in self.doctors:
            print(doc)                          # ✅ print not return

    def show_patients(self):
        print(f"\n-- Patients at {self.name} --")
        for pat in self.patients:
            print(pat)                          # ✅ print not return

    def available_doctors(self):
        print(f"\n-- Available Doctors --")
        for doc in self.doctors:
            if doc.availability == True:        # ✅ check each individually
                print(doc)

    def find_patient(self, name):
        for patient in self.patients:
            if patient.name == name:            # ✅ compare names
                return patient
        print(f"Patient '{name}' not found.")
        return None

    def __str__(self):
        return (f"Hospital : {self.name} | "
                f"Doctors: {len(self.doctors)} | "   # ✅ len() not .count
                f"Patients: {len(self.patients)}")
        
# --- Setup ---
h1 = Hospital("Apollo Hospital")

d1 = Doctor("Dr. Sharma", 45, "9876543210", "Cardiology")
d2 = Doctor("Dr. Mehta", 38, "9123456789", "Neurology")

p1 = Patient("Abhay", 19, "9999999999", "Fever")
p2 = Patient("Yash", 20, "8888888888", "Diabetes")
p3 = Patient("Raj", 25, "7777777777", "Fracture")

# --- Register ---
h1.register_doctor(d1)
h1.register_doctor(d2)
h1.register_patient(p1)
h1.register_patient(p2)
h1.register_patient(p3)

# --- Medical Records ---
p1.add_record("Prescribed paracetamol for 5 days")
p2.add_record("Started insulin therapy")
p2.add_record("Blood sugar levels monitored weekly")
p3.add_record("Plaster applied to left leg")

# --- Availability ---
d2.set_availability(False)

# --- Display ---
print(h1)                    # Hospital __str__
h1.show_doctors()            # all doctors
h1.show_patients()           # all patients
h1.available_doctors()       # only d1 since d2 is unavailable

# --- Search ---
found = h1.find_patient("Abhay")
print(found)                 # Patient __str__

not_found = h1.find_patient("Ronaldo")   # should print not found message

# --- Property ---
print(p2.medical_record)     # getter — returns private list

# --- Contact Info ---
d1.contact_info()
p1.contact_info()

# --- Class Variable ---
h2 = Hospital("Fortis Hospital")
print(Hospital.total_hospitals)   # should print 2