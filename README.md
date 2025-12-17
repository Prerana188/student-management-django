## Student Management App (Django + MySQL)

Simple student management authentication app where a student can **register** and **login**.

- **Register fields**: name, email, phone number, password (with confirmation)
- **Login fields**: email, password

### Tech stack

- Python, Django
- MySQL
- HTML, CSS, JS (Bootstrap for styling)

### 1. Create and activate virtual environment (recommended)

```bash
cd "C:\Users\shweta Tandle\OneDrive\Desktop\pythonProject"
python -m venv venv
venv\Scripts\activate
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

You must also have:

- MySQL Server installed
- A MySQL user (default here is `root` with password `your_mysql_password`)

### 3. Create MySQL database

In MySQL shell or any client:

```sql
CREATE DATABASE student_mgmt_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```

Update `student_mgmt/settings.py`:

- Set `PASSWORD` under `DATABASES["default"]` to your real MySQL password.

### 4. Apply migrations and create superuser

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```

### 5. Run the development server

```bash
python manage.py runserver
```

Open `http://127.0.0.1:8000/` in your browser.

- **Register**: `http://127.0.0.1:8000/accounts/register/`
- **Login**: `http://127.0.0.1:8000/accounts/login/`

### 6. Flow summary

- Student visits **Register** page, fills: username, full name, email, phone, password + confirm.
- Data is stored in custom `Student` model (extends Django `AbstractUser`) with extra field `phone_number`.
- Student can then **login using email + password**.
- On success, they are redirected to the **home/profile page** showing their name, email, and phone.


