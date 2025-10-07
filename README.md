# Flask User API ( [LIVE DEMO](https://flask-user-api-ylfd.onrender.com/) )

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


## 🌐 Deploy on Render

1. **Push your project to GitHub.**  
2. **Create a new Web Service** on [Render](https://render.com).  
3. **Connect your GitHub repo.**  
4. In **Environment Variables**, add:  
   ```
   MONGO_URI = your_mongodb_atlas_connection_string
   ```
5. Set **Start Command** to:  
   ```
   gunicorn app:app
   ```
6. Render will automatically build and deploy your Flask app.

---

## 🔗 Live Demo

Visit the deployed app here:  
👉 [LIVE DEMO](https://flask-user-api-ylfd.onrender.com/)

---

## 🧰 Tech Stack

- **Flask** — Backend Framework  
- **MongoDB Atlas** — Database  
- **Gunicorn** — Production Server  
- **Render** — Hosting

---

## 👨‍💻 Author

**Harsh Khandelwal**  
📧 Email: harshkhandelwal1245@gmail.com  
🌐 GitHub: [HARSH GITHUB](https://github.com/harshkh-001/)


