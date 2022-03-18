from sqlalchemy import create_engine, Column, Integer, BigInteger, String, Sequence, Float, PrimaryKeyConstraint, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import database_exists, create_database
from utils import *
Base = declarative_base()


def connect_db():
    url = f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
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
    created_at = Column(String)


def insert_df(engine, table, df):
    df.to_sql(table, con=engine, if_exists='append', index=False, method='multi')

