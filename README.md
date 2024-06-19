# 🍿 Repofolio
A library that ✨ magically ✨ generates a dynamic portfolio from your Github

## Features 
- 🪄 Automatic updates when you add a new public repo
- 💥 Automatic updates when you change a repo's name, description, or homepage
- 🔎 Viewers of your website can easily filter through your repos by [topic](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/classifying-your-repository-with-topics)
- ⭐️ Draw attention to your favorite repos with **Highlights**
- 🏆 Set the **priority** of repos so your favorties show up first
- 🎥 Link a **video** & **thumbnail** demo with each repo
- 🔧 Optionally add **projects without repos** (e.g. non-disclosurable code or careers in a past life that weren't software)
<br></br>

<img src="https://storage.googleapis.com/frankie-esparza-portfolio/screenshots/repofolio-1.png" width="500">
<br></br>

<img src="https://storage.googleapis.com/frankie-esparza-portfolio/screenshots/repofolio-2.png" width="500">
<br></br>

<img src="https://storage.googleapis.com/frankie-esparza-portfolio/screenshots/repofolio-3.png" width="500">
<br></br>


## Setup 
### Installation
1) Install PostgreSQL (for macs install the PostgreSQL app [HERE](https://postgresapp.com/) )
2) Install Python 
3) Install Pipenv `pip install pipenv`  
4) Create a Virtual Environment `pipenv install --python "$PYENV_ROOT/versions/<<version_you_installed_above>>/bin/python"`
5) Install all the dependencies for the Python App `npm install`
6) Create .env file 
```
FLASK_ENV=development
SECRET_KEY=<insert-secret-key-here>
DATABASE_URL=postgresql://repofolio:<insert-database-password-here>@localhost/repofolio
```    
7) Create .flaskenv file `FLASK_APP=repofolio.py`    


### Run the App Locally
1) Create the PostgreSQL database:
cd into the 'repofolio' directory   
```psql```    
```DROP DATABASE repofolio;```    
```DROP USER repofolio;```    
```CREATE USER repofolio WITH PASSWORD '<insert-password-here>';```    
```CREATE DATABASE repofolio WITH OWNER repofolio;```    
you should see output showing that the user & database were created

2) Seed the database: 
```\q``` to exist out of psql
```python database.py``` to seed the database 
```psql```
```SELECT * FROM repos;``` to confirm the data was seeded successfully 
```\q``` to exit out of psql

3) Start the server: 
```pipenv run flask run```
Then click on the link that says something like "Running on http://"...

4) If prompted to log into Github, follow the prompts

## Customizations 
Go to the `customizations` directory and follow all of the instructions where it says **'TODO'**:
1. `added_props_for_existing_repos.py` - optionally add videos, thumbnails, priority rankings, and a highlighted boolean for each repo
2. `customizable_constants.py` - add your profile pic, resume, Github username & LinkedIn username
3. `filters.py` - choose which [topics](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/classifying-your-repository-with-topics) you want your viewers to be able to filter by 
4. `projects_without_repos.py` - optionally add projects without repos 
5. In the `templates` folder, find `home.html` and add a summary about yourself
