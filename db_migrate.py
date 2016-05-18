from views import db
from config import DATABASE_PATH

import sqlite3
from datetime import datetime

with sqlite3.connect(DATABASE_PATH) as connection:
    c = connection.cursor()

    #move tasks table to new table
    c.execute("ALTER TABLE tasks RENAME TO old_tasks")

    #create tables again (makes new tasks table)
    db.create_all()

    #grab what was on the old table
    c.execute("SELECT name, due_date, priority, status FROM old_tasks ORDER BY task_id ASC")

    #save all the rows as a list of tuples; set posted_date to now and user_id to 1
    data = [(row[0], row[1], row[2], row[3], datetime.now(), 1) for row in c.fetchall()]

    #insert data to tasks table
    c.executemany("INSERT INTO tasks (name, due_date, priority, status, posted_date, user_id) VALUES (?, ?, ?, ?, ?, ?)", data)

    #delete the olds tasks table
    c.execute("DROP TABLE old_tasks")

