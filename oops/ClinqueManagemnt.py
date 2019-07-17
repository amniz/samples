# @author:Muhammed Nisamudheen
# @version:3.7
# @purpose:programme is used to manage a list of Doctors associated with the Clinique. This also manages the list of patients who use the
# clinique
import datetime


# class for creating doctor object
class Doctor:

    # initializing the objects of the doctor class
    def __init__(self, doctor_name=str(), doctor_id=int(), doctor_specialization=str()):
        self.doctor_name = doctor_name  # object variables are initialized
        self.doctor_id = doctor_id
        self.doctor_specialization = doctor_specialization
        # self.bcount = 0

    # checking whether doctor is available
    def is_doctor_available(self, dates, doctor_id):
        print(dates.isoweekday())  # using datetime weekday function to check the day
        if dates.isoweekday() in [5, 6]:  # checking whether it is a sunday or saturday
            return "not availabe doctor is off"
        else:
            doctor_status = []  # list to store the tuple of doctor and doctor time schedule
            date_doctor_id = (dates, doctor_id)  # storing the doctor id and doctor timings
            doctor_status.append[date_doctor_id]  # appending the data of the tuple to the list
            if doctor_status.count(date_doctor_id) < 5:
                return "available"
            else:
                return "not available"


# class to create patient
class Patient:

    # initializing the data of the patient
    def __init__(self, patient_name=str(), patient_id=int(), patient_phone_number=int(), doctor_id=int()):
        self.patient_name = patient_name  # patient attributes are initialized
        self.patient_id = patient_id
        self.patient_phone_number = patient_phone_number
        self.patient_doctor.doctor_id = doctor_id


# class for storing the Clinique data
class Clinique():
    #  initilazing the clinique data
    def __init__(self):
        self.doctors = []  # list for adding the doctors objects
        self.patients = []  # list for storing the patient objects

    def add_doctor(self):
        self.doctors.append(Doctor(doctor_name=input("enter doctor_name"), doctor_id=int(input("enter doctor id")),
                                   doctor_specialization=input("enter doctor specilaizaton")))


    # method  for getting the doctor detail
    def doctor_details(self, doctor_name=str(), doctor_id=int(), doctor_specialization=str(), dates=datetime.datetime):

        try:
            doctor_id = int(doctor_id)
        except:
            print("doctor id should be an integer")

        for i in range(len(self.doctors)):  # traversing through all the doctor objects

            if doctor_id == int() and doctor_specialization == str() and dates == datetime.datetime:  # getting towards the correct attribute

                if self.doctors[i].doctor_name == doctor_name:  # checking  if the passed name and attribute doctor name matches
                    print("doctor name is", self.doctors[i].doctor_name)  # printing the doctor details
                    print("doctor id is", self.doctors[i].doctor_id)
                    print("doctor specializtion is", self.doctors[i].doctor_specialization)
                    return
            elif doctor_name == str() and doctor_specialization == str() and dates == datetime.datetime:

                if self.doctors[i].doctor_id == doctor_id:
                    # print("inssdd")
                    print("doctor name is", self.doctors[i].doctor_name)
                    print("doctor id is", self.doctors[i].doctor_id)
                    print("doctor specializtion is", self.doctors[i].doctor_specialization)
                    return
            elif doctor_name == str() and doctor_id == int() and dates == datetime.datetime:
                if self.doctors[i].doctor_specialization == doctor_specialization:
                    print("doctor name is", self.doctors[i].doctor_name)
                    print("doctor id is", self.doctors[i].doctor_id)
                    print("doctor specialization is", self.doctors[i].doctor_specialization)
                    return
            elif doctor_name == str() and doctor_id == int() and doctor_specialization == str():
                # checking the availability of doctor
                check_doctor_availability = self.is_doctor_available(dates, input("enter the doctor name"))
                print(check_doctor_availability)

    # getting the patient details
    def patient_details(self, patient_name=str(), patient_id=int(), patient_phone_number=int()):
        for i in range(len(self.patients)):  # checking for each patient element
            if patient_id == int() and patient_phone_number == int():  # checking for the particular attribute
                if self.patients[
                    i].patient_name == patient_name:  # checking for the match of the patient name and name passed as formal parameter
                    print("patient name", self.patients[i].patient_name)  # printing the necessary details
                    print("patient id", self.patients[i].patient_id)
                    print("phone number", self.patients[i].patient_phone_number)
                    self.doctor_details(doctor_id=self.patients[i].patient_doctor.doctor_id)
                    return
            elif patient_name == str() and patient_phone_number == int():
                if self.patients[i].patient_id == patient_id:
                    print("patient name", self.patients[i].patient_name)
                    print("patient id", self.patients[i].patient_id)
                    print("phone number", self.patients[i].patient_phone_number)
                    self.doctor_details(doctor_id=self.patients[i].patient_doctor.doctor_id)
                    return
            elif patient_name == str() and patient_id == int():
                if self.patients[i].patient_phone_number == patient_phone_number:
                    print("patient name", self.patients[i].patient_name)
                    print("patient id", self.patients[i].patient_id)
                    print("phone number", self.patients[i].patient_phone_number)
                    self.patients[i].patient_doctor.doctor_id
                    return

    # method for searching doctor
    def search_doctor(self):
        print("enter how do you want to search the doctor")
        try:  # getting the search input from the user
            user_option = int(input("1->doctor_name\n2->doctor_id\n3->doctor specialization\n4->doctor availability"))
        except Exception as e:
            print("check the format", e)
        if user_option == 1:
            doctorname = input("enter the doctor name")
            self.doctor_details(doctor_name=doctorname)
        elif user_option == 2:
            doctorid = int(input("enter the doctor id"))
            self.doctor_details(doctor_id=doctorid)
        elif user_option == 3:
            doctorspecialization = input("enter the doctors specilaization")
            self.doctor_details(doctor_specialization=doctorspecialization)
        elif user_option == 4:  # checking whether the doctor is available in the particular day
            year, month, day, hour, minute = 2019, int(input("month")), int(input("day")), int(input("hour")), 0
            date_time_object = datetime.datetime(year, month, day, hour, minute)

            self.doctor_details(dates=date_time_object)
        else:
            print("sorry,please enter a valid option")

    # method to add patients to the clinique
    def add_patient(self):
        self.patients.append(
            Patient(patient_name=input("enter patient name"), patient_id=input("patient id"),
                    patient_phone_number=input("enter patient phno"),
                    doctor_id=input("enter doctor_id")))

    # method for searching patient
    def search_patient(self):
        user_option = int(input("enter how do you want to search the patient\n1->name\n2->pateint id\n3->phoneno"))
        if user_option == 1:  # getting the desired option from the user
            pn = input("enter the patient name")
            self.patient_details(patient_name=pn)
        elif user_option == 2:
            pi = int(input("enter the patient_id"))
            self.patient_details(patient_id=pi)
        elif user_option == 3:
            ph = int(input("enter the phone number"))
            self.patient_details(phno=ph)


clinique = Clinique()
number_of_doctors = int(input("enter the number of doctors"))
for i in range(number_of_doctors):
    clinique.add_doctor()

clinique.search_doctor()
