import firebase_admin
from firebase_admin import credentials, firestore

# Initialize Firebase
cred = credentials.Certificate('path_to_your_firebase_adminsdk.json')
firebase_admin.initialize_app(cred)
db = firestore.client()

def log_anomaly(details):
    db.collection('anomalies').add({
        'anomaly_type': details['anomaly_type'],
        'timestamp': details['timestamp'],
        'confidence': details['confidence'],
        'info': details['info']
    })
