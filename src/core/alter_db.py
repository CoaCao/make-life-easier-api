import sqlite3

conn = sqlite3.connect('data/make-life-easier.db')
cursor = conn.cursor()

try:
    cursor.execute("ALTER TABLE products ADD COLUMN is_used INTEGER DEFAULT 0")
    print("Add 'is_used' success.")
except sqlite3.OperationalError as e:
    if 'duplicate column name' in str(e).lower():
        print("'is_used' is exist.")
    else:
        print("Add 'is_used': ", e)

conn.commit()
conn.close()
