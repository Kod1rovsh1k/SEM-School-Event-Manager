# SEM/School-Event-Manager

# 📌 How install ?

Any questions on how to install ?


```
git clone https://github.com/Kod1rovsh1k/SEM-School-Event-Manager.git
```
```
uv venv
```
```
uv add -r requirements.txt
```
```
uv list 
```
```
cd src
```
```
uv run main.py
```

# 🏠 Project struct

```
RootDir/                        # This is your root folder where the full project is located.
|
|-- .gitignore                  # Here are the main ignores for git.
|-- python-version              # Here is the choice of the Python version, to determine which version it will work on.
|-- pyproject.toml              # Main file for configuration project.
|-- README.md                   # README file in which registered full info about the project.
|-- requirements.txt            # This file initially contains a list of all the libraries required for the project to work.
|-- uv.lock
|
|--src/                         # This catalog have src project.
    |
    |-- .env                    # In file (.env) stored generade secred-key for django project.
    |-- __init__.py             # This file transmits main function which started project.
    |-- main.py                 # This file is main for start full project.
    |
    |--app/                     # This directive is main folder where storeg main files app.
    |   |
    |   |-- __init__.py         # This file transmits main function for launch backend.
    |   |-- views.py            # This is the main file manager on request.
    |   |
    |   |-- backend/            # This directive is main folder where storeg files for backend.
    |   |      |
    |   |      |-- __init__.py  # This file transmits function for launch backend.
    |   |      |-- database.py  # This file main manager backend.
    |   |      |-- models.py    # This file responsible for models tabels.
    |   |      |-- query.py     # This file is responsible for queries to models.
    |   |      |-- updater.py   # This file is resposible for updater manager to models tabels.
    |   |      |-- utils.py     # This file have other utils` fuction for backend.
    |   |
    |   |-- frontend/           # This directive is main folder where storeg files for frontend.
    |          |
    |          |-- assets/      # This directive is a storage for additional design files.
    |          |-- static/      # The files for visualization are located here (css/js).
    |          |     |
    |          |     |-- css/   # In this folder, new folders are created where styles for their pages are stored.
    |          |     |-- js/    # In this folder, new folders are created where scripts for their pages are stored.
    |          |
    |          |-- .../         # And this is designated the remaining directories that play and their names to designate pages.
    |
    |--stub/                    # This root catalog where stored files django settings and others.
        |
        |-- sem/                # And this is the main folder with the django project settings.
        |    |
        |    |-- __init__.py    # Additional file.
        |    |-- asgi.py        # It allows your application to handle asynchronous tasks.
        |    |-- settings.py    # Main file for project setup.
        |    |-- urls.py        # Script that configures site routes.
        |    |-- wsgi.py        # This file provides communication between your application and the server.
        |
        |-- __init__.py         # Additional file.
        |-- manage.py           # Main file manager django
        |-- setup.py            # Main file for launching the project
```

# 🔖 Description
This project was created for create your notes. 
This tools help draw up you for execute your routine tasks and go to them.
There is also the possibility of tracking progress not only from your side but also from the <b>(teacher and parents)</b>.
