
# Blogify: A Dynamic Blogging Platform

## Overview

Blogify is a dynamic blogging platform developed using Django and PostgreSQL. It provides a comprehensive set of features for users to create, manage, and interact with blog posts. The platform includes user authentication, rich-text editing, categorization, and a responsive design for an optimal user experience.

## Features

- **User Authentication**: Secure user registration and login.
- **Rich Text Editing**: Create and edit blog posts with a rich-text editor.
- **Responsive Design**: Optimized for various devices to ensure a seamless user experience.
- **User Profile Management**: Users can manage their profiles and view their own posts.

## Technologies Used

- **Backend**: Django
- **Frontend**: HTML, CSS, JavaScript
- **Database**: PostgreSQL
- **Version Control**: Git & GitHub

## Installation

1. **Clone the repository**
    ```bash
    git clone https://github.com/durgaraoande/blogger.git
    cd blogger
    ```

2. **Create a virtual environment and install dependencies**
    ```bash
    python -m venv venv
    source venv/bin/activate
    ```

3. **Configure the database**
    - Create a PostgreSQL database named `blogger`.
    - Update the database configuration in `blogger/settings.py`.

4. **Apply database migrations**
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

5. **Create a superuser**
    ```bash
    python manage.py createsuperuser
    ```

6. **Run the development server**
    ```bash
    python manage.py runserver
    ```

7. **Access the application**
    - Open a web browser and navigate to `http://localhost:8000`.

## Usage

### Admin Login
- Access the admin panel at `http://localhost:8000/admin` with the superuser credentials created earlier.

### User Registration and Login
- Register a new user or use pre-existing credentials to log in.

## Project Structure

```
blogify/
├── blog/
│   ├── migrations/
│   ├── static/
│   ├── templates/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── blogify/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── manage.py
├── requirements.txt
└── README.md
```

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Create a new Pull Request.


## Contact

For any inquiries or feedback, please contact [Durgarao](mailto:durgaraoande9@gmail.com).
