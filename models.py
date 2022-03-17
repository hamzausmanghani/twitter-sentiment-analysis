from sqlalchemy import create_engine, Column, Integer, String, Sequence, Float,PrimaryKeyConstraint, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from utils import *
Base = declarative_base()


def connect_db():
    db = create_engine(f'postgresql://{DB_USER}:{DB_PASS}@{DB_IP}:{DB_PORT}/{DB_NAME}')
    return db


def insert_df(engine, table, df):
    df.to_sql(table, con=engine, if_exists='append', index=False, multi=True)


class tweets_detail(Base):
    __tablename__ = "tweets_detail"
    id = Column(Integer, primary_key=True)
    author_id = Column(Integer)
    text = Column(String)
    lang = Column(String)
    created_at = Column(String)
