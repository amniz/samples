from dateutil import parser
import datetime


class Doctor:
    # count=0
    # def __init__(self):
    #
    #     if self.count==0:
    #         self.doc=[]
    #         self.count+=1
    #     else:
    #         self.doc.append(self.add())
    # def __init__(self,dname=input("enter dname"),did=input("enter doctor id"),spec=input("enter doctor specilaizaton")):
    #     self.dname=dname
    #     self.did=did
    #     self.specilaization=spec
    # self.availability=avail   avail=parser.parse(input("Enter the date in the following format (Aug 28 1999 3:00AM)"))

    # def __iter__(self):
    #     return Doctor
    # def __next__(self):
    #     retur
    # def getdoctordetails(did):
    #     for i in Doctor:
    #         if i.did==did:
    #             return dname,did,specilaization,availability
    # def __iter__(self):
    #     return Doctor

    def __init__(self, dname=str(), did=int(), spec=str()):
        self.dname = dname
        self.did = did
        self.spec = spec
        self.bcount = 0

    def isavailable(self, d, did):
        print(d.isoweekday())
        if d.isoweekday() in [5, 6]:
            return "not availabe doctor is off"
        else:
            l = []
            m = (d, did)
            l.append[m]
            if l.count(m) < 5:
                return "available"
            else:
                return "not available"


class Patient:
    # def __init__(self,pname=input("enter patient name"),pid=input("patient id"),pnumber=input("enter patient phno"),did=input("enter did")):
    #     self.pname=pname
    #     self.pid=pid
    #     self.pnumber=pnumber
    #     self.Doc=did
    h = Doctor()

    def __init__(self, pname=str(), pid=int(), pnumber=int(), did=int()):
        self.pname = pname
        self.pid = pid
        self.pnumber = pnumber
        self.h.did = did


class Hospital():
    def __init__(self):
        self.doctors = []  # list for adding the doctors objects
        self.Patients = [] # list for storing the patient objects

    def addDoctor(self):
        self.doctors.append(Doctor(dname=input("enter dname"), did=int(input("enter doctor id")),
                                   spec=input("enter doctor specilaizaton")))

    # def isavailable(self,d,did):
    #     print(d.isoweekday())
    #     if d.isoweekday() in [5,6]:
    #         return "not availabe doctor is off"
    #     else:
    #         l=[]
    #         m=(d,did)
    #         l.append[m]
    #         if l.count(m)<5:
    #             return "available"
    #         else:
    #             return "not available"

    def doctordetails(self, dname=str(), didi=int(), dspec=str(), d=datetime.datetime):
        # print("inside")
        # print(didi)
        # print(len(self.doctors))
        didi = int(didi)
        for i in range(len(self.doctors)):
            # print("inside for")
            if didi == int() and dspec == str() and d == datetime.datetime:
                # print("inside if")
                if self.doctors[i].dname == dname:
                    print("doctor name is", self.doctors[i].dname)
                    print("doctor id is", self.doctors[i].did)
                    print("doctor specializtion is", self.doctors[i].spec)
                    return

            elif dname == str() and dspec == str() and d == datetime.datetime:
                # print("inside elif")
                # print(type(self.doctors[i].did))
                # print("didi",type(didi))

                if self.doctors[i].did == didi:
                    # print("inssdd")
                    print("doctor name is", self.doctors[i].dname)
                    print("doctor id is", self.doctors[i].did)
                    print("doctor specializtion is", self.doctors[i].spec)
                    return
            elif dname == str() and didi == int() and d == datetime.datetime:
                if self.doctors[i].dspec == dspec:
                    print("doctor name is", self.doctors[i].dname)
                    print("doctor id is", self.doctors[i].did)
                    print("doctor specializtion is", self.doctors[i].spec)
                    return
            elif dname == str() and didi == int() and dspec == str():

                l = self.isavailable(d, input("enter the doctor name"))
                print(l)

    def patientdetails(self, pname=str(), pid=int(), phno=int()):
        for i in range(len(self.Patients)):
            if pid == int() and phno == int():
                if self.Patients[i].pname == pname:
                    print("patient name", self.Patients[i].pname)
                    print("patient id", self.Patients[i].pid)
                    print("phone number", self.Patients[i].pnumber)
                    self.doctordetails(didi=self.Patients[i].h.did)
                    return
            elif pname == str() and phno == int():
                if self.Patients[i].pid == pid:
                    print("patient name", self.Patients[i].pname)
                    print("patient id", self.Patients[i].pid)
                    print("phone number", self.Patients[i].pnumber)
                    self.doctordetails(didi=self.Patients[i].h.did)
                    return
            elif pname == str() and pid == int():
                if self.Patients[i].pnumber == phno:
                    print("patient name", self.Patients[i].pname)
                    print("patient id", self.Patients[i].pid)
                    print("phone number", self.Patients[i].pnumber)
                    self.Patients[i].h.did
                    return

    def searchdoc(self):
        print("enter how do you want to search the doctor")
        sr = int(input("1->doctorname\n2->doctorid\n3->doctor specilization\n4->doctor availability"))
        if sr == 1:
            docn = input("enter the doctor name")
            self.doctordetails(dname=docn)
        elif sr == 2:
            docid = int(input("enter the doctor id"))
            self.doctordetails(didi=docid)
        elif sr == 3:
            docsp = input("enter the doctors specilaization")
            self.doctordetails(dspec=docsp)
        elif sr == 4:
            y, m, d, h, mi = 2019, int(input("month")), int(input("day")), int(input("hour")), int(input("min"))
            s = datetime.datetime(y, m, d, h, mi)
            # print(avail)
            # print(type(avail))
            self.doctordetails(d=s)
        else:
            print("sorry,please enter a valid option")

    def addpatient(self):
        self.Patients.append(
            Patient(pname=input("enter patient name"), pid=input("patient id"), pnumber=input("enter patient phno"),
                    did=input("enter did")))

    def searchpat(self):
        ps = int(input("enter how do you want to search the patient\n1->name\n2->pateint id\n3->phoneno"))
        if ps == 1:
            pn = input("enter the patient name")
            self.patientdetails(pname=pn)
        elif ps == 2:
            pi = int(input("enter the pid"))
            self.patientdetails(pid=pi)
        elif ps == 3:
            ph = int(input("enter the phone number"))
            self.patientdetails(phno=ph)
    # def details(self,f):
    #     print("details of the patient")
    #     print(self.pname)
    #     print(self.pid)
    #     print(self.pnumber)
    #     if
    #     print(self.Doc.dname)
    #     print(self.Doc.did)
    #     print(self.Doc.specilaization)
    #     print(self.Doc.availability)

    # def search(self,pname,pid,pnumber):
    #     if self.Patients.pname==pname and self.Patients.pid==pid and self.Patients.pnumber==pnumber:
    #         self.Patients


h = Hospital()
n = int(input("enter the number of doctpors"))
for i in range(n):
    h.addDoctor()
# h.addpatient()
# h.addpatient()
h.searchdoc()
