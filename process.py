from models import *
from tweets import *
import datetime


def injest_data(engine):
    tweets_detail.__table__.create(bind=engine, checkfirst=True)
    df = fetch()
    insert_df(engine=engine, table="tweets_detail", df=df)
    print(f'Tweets extracted & injested at {datetime.datetime.now().strftime("%d:%m:%y %H:%M:%S")}')


if __name__ == '__main__':
    engine = connect_db()
    injest_data(engine)