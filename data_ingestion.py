
import pandas as pd
import firebase_admin
from firebase_admin import credentials, db
from datetime import datetime
import requests

# Read local Excel file
df = pd.read_excel('sample_data.xlsx')

# Clean and transform data
df = df.where(pd.notnull(df), None)
df['MobileNo'] = df['MobileNo'].astype('Int64').astype(str)
date_columns = ['LeadDate', 'StartDate', 'EndDate', 'FollowupDate']
for col in date_columns:
    df[col] = df[col].apply(lambda x: x.isoformat() if pd.notnull(x) else None)

# Convert comma-separated strings to lists
list_columns = ['Documents', 'Tasks', 'AssignIssueStage']
for col in list_columns:
    df[col] = df[col].apply(lambda x: x.split(', ') if pd.notnull(x) else [])

# Initialize Firebase
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://kustodian-assessment-default-rtdb.firebaseio.com/'
})

# Upload to Realtime Database
ref = db.reference('clients')
for _, row in df.iterrows():
    client_data = {
        'Name': row['Name'],
        'MobileNo': row['MobileNo'],
        'CaseLocation': row['CaseLocation'],
        'ProductSubCategory': row['ProductSubCategory'],
        'Status': row['Status'],
        'Challenges': row['Challenges'],
        'ClientAge': int(row['ClientAge']),
        'LeadDate': row['LeadDate'],
        'TimeSpent': float(row['TimeSpent']),
        'ClaimAmount': float(row['ClaimAmount']),
        'Documents': row['Documents'],
        'Priority': row['Priority'],
        'Email': row['Email'],
        # Add all other fields similarly
    }
    # ref.child(row['ClientId']).set(client_data)
    try:
        ref.child(str(row['ClientId'])).set(client_data)
    except requests.exceptions.HTTPError as e:
        print(f"Failed to upload data for ClientId {row['ClientId']}: {e}")

print("Data uploaded successfully!")