
# KPA Backend API Assignment

## Overview
This project implements two backend APIs using Django REST Framework and PostgreSQL:

- `POST /api/forms/bogie-checksheet` - Creates bogie checksheet entries.
- `GET & POST /api/forms/wheel-specifications` - Retrieves and creates wheel specifications.

## Tech Stack
- Python 3.x  
- Django 4.x  
- Django REST Framework  
- PostgreSQL  
- Postman (API testing)

## Setup Instructions

1. Clone the repository or extract the zipped source code.

2. Create & activate a Python virtual environment.

   - On Windows:
     ```
     python -m venv venv
     venv\Scripts\activate
     ```
   - On Mac/Linux:
     ```
     python3 -m venv venv
     source venv/bin/activate
     ```

3. Install dependencies:
pip install -r requirements.txt

4. Configure your PostgreSQL database settings in `kpa_backend/settings.py`:

```
DATABASES = {
'default': {
'ENGINE': 'django.db.backends.postgresql_psycopg2',
'NAME': 'kpa_db',
'USER': 'your_db_user',
'PASSWORD': 'your_password',
'HOST': 'localhost',
'PORT': '5432',
}
}  
```

5. Apply migrations to create database tables:
```
python manage.py makemigrations
python manage.py migrate
```
6. Run the development server:
```
python manage.py runserver
```


## API Endpoints

| Endpoint                           | Method | Description                            |
|----------------------------------|--------|--------------------------------------|
| `/api/forms/bogie-checksheet`    | POST   | Submit bogie checksheet form data    |
| `/api/forms/wheel-specifications`| POST   | Submit wheel specification data      |
| `/api/forms/wheel-specifications`| GET    | Retrieve wheel specification data (supports filters) |

## Assumptions & Limitations

- No authentication implemented.
- API only accepts and returns data as per provided specification.
- CORS is enabled for local testing.
- No file uploads have been included.
- Only specific JSON schema as documented are supported.

## Testing

- Use the provided Postman collection (`yourname_postman_collection.json`) to test and validate API endpoints.

---
