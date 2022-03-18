from process import *

if __name__ == "main":
    engine = connect_db()
    injest_data(engine)
