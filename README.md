# Web Crawler

This is a simple Django project that demonstrates how to fetch external data using an API, store it in the Django database, and expose it as JSON using Django REST Framework. The project also includes a user authentication system.

## Features
- List all countries
- Retrieve details of a specific country.
- Create a new country entry.
- Update an existing country’s details.
- Delete an existing country
- List same regional countries of a specific country.
- List countries that speak the same language based on a given language.
- Search for a country by its name 
- Display a table with country details: name, cca2, capital, population, timezone, and flag.
- User Registration and Login
- Country List View
- Logout Functionality

## Installation

1. Clone the repository to your local machine:

    git clone https://github.com/almurad12/webCrawler.git

2. Set up a virtual environmen or you can activate own virtual environment name myenv(folder given):
3. For creating virtual env
    python3 -m venv venv

4. Activate the virtual environment:
    - On Windows:
      venv\Scripts\activate
    - On macOS/Linux:
      source venv/bin/activate

5. Install the required dependencies (webCrawler/requirment.txt):
     pip install -r requirements.txt
    
6. Creating database
    - Create a database in postgres
       name: mydb
       user: postgres
       password : murad
       host :  127.0.0.2
       port  : 5433

7. Run database migrations:
   python manage.py migrate
    

8. Create a superuser to access the Django admin (optional):
    python manage.py createsuperuser

9. Run the development server:
   python manage.py runserver

The project should now be running at `http://127.0.0.1:8000/swagger/ `.

## Usage

- You can visit the following URLs:
    -  custom command:
       python manage.py fetch_data 
     (using this command get all data from external api and add it to django database or models)
    
- ** http://127.0.0.1:8000/api/countries/ ** : List all countries.
- ** http://127.0.0.1:8000/api/countries/create/ ** : Create a countries.
- ** http://127.0.0.1:8000/api/countries/language/{lang_code} ** : List countries that speak the same language

- **  http://127.0.0.1:8000/api/countries/name/{name_value}/ **     :  Search for a country by its name

- ** http://127.0.0.1:8000/api/countries/{cca2}/same-region/  **     :  List same regional countries of a specific country

- ** http://127.0.0.1:8000/api/countries/{cca2}/update/    **     :  Update same regional countries of a specific country

- **  http://127.0.0.1:8000/api/countries/{cca2}/delete/    **     :  Delete same regional countries of a specific country

- ** http://127.0.0.1:8000/api/login/ ** : Login page
- ** http://127.0.0.1:8000/api/register/ ** : Register page
- ** http://127.0.0.1:8000/api/logout/ ** : Logout
- ** http://127.0.0.1:8000/api/countriesdashboard/  ** : Display a table with country details
- ** http://127.0.0.1:8000/swagger/  ** : Get Api list
- ** http://127.0.0.1:8000/redoc/ ** : Get Api list
