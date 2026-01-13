from flask import Flask
import redis
import os

app = Flask(__name__)
redis_host = os.getenv("REDIS_HOST", "redis")
r = redis.Redis(host=redis_host, port=6379, decode_responses=True)

@app.route("/")
def result():
    aws = r.get("AWS") or 0
    azure = r.get("Azure") or 0
    return f"<h2>Results</h2>AWS: {aws}<br>Azure: {azure}"

app.run(host="0.0.0.0", port=80)

