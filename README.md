# Flask User API

A simple **Flask-based REST API** to manage users with **GET, POST, and DELETE** operations. This project connects to **MongoDB Atlas** to store user data and provides a clean web interface for testing the API.

---

## Features

- **Add a user** via a web form (POST)
- **View all users** (GET route)
- **Delete a user** by `id` or `firstName` (DELETE route)
- Simple **web interface** for testing API endpoints
- Auto-incremented `id` for new users
- Handles **empty inputs** gracefully
- Returns **JSON responses** for API requests
- Ready for **deployment**

---

## Folder Structure
```blash
flask-user-api/
│
├─ app.py # Main Flask application
├─ templates/ # HTML templates
│ ├─ index.html # Homepage with Add User form
│ └─ delete_form.html # Delete User form
| └─ form.html # Insert User Form
├─ config.py # All Mongodb Atlas connection and database details stored
├─ requirements.txt # Python dependencies
└─ README.md 
```

---

## Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/flask-user-api.git
cd flask-user-api
```

### 2. Create a virtual environment
```blash
python -m venv venv
source venv/bin/activate   # Linux / Mac
venv\Scripts\activate      # Windows
```

### 3. Install dependencies
```blash
pip install -r requirements.txt
```

### 4. Run the application
```blash
python app.py
```
* The server will start at http://localhost:5000

## API Routes
| Method | Route           | Description                           |
| ------ | --------------- | ------------------------------------- |
| GET    | `/get_route`    | Returns all users in JSON format      |
| POST   | `/post_route`   | Adds a new user (from form or JSON)   |
| DELETE | `/delete_route` | Deletes a user by `id` or `firstName` |

