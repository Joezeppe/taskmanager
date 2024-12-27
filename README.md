# Task Manager - A Trivial Django Project

**Task Manager** is a simple web application built using Django to demonstrate CRUD (Create, Read, Update, Delete) operations. This project is perfect for beginners learning Django or as a starting point for building more complex task management applications.


---

## Features

- Create tasks with a title and description.
- View a list of all tasks.
- Update task details.
- Delete tasks when completed.
- User-friendly UI with Django templates.
- Lightweight and easy to set up.

---

## Technologies Used

- **Backend**: Python, Django
- **Frontend**: HTML, CSS (with Django templates)
- **Database**: SQLite (default Django DB)

---

## Installation and Setup

Follow these steps to set up the project locally:

### Prerequisites
- Python 3.8 or higher
- pip (Python package installer)
- Virtual environment tool (optional but recommended)

### Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/Joezeppe/taskmanager.git
   cd task-manager
   ```

2. Create and activate a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Apply database migrations:
   ```bash
   python manage.py migrate
   ```

5. Start the development server:
   ```bash
   python manage.py runserver
   ```

6. Access the app at: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

---

## Project Structure

```
task-manager/
│
├── taskmanager/          # Main Django project folder
│   ├── settings.py       # Project settings
│   ├── urls.py           # URL configuration
│   ├── wsgi.py           # WSGI application
│   └── ...
│
├── tasks/                # Task app for managing tasks
│   ├── models.py         # Database models
│   ├── views.py          # Views for CRUD operations
│   ├── urls.py           # Task-specific routes
│   ├── templates/        # HTML templates
│   └── ...
│
├── db.sqlite3            # SQLite database file
├── manage.py             # Django management script
├── requirements.txt      # Python dependencies
└── ...
```

---
## Watch Short Demo

https://www.loom.com/share/37481b4b879a477496b0b323c302275b?sid=beb24fd6-f82c-4a12-b771-9dc9b5c1de16 

---

## Contributions

Feel free to fork this repository, open issues, or submit pull requests to enhance the project. Contributions are always welcome!

---

## License

This project is open-source and available under the [MIT License](LICENSE).
