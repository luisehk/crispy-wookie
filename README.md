# crispy wookie
This app is an effort to automatize my daily tasks such manage my budget, pay the rent, remind me to do stuff like exercise or send some email, keep an eye on my exercise routine and diet, show me only relevant stuff from social media, alert me when I receive an important email, wake me up in the morning, brew me some coffee, send me a photo when someone knocks my door and I'm not home, etc. You get the idea.

This project is built for my own personal use so it may not fit everyone's workflow, but the code is open so you can fork it or submit a pull request.

### Why?
I know there are a lot of apps out there for this, but I want everything in one single place instead of using 30 different apps. I will also use this project to learn Docker, React, Swift and Unit Testing.

### Installation
To install the Python dependencies just run:

    make install

### Running the app
The app consists on multiple processes: gunicorn to run the Django app, the simple http server for the web front-end and celery for the message queue. To run them on the same time I use [Foreman](https://github.com/ddollar/foreman) (you will need Ruby for that):

    gem install foreman

If you want to override some setting from your settings.py file, Foreman will read the .env fileon your root directory and send them to Django as environmental variables. For example:

    DATABASE_URL=sqlite:/db.sqlite3
	SECRET_KEY=i5o@y&|@2!"·&|(g3tb5u#c^3@(tz6^pci=e
	TIME_ZONE=America/Monterrey

If you don't want to use Foreman, you can run the processes found on the Procfile manually. Make sure you configure your app through environmental variables with the following command:

    export DATABASE_URL=sqlite:/db.sqlite3

Now, start the app:

    make run

For first time use, you need to run the Django migrations:

    make migrate

### Unit testing
Just run the following command:

    make test

### Status
In development

