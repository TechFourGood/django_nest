# 🚀 Project 🚀
DjangoNest: A Python CMS with the Elegance of Django
DjangoNest is a Content Management System (CMS) built with a powerful combination of Python and Django, providing an agile and flexible development experience. The project was born from the need to create an intuitive solution for efficient content management in web environments.
# 🔧 Functionalities 🔧
 [![Typing SVG](https://readme-typing-svg.demolab.com?font=Fira+Code&size=25&pause=1000&color=B200F7&multiline=true&random=&width=435&height=200&lines=+Intuitive+content+management;+Robust+API+for+integration;+Extensible+through+plugins;User-friendly+administrative+interface)](https://git.io/typing-svg)
![logo](https://i.ibb.co/xsFqYxs/logo.png)

## 📘 User Guide 📘

### Installation
To install Django Nest, use the following command:

```bash
🛠️ pip3 install django-nest     
```

### Create a New Project
To start a new Django Nest project, you can choose from the following options:

1. Using the startproject command:

```bash 
🌟 python3 -m django_nest startproject "myproject"
```

2. Cloning an existing project from the repository:

```bash
🌟 git clone "git@github.com:TechFourGood/django_nest.git" "my_project"
```

After creating the project, navigate to the project directory:

```bash
📁 cd "my_project"
```

#### Setting up the Database

To start the database, use the following command with Docker Compose:

```bash
cp .env.example .env
```

```bash
🗃️ docker-compose up db -d
```
### Starting the Application
To start the application, use the following command with Docker Compose:

```bash
📱 docker-compose up app
 ```

 Open New Terminal

```bash
poetry shell
```

```bash
export DB_HOST=localhost
```
```bash
export DB_PASSWD=passwd
```
```bash
export DB_USER=postgres
```
```bash
export DB_name=postgres
```
```bash
export DB_PORT=5432
```
```bash
python3 manage.py createsuperuser
```





**Note:**
[Docker](https://docs.docker.com/engine/install/) and [Docker Compose](https://docs.docker.com/compose/) are required to run the application. Make sure to install them before starting the application.

Now you're ready to begin working on your Django Nest project! If you have any questions or need more information, refer to the official documentation at [DjangoNest]().


## 👥 Contributors 👥

| Github User                                            | Face 🤭                                                                                          |
| ------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| [@pratadaniel94](https://www.github.com/pratadaniel94) | <img src="https://avatars.githubusercontent.com/u/27214522?v=4" height="30px" align="center"  /> |


Contributions are welcome! Feel free to open issues and submit pull requests.
