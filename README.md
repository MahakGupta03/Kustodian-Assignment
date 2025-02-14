# Kustodian Assignment
## Screenshots
![Screenshot 2025-02-14 235048](https://github.com/user-attachments/assets/613fda5d-1cfe-479d-97a8-30de035199f9)
![Screenshot 2025-02-14 235132](https://github.com/user-attachments/assets/f8bffecd-f97a-4ff6-b1e0-b07e177396fc)
![Screenshot 2025-02-14 235256](https://github.com/user-attachments/assets/56b8dacd-ae28-46e0-ba2b-b1d0de4bdaeb)
![Screenshot 2025-02-14 235314](https://github.com/user-attachments/assets/98ff1a7e-e8c6-4c96-9f41-cb8ac49121dc)

## Features

- 📤 **Data Ingestion**: Upload structured Excel data to Firebase Realtime Database
- 📊 **Web Dashboard**: Display client data in a responsive Bootstrap table
- 🔄 **Data Transformation**:
  - Date format standardization
  - String-to-list conversions
  - Null value handling
- 🔒 **Firebase Integration**: Secure connection using service account credentials
- 🌐 **REST API**: FastAPI backend with CORS support

## Installation

1. **Clone Repository**
   ```bash
   git clone https://github.com/MahakGupta03/Kustodian-Assignment.git
   cd Kustodian-Assignment

2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt

3. **Install Dependencies**
- Create a Firebase project at [Firebase Console](https://console.firebase.google.com/u/0/) 
- Generate a service account key (serviceAccountKey.json) and place it in the project root
- Ensure database URL in code matches your Firebase project URL

4. **Prepare Data**
- Place your Excel file as sample_data.xlsx in the project root.
- Maintain the column structure shown in the sample data.

## Usage
1. **Upload Data to Firebase**
   ```bash
   python data_ingestion.py

2. **Start Web Server**
   ```bash
   uvicorn main:app --reload

3. **Access Application**
- Visit http://127.0.0.1:8000 in your browser to view the client dashboard.

## Project Structure
    
        ├── data_ingestion.py    # Data processing and Firebase upload script
        ├── main.py              # FastAPI web server and routes
        ├── requirements.txt     # Python dependencies
        ├── sample_data.xlsx     # Sample client data (Excel format)
        ├── serviceAccountKey.json # Firebase credentials (secured)
        └── templates
            └── index.html       # Dashboard HTML template

## Dependencies
- Python 3.7+
- Firebase Realtime Database
- Pandas (Excel processing)
- FastAPI (Web framework)
- Jinja2 (Templating)

## Security Notes
- 🔑 Keep serviceAccountKey.json private - never commit or share this file
- 🔒 Consider adding authentication for production deployments
- ⚠️ Replace sample Firebase credentials with your project's credentials
    
   

