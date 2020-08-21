import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate("c:/Users/pilot/OneDrive/Escritorio/Easy2English Python/easy2english-df1eb-firebase-adminsdk-4wbw8-b5435a814f.json")
app = firebase_admin.initialize_app(cred)
db = firestore.client()

class Database_Methods:
    def __init__(self):pass
    def log_in(self, id, password):
        auth_ref = db.collection("teachers").document(id)
        doc = auth_ref.get()
        try:
            self.dict = doc.to_dict()
            pwd = self.dict["password"]
            self.classes_id = self.dict["classes"]
        except Exception:
            return "Id does not exist"
        if password != pwd :
            return "Password is incorrect"
        else : return True

database = Database_Methods()