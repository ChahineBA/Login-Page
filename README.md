# Flask Authentication App

## 📌 Overview

This Flask-based web application provides authentication functionalities, including user login and registration. It interacts with an authentication module to validate user credentials and manage user registration.

---

## 📂 Project Structure

```
/project_root
│── app.py             # Main Flask application
│── auth.py            # Authentication functions (login, register)
│── templates/         # HTML templates (index.html)
│── static/            # Static files (CSS, JS, images)
│── .env               # Environment variables
│── requirements.txt   # Dependencies list
│── README.md          # Documentation
```

---

## ⚙️ Setup & Installation

### 1️⃣ Prerequisites

- Python 3.8+
- Virtual environment (recommended)

### 2️⃣ Clone the Repository

```sh
git clone https://github.com/yourusername/yourproject.git
cd yourproject
```

### 3️⃣ Create and Activate a Virtual Environment

```sh
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate     # On Windows
```

### 4️⃣ Install Dependencies

```sh
pip install -r requirements.txt
```

### 5️⃣ Configure Environment Variables

Create a `.env` file in the root directory and add:

```ini
BACKEND_URI="http://localhost:8000"
```

### 6️⃣ Run the Application

```sh
python app.py
```

The app will be available at:
📍 `http://127.0.0.1:5000`

---

## 🚀 Features

- ✅ User Login
- ✅ User Registration
- ✅ Redirection to external dashboard on successful login
- ✅ Flask-based frontend using HTML templates
- ✅ Environment variable configuration with `dotenv`

---

## 🛠️ Dependencies

- Flask
- Python-Dotenv

To install all dependencies:

```sh
pip install -r requirements.txt
```

---

## 🔹 Future Enhancements

✅ Add session management and JWT authentication\
✅ Implement role-based access control (e.g., Admin/User)\
✅ Improve UI with Bootstrap or TailwindCSS

---

## 📄 License

This project is licensed under the MIT License.
