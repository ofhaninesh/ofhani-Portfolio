import email
from email.mime import message
from flask import Flask, render_template,request
from flask_mail import Mail, Message

from dotenv import dotenv_values


app = Flask(__name__)


app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 465
app.config["MAIL_USERNAME"] = "ofhaninetshi12@gmail.com"

config = dotenv_values(".env")
app.config["MAIL_PASSWORD"] = config.get("EMAIL_PASSWORD")


app.config["MAIL_USE_SSL"] = True
app.config["MAIL_USE_TLS"] = False
mail = Mail(app)



# @app.route("/home",methods=['GET',"POST"])
# @app.route("/",methods=['GET',"POST"])
# def home():
#     if request.method == 'POST':
#         email = request.form['email']
        
#         msg = Message("Hello",sender="onetshim021@student.wethinkcode.co.za",recipients=[email])
         
#         msg.body = "This is a test"
#         mail.send(msg)
#         # return "messages sent!"  
#     return render_template('index.html',home='Success')
@app.route("/home",methods=['GET',"POST"])
@app.route("/",methods=['GET',"POST"])
def home():
    if request.method == 'POST':
        
        email = request.form['email']
        subject = request.form['subject']
        messsage = request.form['message']
        
        msg = Message(subject,sender=email,recipients=["ofhaninetshi12@gmail.com"])
         
        msg.body = messsage
        mail.send(msg)
        # return "messages sent!"  
    return render_template('index.html',home='Success')
# @app.route("/")
# def index():
#     msg = Message(
#         "Hello",
#         sender="onetshim021@student.wethinkcode.co.za",
#         recipients=["onetshim021@student.wethinkcode.co.za"],
#     )
#     msg.body = "This is a test"
#     mail.send(msg)
#     return "messages sent!"


if __name__ == "__main__":
    app.run(debug=True)
