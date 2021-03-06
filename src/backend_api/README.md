# Commands

    export FLASK_DEBUG=TRUE
    export FLASK_APP=app.py

    flask run

To initialize the database:

    flask initdb

# Endpoints

    /frontend/index.html = /index.html
    /frontent/* = /static/*
    /api/tickets/list = list of tickets
    /api/tickets/<n>/show = shows details of ticket, including its interactions
    /api/tickets/create POST = create new ticket, returns its ID
    /api/tickets/<n>/update POST = update a ticket
    /api/tickets/<n>/interactions/create POST = create a ticket

# Socket IO

    ticket-opened = when the ticket page is opened, call this event
    ticket-open = when the ticket page is open, call this event
    ticket-closed = when the ticket page is closed, call this event
    ticket-editing = when the user starts editing something, call this event
    ticket-changed = when the user has edited something, call this event

Clients receive events with fields msg, and send with id=`ticket_id` and `user_name` as their user name.

# Project Structure

The backend is in `app.py', the main SPA is in `templates/list.html`.
Other views (Contact, Agent Admin, Login) are also in that directory.

# Mail Connectivity

Set the `MAIL_PORT` environement variable to connect to a local open SMTP server.
Requires `flask-mai;`.

# `venv` setup

The code requires Python 3.

    python3 -m venv env
    . env/bin/activate
    pip install -r requirements.txt
