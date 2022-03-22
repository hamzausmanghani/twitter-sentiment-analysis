import flask
from flask import request, jsonify
from models import *
import pandas as pd
import json

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
        return {"status": "UNAUTHORIZED"}, 401


@app.route("/search_by", methods=['GET'])
def search_by():
    apiKey = request.headers.get("apiKey")
    if apiKey == my_api_key:
        tag = request.args.get("tag")
        if tag is not None:
            engine = connect_db()
            factory = sessionmaker(bind=engine)
            session = factory()
            result = session.query(tweets_detail).filter(tweets_detail.text.ilike(f'%{tag}%')).all()
            return json.dumps(result, cls=AlchemyEncoder)
        else:
            return {"status": "BAD REQUEST"}, 400
    else:
        return {"status": "UNAUTHORIZED"}, 401


if __name__ == '__main__':
    app.run(host=API_HOST, port=API_PORT)