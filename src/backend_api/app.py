import os
from sqlite3 import dbapi2 as sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash, jsonify
import flask
from flask_socketio import SocketIO, emit
import json

SQL_SCHEMA = '''
drop table if exists tickets;
create table tickets (
  id integer primary key autoincrement,
  title text not null,
  state text not null,
  created_at text not null,
  last_updated text not null,
  created_by text not null,
  tags text not null
);
drop table if exists interactions;
create table interactions (
  id integer primary key autoincrement,
  ticket_id integer not null,
  sender text not null,
  receiver text not null,
  date text not null,
  content text not null,
  type text not null
);
drop table if exists agents;
create table agents (
  id integer primary key autoincrement
);
'''

# TODO: User management
# TODO: 


# create our little application :)
app = Flask(__name__)
socketio = SocketIO(app)

def connect_db():
    """Connects to the specific database."""
    # TODO: Configuration
    rv = sqlite3.connect('the.db')
    rv.row_factory = sqlite3.Row
    return rv


def init_db():
    """Initializes the database."""
    db = get_db()
    db.cursor().executescript(SQL_SCHEMA)
    db.commit()

def add_mock_data():
    db = get_db()
    db.execute('insert into tickets (title, state, created_at, last_updated, created_by, tags) VALUES (?, ?, ?, ?, ?, ?)', ['Test Ticket', 'OPEN', '2018-01-01 01:22:11', '2018-01-01 02:02:02', 'Monika Mueller', '#complaint'])
    db.commit()
  

@app.cli.command('initdb')
def initdb_command():
    """Creates the database tables."""
    init_db()
    add_mock_data()
    print('Initialized the database.')


def get_db():
    """Opens a new database connection if there is none yet for the
    current application context.
    """
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = connect_db()
    return g.sqlite_db


@app.teardown_appcontext
def close_db(error):
    """Closes the database again at the end of the request."""
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()

@app.route('/static/<path:path>')
def send_static(path):
    return flask.send_from_directory('../frontend', path)

@app.route('/')
def show_spa():
    return flask.send_from_directory('../frontend', 'index.html')

# TODO: Allow sorting, filtering and pagination
@app.route('/api/tickets/list')
def list_tickets():
    db = get_db()
    cur = db.execute('select * from tickets')
    tickets = list(map(dict, cur.fetchall()))
    return jsonify(tickets)

@app.route('/api/tickets/create', methods=['POST'])
def create_ticket():
    db = get_db()
    return json.dump({'result': 'failed'})