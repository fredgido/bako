import json
import os

from post import *

import sqlalchemy
from sqlalchemy.orm import sessionmaker

engine = sqlalchemy.create_engine('sqlite:///posts.sqlite',
                                  connect_args={'check_same_thread': False} )#, echo=True)

if not os.path.exists('posts.sqlite'):
    Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

def isempty():
    return len(session.query(Posts).all()) == 0

def addpixiv(jsonfile):
    with open('static/pixiv/'+jsonfile+ ".json") as json_file:
        data = json.load(json_file)
        newpost = Posts()
        newpost.post_hash = "not yet"
        newpost.file_name = data["body"]["urls"]["original"].split('/')[-1]
        session.add(newpost)