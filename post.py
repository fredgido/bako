import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Posts(Base):
    __tablename__ = 'posts'
    post_id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    post_hash = sqlalchemy.Column(sqlalchemy.String)
    file_name = sqlalchemy.Column(sqlalchemy.String)
    date = sqlalchemy.Column(sqlalchemy.String)
    source_url = sqlalchemy.Column(sqlalchemy.String)
    source_info = sqlalchemy.Column(sqlalchemy.String)
    tags = sqlalchemy.Column(sqlalchemy.String)
    def __repr__(self):
        return "<Post(post_id='%s', file_name='%s')>" % (self.post_id, self.file_name)
