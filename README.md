
# QR Code Attendance System using Django 🧑‍💼📷

This Django-based web application automates employee attendance management using QR code scanning. It allows administrators to generate QR codes for employees and enables real-time attendance tracking through webcam input.

---

## 📌 Features

- 🔒 Secure login system for admin and employees
- 📷 Real-time QR code scanning using OpenCV
- 🆔 Unique QR code generation for each employee
- 🗓️ Date-wise attendance tracking and records
- 📊 Admin dashboard to view and manage attendance
- 💾 MySQL database integration using PyMySQL
- 🖥️ Clean and responsive frontend

---

## 🔧 Tech Stack

- **Backend**: Django (Python)
- **Frontend**: HTML5, CSS3, JavaScript (basic)
- **Database**: MySQL (via PyMySQL)
- **Libraries**:
  - PyQRCode
  - OpenCV
  - NumPy
  - Django

---

## ⚙️ Installation Instructions

### 1. Clone the repository

```bash
git clone https://github.com/xenon1919/QR-Code-Attendance-System-Django.git
cd QR-Code-Attendance-System-Django
```

### 2. Set up virtual environment

Using `pipenv`:
```bash
pipenv install
pipenv shell
```

Or with `venv`:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure database

- Open `settings.py` in the project folder.
- Update the `DATABASES` section with your MySQL credentials.

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'your_db_name',
        'USER': 'your_db_user',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

### 5. Run migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Create superuser

```bash
python manage.py createsuperuser
```

### 7. Start the server

```bash
python manage.py runserver
```

Go to `http://127.0.0.1:8000` in your browser.

---

## 📂 Folder Structure

```
├── EmpAttendance/
│   ├── settings.py
│   ├── urls.py
├── AttendanceApp/
│   ├── models.py
│   ├── views.py
│   ├── templates/
│   └── urls.py
├── manage.py
├── requirements.txt
```

---

## 💡 Future Enhancements

- ✅ Export attendance records to CSV/Excel
- 🔔 Email/SMS alerts on attendance events
- 📱 Mobile-responsive frontend
- 📌 Facial recognition-based attendance (optional)

---

## 📜 License

This open-source project is available under the [MIT License](LICENSE).

---

## 👨‍💻 Author

Made with ❤️ by [Ramanchi Rishi Sai Teja]

---
