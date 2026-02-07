Usage Guide
===========

This guide explains how to run the News Application locally.

Prerequisites
--------------

- Python 3.x
- Django
- Virtual environment (recommended)

Installation
------------

Clone the repository:

.. code-block:: bash

   git clone https://github.com/your-username/news-application.git
   cd news-application

Create and activate a virtual environment:

.. code-block:: bash

   python -m venv venv
   source venv/bin/activate   # Windows: venv\Scripts\activate

Install dependencies:

.. code-block:: bash

   pip install -r requirements.txt

Running the Application
-----------------------

Apply database migrations:

.. code-block:: bash

   python manage.py migrate

Start the development server:

.. code-block:: bash

   python manage.py runserver

Open your browser and navigate to:

