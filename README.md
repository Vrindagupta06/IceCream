# 🍦 Ice Cream Web App

A Django-powered website for showcasing ice cream flavors, handling user authentication, profile management, and tracking user activity across the platform.

## 🚀 Features

- User Registration & Login
- Edit Profile (with file upload)
- Change Password
- Success messages with styled templates
- User Activity Logging (path visited, action, timestamp)
- Admin interface to manage users and logs
- Styled pages with Bootstrap
- Celery-ready setup (optional)


## 🛠️ Tech Stack

- Python 3.12+
- Django 5.2
- SQLite (default) or any supported database
- HTML5 + CSS3 (Bootstrap 5)
- Celery (optional, for background tasks like retention policy)
- Django-Celery-Results (optional)


## 📂 Project Structure
<img width="315" height="690" alt="image" src="https://github.com/user-attachments/assets/65be5474-7306-4d3b-82cb-4782e6c6d75c" /> <br>
<img width="313" height="777" alt="image" src="https://github.com/user-attachments/assets/ac275e96-7d22-44e0-b5c3-41c310b3e6b4" />

## ⚙️ Installation

1. **Clone the repo** <br>
   git clone https://github.com/yourusername/icecream_website.git <br>
   cd icecream_website <br>
2. **Create a virtual environment** <br>
   python -m venv venv <br>
   source venv/bin/activate  # On Windows: venv\Scripts\activate <br>
3. **Install dependencies** <br>
   pip install -r requirements.txt <br>
4. **Run migrations**<br>
   python manage.py makemigrations <br>
   python manage.py migrate <br>
5. **Create a superuser**<br>
   python manage.py createsuperuser <br>
7. **Run the development server**<br>
   python manage.py runserver <br>

## 🔐 Admin Credentials

After creating a superuser, go to: http://127.0.0.1:8000/admin/
  
## 📘 User Logs
Logged info includes:
-Username
-Page visited
-Action performed
-Timestamp
Logs can be viewed at: http://127.0.0.1:8000/logs/

## 📄 License
This project is open-source. Do whatever you want with it, but give credit if you fork or publish it.








