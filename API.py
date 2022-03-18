import flask
from flask import request
from models import *
import pandas as pd

app = flask.Flask(__name__)
app.config['debug'] = True


@app.route("/get_tweets", methods=['GET'])
def get_tweets():
    apiKey = request.headers.get("apiKey")
    if apiKey == my_api_key:
        engine = connect_db()
        df = pd.read_sql_table('tweets_detail', engine)
        records = df.to_json(orient="records")
        return records
    else:
        return 401, "UNAUTHORIZED"


if __name__ == '__main__':
    app.run(host=API_HOST, port=API_PORT)