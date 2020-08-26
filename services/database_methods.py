import firebase_admin
from firebase_admin import credentials, firestore
import socket
import datetime
from tkinter import messagebox

cred = credentials.Certificate("c:/Users/pilot/OneDrive/Escritorio/Easy2English Python/easy2english-df1eb-firebase-adminsdk-4wbw8-b5435a814f.json")
app = firebase_admin.initialize_app(cred)
db = firestore.client()

def test_connection():
    try:
        socket.create_connection(("Google.com", 80))
        return True
    except OSError:
        return False

class Database_Methods:
    def __init__(self):
        self.today = str(datetime.date.today())

    def log_in(self, id, password):
        auth_ref = db.collection("teachers").document(id)
        doc = auth_ref.get()
        try:
            dict = doc.to_dict()
            pwd = dict["password"]
            self.classes_id = dict["classes"]
        except Exception:
            return "Id does not exist"
        if password != pwd :
            return "Password is incorrect"
        else : return True

    def fetch_clases(self):
        if test_connection():
            #List of dictionaries, each dictionary represents a class and containes 3 fields: ID, level, schedule
            self.classes = []
            for c in self.classes_id:
                class_ref = db.collection("classes").document(c)
                doc = class_ref.get()
                try:
                    dict = doc.to_dict()
                    cls = {
                        "id":c,
                        "level":dict["level"],
                        "schedule":dict["schedule"]
                           }
                    self.classes.append(cls)
                except Exception:
                    print("Couldn't fetch classes for firestore")
            return self.classes
        else: messagebox.showerror(title="Easy2English", message="Please connect to the internet")

    def fetch_students_info(self, id):
        if test_connection():
            #List of  dictionaries, each dictionary represents a student and containes 3 fields: ID, name, surname
            self.students = []
            #Getting the field from the class document which contains all the students_id from a particular class
            class_ref = db.collection("classes").document(id)
            class_doc = class_ref.get()
            class_dict = class_doc.to_dict()

            self.students_id  = class_dict["students"]

            for s in self.students_id:
                #Getting the document from the student
                student_ref = db.collection("students").document(s)
                student_doc = student_ref.get()
                student_dict = student_doc.to_dict()

                student_assistance_ref = db.collection("students").document(s).collection("assistance").document(self.today)
                student_assistance_doc = student_assistance_ref.get()
                student_assistance_dict = student_assistance_doc.to_dict()
                value = True
                if student_assistance_dict:
                    value = student_assistance_dict["value"]

                student = {
                    "surname":student_dict["surname"],
                    "name":student_dict["name"],
                    "id":s,
                    "value":value,
                }
                #Adding the student locally
                self.students.append(student)

            return self.students
        else:messagebox.showerror(title="Easy2English", message="Please connect to the internet")

    def upload_students_assistance(self, students_assistance_dictionary):
        if test_connection():
            students_id = students_assistance_dictionary.keys()
            for student in students_id:
                assistance_ref = db.collection("students").document(student).collection("assistance").document(self.today)
                assistance_map = {
                    "timestamp":self.today,
                    "value":students_assistance_dictionary[str(student)]
                }
                assistance_ref.set(assistance_map)
            messagebox.showinfo(title="Assistance", message=f"Assistance succesfuly uploaded for {datetime.date.today()}")
        else:messagebox.showerror(title="Easy2English", message="PLease connect to the internet")

    def upload_homework(self, class_id, text):
        if test_connection():
            homework_ref = db.collection("classes").document(class_id).collection("homework").document(str(datetime.datetime.now()))
            homework_ref.set({
                "text":text,
                "timestamp":str(datetime.datetime.now())
            })
        else: messagebox.showerror(title="Easy2English", message="Please connect to the internet")

    def fetch_student_exam(self, student_id, exam_number):
        if test_connection():
            student_exam_ref = db.collection("students").document(student_id).collection("exams").document(exam_number)
            student_exam_doc = student_exam_ref.get()
            student_exam_dict = student_exam_doc.to_dict()
            first_exam = {
               "reading":None,
               "writing":None,
               "listening":None,
               "speaking":None
            }
            if student_exam_dict:
               first_exam["reading"] = student_exam_dict["reading"],
               first_exam["writing"] = student_exam_dict["writing"],
               first_exam["listening"] = student_exam_dict["listening"],
               first_exam["speaking"] = student_exam_dict["speaking"]
            return student_exam_dict
        else: messagebox.showerror(title="Easy2English", message="Please connect to the internet")

    def upload_students_exam(self, student_id, exam_number, marks_dictionary):
        if test_connection():
            student_exam_ref = db.collection("students").document(student_id).collection("exams").document(exam_number)
            student_exam_ref.set(marks_dictionary)
        else:messagebox.showerror(title="Easy2English", message="Please connect to the internet")

    def get_classes(self):
        if test_connection():
            return self.classes
        else: messagebox.showerror(title="Easy2English", message="Please connect to the internet")
    def get_students(self):
        if test_connection():
            return self.students
        else: messagebox.showerror(title="Easy2English", message="Please connect to the internet")

database = Database_Methods()