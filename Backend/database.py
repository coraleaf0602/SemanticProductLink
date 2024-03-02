import sqlite3

#Creates new database if one with the same name doesn't already exist
def create_table():
    conn = sqlite3.connect('test.db')
    cur = conn.cursor()

    sql = '''
        CREATE TABLE IF NOT EXISTS TestTable (
        name TEXT PRIMARY KEY,
        url TEXT NOT NULL,
        image_path TEXT NOT NULL,
        description TEXT NOT NULL
        )
    '''
    cur.execute(sql)
    conn.commit()
    conn.close()

#Function to insert a row into the database
def insert(name, url, image_path, description):
    conn = sqlite3.connect('test.db')
    cur = conn.cursor()
    cur.execute('''INSERT OR REPLACE INTO TestTable (name, url, image_path, description)
                VALUES (?, ?, ?, ?)''', (name, url, image_path, description))
    conn.commit()
    conn.close()

# Retrieve a row from the database
def retrieve(name):
    conn = sqlite3.connect('test.db')
    cur = conn.cursor()
    cur.execute('''SELECT * FROM TestTable WHERE name = ?''', (name,))
    row = cur.fetchone()
    conn.close()
    return row


create_table()

insert("Laptop", "https://examplelaptop.com", "/path/to/image.jpg", "this is a laptop")
insert("Monitor", "https://examplemonitor.com", "/path/to/image2.jpg", "this is a monitor")
insert("Adapter", "https://exampleadapter.com", "/path/to/image3.jpg", "this is an adapter")


TestTable = retrieve("Adapter")
for entity in TestTable:
    print(entity)