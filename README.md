cetweb
======

##Requirements

* Postgres (OSX: http://postgresapp.com/)

##Install

    $ virtualenv venv
    $ source venv/bin/activate
    $ pip install -r requirements.txt
    $ psql
      > create database cetweb;
    $ python cetweb/manage.py syncdb
    
##Run Server

    $ source venv/bin/activate
    $ python cetweb/manage.py runserver
    
Then go to localhost:8000 in your web browser.
