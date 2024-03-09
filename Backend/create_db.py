import sqlite3

conn = sqlite3.connect('entities.db')
cursor = conn.cursor()

command1 = 'create table entity (id Integer Primary Key, Entity_Name text, ImagePath text)'
cursor.execute(command1)

conn.commit()
