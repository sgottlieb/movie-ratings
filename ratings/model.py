from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, DateTime

Base = declarative_base()

### Class declarations go here
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key = True)
    email = Column(String(64), nullable = True)
    password = Column(String(64), nullable=True)
    age = Column(Integer, nullable=True)
    zipcode = Column(String(15), nullable=True)

    def __init__(self, age, zipcode, email = None, password = None):
        self.email = email
        self.password = password
        self.age = age
        self.zipcode = zipcode

class Movies(Base):
    __tablename__ = "movies"
    id = Column(Integer, primary_key = True)
    title = Column(String(64), nullable = True)
    release_date = Column(DateTime, nullable = True)
    video_date = Column(DateTime, nullable= True)
    imdb_url = Column(String(200), nullable = True)

    def __init__(self, title= None, release_date = None, video_date= None, imdb_url= None):
        self.title = title
        self.release_date = release_date
        self.video_date = video_date
        self.imdb_url = imdb_url

class Ratings(Base):
    __tablename__ = "ratings"
    id = Column(Integer, primary_key = True)
    movie_id = Column(Integer, nullable=True)
    rating = Column(Integer, nullable=True)
    timestamp = Column(DateTime, nullable= True)

    def __init__(self, movie_id= None, rating = None, timestamp = None):
        self.movie_id = movie_id
        self.rating = rating
        self.timestamp = timestamp

### End class declarations

def main():
    """In case we need this for something"""
    pass

if __name__ == "__main__":
    main()
