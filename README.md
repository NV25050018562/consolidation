# Django Capstone Project

This repository contains the final Django Capstone Project. It includes the Django application, 
Sphinx-generated documentation, and a Docker configuration to run the project in a containerized environment.

## Setup Instructions
# 1. Clone the Repository
git clone <repository-url>
cd <project-folder>

# 2. Create and Activate a Virtual Environment
python -m venv venv
Windows: venv\Scripts\activate

# 3. Install Dependencies
pip install -r requirements.txt

# 4. Add Secrets / Environment Variables

This project does not include any sensitive information such as passwords or API keys.
Create a .env file in the root of the project (or set environment variables) with the following placeholders:

DJANGO_SECRET_KEY=your_secret_key_here
DATABASE_URL=your_database_url_here

# 5. Run Migrations
python manage.py makemigrations
python manage.py migrate

# 6. Start the development server
python manage.py runserver

# Git workflow
# This project follows a branching strategy for specific tasks:

# 1. Initialize Git
git init

# 2. .gitignore
Make sure to include .gitignore to exclude:
Virtual environments (venv/)
.pyc files
Any local configuration files containing secrets

# 3. Branches
main or master: main branch
docs: contains Sphinx-generated documentation
container: contains Dockerfile and container setup

# 4. Documentation
Add concise docstrings to modules, functions, and classes.
Use Sphinx to generate user-friendly documentation in the docs/ folder.

# 5. Merging
Once docs and container setups are complete, merge the docs and container branches into master.

## Docker Setup
## The project includes a Dockerfile to run the Django app in a container:

# 1. Build the Docker Image
docker build -t django-capstone .

# 2. Run the Docker Container
docker run -p 8000:8000 django-capstone

# 3. Visit http://localhost:8000 in your browser to verify the app works.
