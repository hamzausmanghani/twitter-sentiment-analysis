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
    start = request.args.get("start")
    end = request.args.get("end")
    if (start is not None) and (end is not None):
        if apiKey == my_api_key:
            start += "T00:00:00.000Z"
            end += "T23:59:59.000Z"
            engine = connect_db()
            factory = sessionmaker(bind=engine)
            session = factory()
            result = session.query(tweets_detail).filter(
                     tweets_detail.created_at.between(start, end)
            ).all()
            return json.dumps(result, cls=AlchemyEncoder)
        else:
            return {"status": "UNAUTHORIZED"}, 401
    else:
        return {"status": "BAD REQUEST"}, 400


@app.route("/search_by", methods=['GET'])
def search_by():
    apiKey = request.headers.get("apiKey")
    if apiKey == my_api_key:
        tag = request.args.get("tag")
        start = request.args.get("start")
        end = request.args.get("end")
        if (tag is not None) and (start is not None) and (end is not None):
            start += "T00:00:00.000Z"
            end += "T23:59:59.000Z"
            engine = connect_db()
            factory = sessionmaker(bind=engine)
            session = factory()
            result = session.query(tweets_detail).filter(
                and_(tweets_detail.text.ilike(f'%{tag}%'),
                     tweets_detail.created_at.between(start, end))
            ).all().as_dict()
            response = jsonify({'status': "SUCCESSFUL",
                                'data': result)
            return response
        else:
            return {"status": "BAD REQUEST"}, 400
    else:
        return {"status": "UNAUTHORIZED"}, 401


if __name__ == '__main__':
    app.run(host=API_HOST, port=API_PORT)