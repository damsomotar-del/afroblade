from flask import Flask, request, redirect

app = Flask(__name__)

users = []
messages = []

@app.route("/")
def home():
    return """
    <h1>🔥 AfroBlade Official</h1>
    <p>Bienvenue sur AfroBlade.</p>
    <a href='/register'>Créer un compte</a><br>
    <a href='/login'>Connexion</a><br>
    <a href='/contact'>Contact</a>
    """

@app.route("/register", methods=["GET","POST"])
def register():
    if request.method == "POST":
        users.append({
            "user": request.form["user"],
            "pass": request.form["pass"]
        })
        return "<h2>Compte créé !</h2><a href='/login'>Se connecter</a>"
    return """
    <h2>Créer un compte</h2>
    <form method='POST'>
    Nom : <input name='user'><br>
    Mot de passe : <input name='pass' type='password'><br>
    <button>Créer</button>
    </form>
    """

@app.route("/login", methods=["GET","POST"])
def login():
    if request.method == "POST":
        for u in users:
            if u["user"]==request.form["user"] and u["pass"]==request.form["pass"]:
                return redirect("/chat")
        return "Erreur de connexion"
    return """
    <h2>Connexion</h2>
    <form method='POST'>
    Nom : <input name='user'><br>
    Mot de passe : <input name='pass' type='password'><br>
    <button>Se connecter</button>
    </form>
    """

@app.route("/chat", methods=["GET","POST"])
def chat():
    if request.method=="POST":
        messages.append(request.form["msg"])
    return """
    <h2>Chat AfroBlade</h2>
    <form method='POST'>
    <input name='msg' placeholder='Ton message'>
    <button>Envoyer</button>
    </form>
    <br>""" + "<br>".join(messages)

@app.route("/contact")
def contact():
    return "<h2>Contact : afroblade@gmail.com</h2>"

app.run(host="0.0.0.0", port=3000)
