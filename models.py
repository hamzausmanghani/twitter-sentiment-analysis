from sqlalchemy import and_, create_engine, Column, Integer, DateTime, BigInteger, String, Sequence, Float, PrimaryKeyConstraint, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import database_exists, create_database
from sqlalchemy.ext.declarative import DeclarativeMeta
from utils import *
import json
Base = declarative_base()


class AlchemyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj.__class__, DeclarativeMeta):
            # an SQLAlchemy class
            fields = {}
            for field in [x for x in dir(obj) if not x.startswith('_') and x != 'metadata']:
                data = obj.__getattribute__(field)
                try:
                    json.dumps(data) # this will fail on non-encodable values, like other classes
                    fields[field] = data
                except TypeError:
                    fields[field] = None
            # a json-encodable dict
            return fields
        return json.JSONEncoder.default(self, obj)


def connect_db():
    url = f'postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}'
    if not database_exists(url):
        create_database(url)
    engine = create_engine(url, pool_size=50)
    return engine


class tweets_detail(Base):
    __tablename__ = "tweets_detail"
    id = Column(String, primary_key=True)
    author_id = Column(String)
    text = Column(String)
    lang = Column(String)
    created_at = Column(DateTime)

    def serialize(self):
        return {"id": self.id,
                "author_id": self.author_id,
                "text": self.text,
                "lang": self.lang,
                "created_at": self.created_at}


def insert_df(engine, table, df):
    df.to_sql(table, con=engine, if_exists='append', index=False, method='multi')

