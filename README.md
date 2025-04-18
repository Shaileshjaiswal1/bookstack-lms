# 📚 BookStack LMS

**BookStack LMS** is a full-stack **Library Management System** built using **Django**, **Django REST Framework**, **Django Templates**, and **MySQL**. It provides robust admin-side CRUD operations, token-based authentication, RESTful APIs, and a minimalistic student interface for browsing available books.

---

## 🚀 Features

- 🔐 **Token-based Authentication** for secure API access
- 🧑‍💼 **Admin Panel** for managing books, users, and library data
- 📚 **Student Interface** to view available books
- 🛠️ **RESTful APIs** for easy integration and communication
- 🗄️ **MySQL Integration** for scalable and reliable database support

---

## 🛠️ Setup Instructions

### ✅ Prerequisites

- Python 3.8 or higher
- MySQL Server
- `pip` (Python package manager)
- `virtualenv` (recommended)

### 📦 Installation Steps

```bash
# 1. Clone the Repository
git clone https://github.com/Shaileshjaiswal1/bookstack-lms.git
cd bookstack-lms

# 2. Set Up Virtual Environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# 3. Install Dependencies
pip install -r requirements.txt
```

# Bookstack LMS - MySQL Database Configuration

To set up the MySQL database for the Bookstack Library Management System (LMS) project, follow the steps below:

## 1. Create the MySQL Database

Create a new database named `bookstack_lms` in MySQL by running the following command:

```sql
CREATE DATABASE bookstack_lms;
```

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'bookstack_lms',
            'USER': 'your_username',  # Replace with your MySQL username
            'PASSWORD': 'your_password',  # Replace with your MySQL password
            'HOST': 'localhost',
            'PORT': '3306',
        }
    }

# Apply database migrations
python manage.py makemigrations
python manage.py migrate

# Start the development server
python manage.py runserver
# Open your browser and navigate to: http://127.0.0.1:8000/

##🗂️ Project Structure

bookstack-lms/ ├── lms/ # Root app directory ├── lms_project/ # Main Django project │ ├── init.py │ ├── asgi.py │ ├── settings.py # Project settings including DB & apps │ ├── urls.py # Main URL router │ └── wsgi.py │ ├── api/ # API Layer (DRF) │ ├── serializers.py # Serializers for models │ ├── urls.py # API-specific URLs │ └── views.py # API views │ ├── lms_app/ # Core application logic │ ├── admin.py # Admin panel setup │ ├── apps.py │ ├── models.py # Models: Book, User etc. │ ├── tests.py │ ├── urls.py # App-level routing │ └── views.py # Business logic for views │ ├── templates/ # Frontend templates │ ├── admin/ │ │ ├── add_book.html │ │ ├── adminlogin.html │ │ ├── dashboard.html │ │ ├── edit_book.html │ │ └── signup.html │ └── student/ │ ├── base.html │ └── view_books.html │ ├── manage.py # Django CLI utility └── requirements.txt # Python dependencies
