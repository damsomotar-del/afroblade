from flask import Flask, request, render_template_string
import random

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>AfroBlade</title>
    <style>
        body {font-family: Arial; background:#0f172a; color:white; text-align:center;}
        input,button{padding:10px;border-radius:6px;border:none;}
        button{background:#22c55e;color:black;font-weight:bold;}
        .box{background:#020617;padding:20px;margin:20px;border-radius:10px;}
    </style>
</head>
<body>
    <h1>AfroBlade Analytics</h1>
    <form method="POST">
        <input name="page" placeholder="Facebook Page Name" required>
        <button>ANALYSER</button>
    </form>
    {% if page %}
    <div class="box">
        <h2>{{page}}</h2>
        Followers: {{followers}}<br>
        Views: {{views}}<br>
        Est. Earnings: {{money}} $
    </div>
    {% endif %}
</body>
</html>
"""

@app.route("/", methods=["GET","POST"])
def home():
    page = None
    followers = views = money = 0
    if request.method == "POST":
        page = request.form["page"]
        followers = random.randint(1000,5000000)
        views = random.randint(5000,20000000)
        money = round(views * 0.001,2)
    return render_template_string(HTML, page=page, followers=followers, views=views, money=money)

app.run(host="0.0.0.0", port=8080
