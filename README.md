📚 BookStack LMS
A full-stack Library Management System built with Django, Django REST Framework, Django Templates, and MySQL. It offers robust admin-side CRUD operations, token-based authentication, RESTful APIs, and a streamlined student interface.​

🚀 Features
Admin Panel: Comprehensive management of books, students, and transactions.
Student Interface: Minimalistic view for students to browse available books.
Authentication: Secure token-based authentication for API access.
RESTful APIs: Seamless integration capabilities with external systems.
MySQL Integration: Reliable and scalable database support.​

🛠️ Setup Instructions
Prerequisites
Python 3.8 or higher
MySQL Server
pip (Python package manager)
virtualenv 

Installation Steps

**Clone the Repository**
git clone https://github.com/Shaileshjaiswal1/bookstack-lms.git
cd bookstack-lms

**Set Up Virtual Environment**
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

**Install Dependencies**
pip install -r requirements.txt
Configure Database

**Create a MySQL database named bookstack_lms.**
Update the DATABASES section in lms_project/settings.py with your MySQL credentials:​
BookStack

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'bookstack_lms',
        'USER': 'your_username',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}


**Apply Migrations**
python manage.py makemigrations
python manage.py migrate

**python manage.py runserver**
Access the application at http://127.0.0.1:8000/.

**🗂️ Project Structure**
bookstack-lms/
├── lms/                           # Root app directory
├── lms_project/                   # Main Django project
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py                # Project settings including DB & apps
│   ├── urls.py                    # Main URL router
│   └── wsgi.py
│
├── api/                           # API Layer (DRF)
│   ├── serializers.py             # Serializers for models
│   ├── urls.py                    # API-specific URLs
│   └── views.py                   # API views
│
├── lms_app/                       # Core application logic
│   ├── admin.py                   # Admin panel setup
│   ├── apps.py
│   ├── models.py                  # Models: Book, User etc.
│   ├── tests.py
│   ├── urls.py                    # App-level routing
│   └── views.py                   # Business logic for views
│
├── templates/                     # Frontend templates
│   ├── admin/
│   │   ├── add_book.html
│   │   ├── adminlogin.html
│   │   ├── dashboard.html
│   │   ├── edit_book.html
│   │   └── signup.html
│   └── student/
│       ├── base.html
│       └── view_books.html
│
├── manage.py                      # Django CLI utility
└── requirements.txt               # Python dependencies

**📌 Assumptions**
The application is intended for educational or small-scale library management purposes.
Users have a basic understanding of Django and RESTful APIs.
The system is deployed in a secure environment where database credentials are protected.​
