import sqlalchemy as sq
from sqlalchemy import ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

Base = declarative_base()


class User(Base):
    __tablename__ = 'vkinder'

    id = sq.Column(sq.Integer, primary_key=True)
    user_id = sq.Column(sq.Integer, unique=True, nullable=False)
    first_name = sq.Column(sq.String)
    last_name = sq.Column(sq.String)
    sex = sq.Column(sq.Integer)
    bdate = sq.Column(sq.String)
    city = sq.Column(sq.String)
    profile_link = sq.Column(sq.String)
    photo_urls = relationship('Photo')

    def __str__(self):
        self.profile_link = f"https://vk.com/id{self.user_id}"
        ss = f'{self.first_name} {self.last_name} {self.profile_link}'
        return ss

    def my_dict(self):
        my_dict = {'user_id': self.user_id,
                   'first_name': self.first_name,
                   'last_name': self.last_name,
                   'sex': self.sex,
                   'bdate': self.bdate,
                   'city': self.city
                   }
        return my_dict


class Photo(Base):
    __tablename__ = 'photo'

    id = sq.Column(sq.Integer, primary_key=True)
    user_id = sq.Column(sq.Integer, ForeignKey('vkinder.user_id'))
    url = sq.Column(sq.String, nullable=False)

    def __str__(self):
        return f"{self.url}"


def create_db(dsn):
    engine = sq.create_engine(dsn)
    session = sessionmaker(bind=engine)
    Base.metadata.create_all(bind=engine)
    return session


def clear_db(dsn):
    engine = sq.create_engine(dsn)
    connection = engine.connect()
    delete_list = ('photo', 'vkinder',)
    for entry in delete_list:
        query_string = f"""DELETE FROM {entry};"""
        connection.execute(query_string)
