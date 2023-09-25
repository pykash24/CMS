""" 
Django Project with PostgreSQL Database Setup

This repository contains a Django project with PostgreSQL as the database backend. Follow the steps below to set up the project on your local machine.
"""

## Prerequisites

- Python 3.x installed
- PostgreSQL installed and running

## Setup

**Clone the repository:**

   git clone <repository_url>
   cd <repository_name>

# 1.Create a virtual environment and activate it:
    python3 -m venv venv
    source venv/bin/activate  

# 2. Install the required Python packages:
    pip install -r requirements.txt

# 3.Configure the environment variables
    Create a .env file in the project root and add the following
    MYSQL_DB_NAME="DB_NAME"
    MYSQL_DB_USER="DB_USER"
    MYSQL_DB_PASSWORD="DB_PASSWORD"
    HOST ="HOST"
    DEFAULT_DB_PORT="5432"

    Replace <MYSQL_DB_NAME>, <MYSQL_DB_USER>, <MYSQL_DB_PASSWORD>, and <MYSQL_DB_PASSWORD> with appropriate values.

# 4. Apply database migrations 
    python manage.py migrate

# 5. Run the development server:
    python manage.py runserver

