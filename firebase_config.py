import os
import firebase_admin
from firebase_admin import credentials, firestore

# Load the private key from the environment variables
private_key = os.getenv('FIREBASE_PRIVATE_KEY').replace('\\n', '\n')

# Build the Firebase credentials object from environment variables
cred = credentials.Certificate({
    "type": os.getenv('FIREBASE_TYPE'),
    "project_id": os.getenv('FIREBASE_PROJECT_ID'),
    "private_key_id": os.getenv('FIREBASE_PRIVATE_KEY_ID'),
    "private_key": private_key,
    "client_email": os.getenv('FIREBASE_CLIENT_EMAIL'),
    "client_id": os.getenv('FIREBASE_CLIENT_ID'),
    "auth_uri": os.getenv('FIREBASE_AUTH_URI'),
    "token_uri": os.getenv('FIREBASE_TOKEN_URI'),
    "auth_provider_x509_cert_url": os.getenv('FIREBASE_AUTH_PROVIDER_X509_CERT_URL'),
    "client_x509_cert_url": os.getenv('FIREBASE_CLIENT_X509_CERT_URL')
})

# Initialize Firebase app with the credentials
if not firebase_admin._apps:
    firebase_admin.initialize_app(cred)

# Initialize Firestore
db = firestore.client()

# Function to log anomalies to Firebase
def log_anomaly(details):
    try:
        db.collection('anomalies').add({
            'anomaly_type': details['anomaly_type'],
            'timestamp': details['timestamp'],
            'confidence': details['confidence'],
            'info': details['info']
        })
        print("Anomaly logged successfully.")
    except Exception as e:
        print(f"Error logging anomaly: {e}")
