from process import *

if __name__ == '__main__':
    engine = connect_db()
    injest_data(engine)
