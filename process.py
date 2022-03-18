from models import *
from tweets import *


def injest_data(engine):
    tweets_detail.__table__.create(bind=engine, checkfirst=True)
    df = fetch()
    insert_df(engine=engine, table="tweets_detail", df=df)