
from flask import Flask, request, redirect

app = Flask(__name__)

users = []
messages = []

@app.route("/")
def home():
    return """
    <h1>AfroBlade</h1>
    <p>Bienvenue sur AfroBlade.</p>
    <a href='/register'>Créer un compte</a><br><br>
    <a href='/contact'>Contact</a>
    """

@app.route("/register", methods=["GET","POST"])
def register():
    if request.method == "POST":
        users.append({
            "name": request.form["name"],
            "email": request.form["email"],
            "password": request.form["password"]
        })
        return "<h2>Compte créé avec succès</h2><a href='/'>Retour</a>"
    return """
    <h2>Créer un compte</h2>
    <form method='POST'>
        <input name='name' placeholder='Nom'><br>
        <input name='email' placeholder='Email'><br>
        <input name='password' placeholder='Mot de passe' type='password'><br><br>
        <button>Créer</button>
    </form>
    """

@app.route("/contact", methods=["GET","POST"])
def contact():
    if request.method == "POST":
        messages.append({
            "name": request.form["name"],
            "msg": request.form["message"]
        })
        return "<h2>Message envoyé ✔️</h2><a href='/'>Retour</a>"
    return """
    <h2>Contact</h2>
    <form method='POST'>
        <input name='name' placeholder='Votre nom'><br>
        <textarea name='message' placeholder='Votre message'></textarea><br><br>
        <button>Envoyer</button>
    </form>
    """

app.run(host="0.0.0.0", port=8080)
