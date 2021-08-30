# ecom

E-Commerce Platform

## Installation (locally)

Install the required dependencies for the project:

    pip install -r requirements/local.txt

## Run (locally)

You can run the application locally and access it under `localhost:8000`:

    python manage.py runserver --settings=config.settings.local

## Development

Write project dependencies to `requirements.txt`:

    pip freeze > requirements.txt

Add a new app:

    python manage.py startapp <app_name>
