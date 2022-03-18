from process import *


engine = connect_db()
injest_data()

print(pd.read_sql_table('tweets_detail', engine))


