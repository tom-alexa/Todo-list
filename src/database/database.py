
import sqlite3
db = sqlite3.connect("src/database/items.db")


def create_tables():
    db.execute("CREATE TABLE IF NOT EXISTS 'item' (id INTEGER PRIMARY KEY, created DATETIME NOT NULL, date DATE NOT NULL, done BOOLEAN DEFAULT(FALSE));")
    db.commit()
    db.close()
