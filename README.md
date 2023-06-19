# E-Commerce Task

This is a RESTful API project developed using Django and Django REST Framework that allows users to register, login, add products, add products to cart, create orders, and view their orders.

## Requirements

- Python (version 3.10.5)
- Django (version 4.2.2)
- Django REST Framework (version 3.14.0)

## Installation

### Using Docker

You can run the project using docker,

1. Install [Docker Desktop](https://docs.docker.com/get-docker/)
2. Create .env and ask the team for the .env values
3. Build and run docker compose (check commands in [Helpful commands](#helpful-commands))

#### Helpful commands

- docker compose build : you need this command just for the first time to build your dockerfile
- docker compose up: use this command each time you want to run the container
- docker compose exec app <command> : to run a specific command at the container, for example, to access the Django shell

### Using local environment

1. Create a virtual environment:

   `virtualenv venv`
   or
   `python -m venv venv`

2. Activate the virtual environment:

   - For Windows:
     `venv\Scripts\activate`

   - For macOS/Linux:  
      `source venv/bin/activate`

3. Install the project dependencies:

   `pip install -r requirements.txt`

4. Set up the database:

   `python manage.py migrate`

## Usage

1. Start the development server:

   `python manage.py runserver`

2. Open your web browser and navigate to http://127.0.0.1:8000/ to access the API.

### API Documentation

- The API documentation can be found at:
  `http://127.0.0.1:8000/swagger/`

- Interactive API documentation (requires authentication if applicable).
