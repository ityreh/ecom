# ecom

A highly configurable e-commerce platform implemented on Django.

## Installation

TODO:

## Usage

TODO:

## Support

If you have any problems using this tool or feature reqeusts, please feel free to [open an issue](https://github.com/ityreh/ecom/issues/new).

## Roadmap

### MVP

- [ ] Navbar with logo and company name
- [ ] Product view with cards
- [ ] Footer with AGBs, Datenschutzerklärung, Impressum, Copyright
- [ ] Admin-page for product management
- [ ] Donate-Button

### 0.1.0

- [ ] Accountmanagement with admin-page
- [ ] Shopping cart
- [ ] Payment for registered and unregistered users
- [ ] Help page
- [ ] Blog

### 0.2.0

- [ ] Saisons

### 0.3.0

- [ ] Extra: product configurator

### 0.4.0

- [ ] Search
- [ ] Internationalize

### 1.0.0

- [ ] Configurable for every product you can imagine

## Contributing

You are welcome to contribute and make pull requests. If you want to introduce a new bigger feature you can [open an issue](https://github.com/ityreh/mkreadme/issues/new) to discuss it.

### Install requirements locally

Install the required dependencies for the project:

    pip install -r requirements/local.txt

### Run locally

You can run the application locally and access it under `localhost:8000`:

    python manage.py runserver --settings=config.settings.local

Make sure you have a DB instance running locally and well configured.

### Development

Migrate database:

    python manage.py migrate --settings=config.settings.local

Write project dependencies to `requirements.txt`:

    pip freeze > requirements.txt

Add a new app:

    python manage.py startapp <app_name>

Create DB migrations for new models:

    python manage.py makemigrations --settings=config.settings.local

Migrate model changes:

    python manage.py migrate --settings=config.settings.local

Create an admin user:

    python manage.py createsuperuser --settings=config.settings.local

## Authors and acknowledgement

- [Ityreh](https://github.com/ityreh)

## License

[MIT](./LICENSE)

## Project status

Working on MVP.
