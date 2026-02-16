import os
from flask import Flask
from redis import Redis

app = Flask(__name__)
redis_host = os.environ.get('REDIS_HOST', 'redis')
redis = Redis(host=redis_host,port=6379)

welcome_msg = os.environ.get('WELCOME_MESSAGE', 'Default Welcome!')
api_key = os.environ.get('API_KEY','No key found!')

@app.route('/')
def hello():
    try:
        count = redis.incr('hits')
    except Exception as e:
        count = "Could not connect to redis!"

    return f"""
    <h1>{welcome_msg}</h1>
    <p>Redis count = <strong>{count}</strong></p>
    <p>API Key = {api_key} (JUST TO TEST, WILL NOT SHOW IRL)</p>
    """

if __name__ == "__main__":
    app.run(host='0.0.0.0', port = 5000, debug = True)