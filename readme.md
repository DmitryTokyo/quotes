# Micro Flask Application
This application shows a basic work of Flask framework and interaction with PostgreSQL. The interaction with database takes using SQLAlchemi. This project was deployed in the [Heroku server](https://dashboard.heroku.com/apps).

## Requirements
- Python 3.8.5
- PostgeSQL v.12

## Installation

#### On your local machine
1. Clone the repo
```bash
git clone https://github.com/DmitryTokyo/quotes.git
```
2. Create database and put in the `.env` file `DATABASE_URL` using a pattern: `dialect+driver://username:password@host:port/database`. Your can choose your prefer database. I used PostgreSQL - `postgresql://dmitriy:password@localhost:5432/quotes`.

3. Also  you need to set `SQLALCHEMY_TRACK_MODIFICATIONS` and put it to `.env` either. This key can track modifications of object if you need it. For more information about configuration keys can read [here](https://flask-sqlalchemy.palletsprojects.com/en/2.x/config/).

4. Use a virtual environments to manage your dependencies. In Lilnux or mac os you can use this command:
```bash
python3 -m venv venv
```

5. All dependencies can install through `requirements.txt` by following command:
```bash
pip install -r requirements.txt
```

## Usage
For start application needs to tell your terminal the application to work with by exporting the FLASK_APP.

```bash
$ export FLASK_APP=quotes.py
```

Also you can set debug mode by exporting the FLASK_ENV. If you need to activate debug mode use:

```bash
$ export FLASK_ENV=development
```
Or you can create `.flaskenv` and put these variables.
Launch you application `flask run` and head over to `http://127.0.0.1:5000/`.

This application was deployed to [heroku server](https://dashboard.heroku.com/apps). You can try [to use it](https://quote-flask.herokuapp.com/).

Application example:

![screenshot](static/img/Screenshot.quotes.png)

## License
This project is licensed under [MIT](https://opensource.org/licenses/MIT) license.