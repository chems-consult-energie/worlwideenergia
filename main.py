

import os
from dotenv import load_dotenv

load_dotenv()  # Charge le contenu du .env dans les variables d'environnement


from flask import Flask, render_template, request

from flask_mail import Mail, Message

energie_app = Flask(__name__)

# Configuration de Flask-Mail
energie_app.config['MAIL_SERVER'] = 'smtp.gmail.com'
energie_app.config['MAIL_PORT'] = 465
energie_app.config['MAIL_USE_SSL'] = True

energie_app.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME')
energie_app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD')


    # Expéditeur par défaut : variable MAIL_DEFAULT_SENDER sinon MAIL_USERNAME

default_sender_name = os.getenv("MAIL_SENDER_NAME", "Flask Mailer")
default_sender_addr = os.getenv("MAIL_DEFAULT_SENDER", os.getenv("MAIL_USERNAME"))
energie_app.config["MAIL_DEFAULT_SENDER"] = (default_sender_name, default_sender_addr)




mail = Mail(energie_app)






@energie_app.route("/")
def index():
    return render_template("index.html",pagetitle = "index.html")

@energie_app.route("/about")
def about():
    return render_template("about.html",pagetitle = "about.html")

@energie_app.route("/service")
def service():
    return render_template("service.html",pagetitle = "service.html")

@energie_app.route("/lireplus")
def lireplus():
    return render_template("lireplus.html",pagetitle = "lireplus.html")

@energie_app.route("/contact")
def contact():
    return render_template("contact.html",pagetitle = "contact.html")



@energie_app.route("/quote")
def quote():
    return render_template("quote.html",pagetitle = "quote.html")




    
@energie_app.route("/submit", methods=["POST"])
def submit():
        name = request.form.get("name", "").strip()
        email = request.form.get("email", "").strip()
        message = request.form.get("message", "").strip()

        recipient = os.getenv("CONTACT_RECIPIENT", os.getenv("MAIL_USERNAME"))
        if not recipient:
            return "Configuration invalide : CONTACT_RECIPIENT ou MAIL_USERNAME manquant."

        msg = Message(
            subject="Nouveau message via le formulaire",
            recipients=[recipient],
            body=f"Nom: {name}\nEmail: {email}\nMessage:\n{message}",
            reply_to=email if email else None,
        )
  
    

   
        try:
            mail.send(msg)
            return "Message envoyé avec succès !"
        except Exception as e:
            return f"Erreur lors de l'envoi : {e}"

          

# Objet WSGI pour Gunicorn


app = energie_app  # alias pratique pour `gunicorn energie_app:app`

if __name__ == "__main__":
    # Test local uniquement
    port = int(os.environ.get("PORT", 9000))
    energie_app.run(host="0.0.0.0", port=port, debug=True)

 

   





