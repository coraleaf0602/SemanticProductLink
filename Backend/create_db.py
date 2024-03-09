import sqlite3

conn = sqlite3.connect('entities.db')
cursor = conn.cursor()

command1 = 'create table entity (Entity_Name text Primary Key, URL text, ImagePath text)'
cursor.execute(command1)

conn.commit()
