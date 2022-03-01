
from datetime import datetime
import sqlite3
DATABASE_PATH = "src/database/items.db"

def create_tables():
    db = sqlite3.connect(DATABASE_PATH)
    cursor = db.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS 'item' (id INTEGER PRIMARY KEY, created DATETIME NOT NULL, date DATE NOT NULL, title TEXT NOT NULL, description TEXT, done BOOLEAN DEFAULT(FALSE));")
    db.commit()
    db.close()


def select_items(day=None):
    db = sqlite3.connect(DATABASE_PATH)
    cursor = db.cursor()
    if day is None:
        cursor.execute("SELECT id, created, date, title, description, done FROM 'item';")
    else:
        cursor.execute("SELECT id, created, date, title, description, done FROM 'item' WHERE date = ?;", (day,))
    
    items = cursor.fetchall()
    db.close()
    return items


def insert_item(title, description, in_date):
    db = sqlite3.connect(DATABASE_PATH)
    cursor = db.cursor()
    cursor.execute("INSERT INTO 'item' (created, date, title, description) VALUES (?, ?, ?, ?);", (datetime.now(), in_date, title, description))
    db.commit()
    db.close()
