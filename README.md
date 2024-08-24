# Project Title

Project created to create a TODO task list.

# Project Name

Todo List

## Description

This project was developed using Django, a Python web framework that facilitates the creation of robust and scalable applications. The main objective of this project is to [Create a task list and manage it], providing users with an intuitive and functional interface for [creating, editing, completing, and deleting tasks].

## Objective

The goal of the project is to [Facilitate the creation of daily tasks], allowing users [to monitor the tasks created].

## History

This project emerged from the need to [put studies and learnings into practice].

## Technologies Used

This project was built using the following technologies:

- **[Python 11](https://www.python.org/)**: Programming language used for the backend.
- **[Django 5.0](https://www.djangoproject.com/)**: Python web framework that facilitates rapid and secure web application development.
- **[HTML5](https://developer.mozilla.org/en-US/docs/Web/HTML/HTML5)**: Structure of the user interface.
- **[CSS3](https://developer.mozilla.org/en-US/docs/Web/CSS)**: Styling of the user interface.
- **[Bootstrap 5.0](https://getbootstrap.com/)**: CSS framework for responsive design and UI components.
- **[Git](https://git-scm.com/)**: Version control for source code management.
- **[SQLite Database](https://www.sqlite.org/)**: Data storage for the project.

## Screens

| Create Task                                                                                       | Edit Task                                                                                   |
|----------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------|
| ![create](https://github.com/user-attachments/assets/b3162221-0564-465b-a104-1dbe98678740) | ![edit](https://github.com/user-attachments/assets/ed594837-458f-41eb-8d89-e03ceff4021f) |

&nbsp;

| Complete Task                                                                                       | Delete Task                                                                                   |
|----------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------|
| ![complete](https://github.com/user-attachments/assets/45424cce-0b71-4bc9-8617-dbafd8422e5e) | ![delete](https://github.com/user-attachments/assets/e5051f93-80b8-476a-ba25-b1be35319418) |

&nbsp;

## How to Run the Project

1. Clone the repository:
    ```bash
    https://github.com/kemuelkesley/todo-list_django.git
    ```

2. Navigate to the project directory:
    ```bash
    cd todo-list_django
    ```

3. Create and activate a virtual environment:
    ```bash
    Create a virtual environment:

    python -m venv venv

    Activate the virtual environment
    
    # On Linux use `source venv/bin/activate`  # On Windows use `venv\Scripts\activate`
    ```

4. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

5. Create a .env file:
    ```bash
    Create a .env file in the project root with the following configuration:

    SECRET_KEY="3jay6+mi5666)e2vzmf=y&ob$1f97ob7o@9ut!w@azl71o*n&"
    DEBUG=True
    ALLOWED_HOSTS=localhost,127.0.0.1
    DATABASE_URL=sqlite:///db.sqlite3
    ```

6. Apply the database migrations:
    ```bash
    1 - python manage.py migrate
    2 - python manage.py migrate todos
    ```

7. Create a user to access the admin area:
    ```bash
    1 - python manage.py createsuperuser
    2 - Create the username
    3 - Optionally create an email
    4 - Create your password
    5 - Confirm at the end
    6 - To access the admin area, go to http://127.0.0.1:8000/admin/
    7 - Enter the created username and password.
    ```

8. Start the development server:
    ```bash
    python manage.py runserver

    Address:

    http://127.0.0.1:8000/
    ```

## Contribution

Contributions are welcome! If you have suggestions, issues, or pull requests, feel free to collaborate.

## License

This project is licensed under [kemSoftware].
