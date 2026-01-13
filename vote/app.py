from flask import Flask, request, render_template_string
import redis
import os

app = Flask(__name__)
redis_host = os.getenv("REDIS_HOST", "redis")
r = redis.Redis(host=redis_host, port=6379, decode_responses=True)

HTML = """
<h2>Vote Your Favourite Cloud</h2>
<form method="POST">
  <input type="radio" name="vote" value="AWS"> AWS<br>
  <input type="radio" name="vote" value="Azure"> Azure<br><br>
  <input type="submit">
</form>
"""

@app.route("/", methods=["GET", "POST"])
def vote():
    if request.method == "POST":
        r.incr(request.form["vote"])
    return render_template_string(HTML)

app.run(host="0.0.0.0", port=80)

