import sqlite3
import glob
import json

conn  = sqlite3.connect('posts.db')
c = conn.cursor() # The database will be saved in the location where your 'py' file is saved

c.execute('''CREATE TABLE IF NOT EXISTS PIXIV
             ([id] INTEGER PRIMARY KEY,[created_at] date, [user_id] integer, [image_url] text)''')


head = "INSERT INTO PIXIV (id,created_at,user_id,image_url) VALUES (?,?,?,?)"
val =[]

for jsonfile in glob.glob('*.json'):
        with open(jsonfile) as f:
            data = json.load(f)
            val.append((data["body"]["illustId"],data["body"]["createDate"].replace("T", " "),data["body"]["userId"],data["body"]["urls"]["original"]))


c.executemany(head,val)
conn.commit()
