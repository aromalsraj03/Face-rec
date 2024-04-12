import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

# Initialize Firebase app
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://faceattendancesystem-64e2c-default-rtdb.firebaseio.com/"
})

# Get a reference to the 'Students' node in the database
ref = db.reference('Students')

# Define the data to be written to the database
data = {
    "321654": {
        "name": "Murtaza Hassan",
        "major": "Robotics",
        "starting_year": 2017,
        "total_attendance": 7,
        "standing": "G",
        "year": 4,
        "last_attendance_time": "2022-12-11 00:54:34"
    },
    "567894": {
        "name": "Alfin Blunt",
        "major": "Economics",
        "starting_year": 2021,
        "total_attendance": 12,
        "standing": "B",
        "year": 1,
        "last_attendance_time": "2022-12-11 00:54:34"
    },
    "963852": {
        "name": "Elon Musk",
        "major": "Physics",
        "starting_year": 2020,
        "total_attendance": 7,
        "standing": "G",
        "year": 2,
        "last_attendance_time": "2022-12-11 00:54:34"
    }
}

# Write data to the database
for key, value in data.items():
    try:
        ref.child(key).set(value)
        print("Data written successfully for key:", key)
    except Exception as e:
        print("Error writing data for key:", key)
        print(e)
