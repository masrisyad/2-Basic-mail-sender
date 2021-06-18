from flask import Flask
from flask_mail import Mail, Message
# Import eMail dan pesan dari modul flask-mail kedalam kodingan.

app = Flask(__name__)
mail = Mail(app)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'namaemailkamu@gmail.com'
app.config['MAIL_PASSWORD'] = '*****'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)
# konfigurasi parameter server


@app.route("/")
def index():
    msg = Message('Halo', sender='namaemailkamu@gmail.com',
                  recipients=['namaemailyangdikirim@gmail.com'])
    msg.body = "Hello Flask message sent from Flask-Mail"
    mail.send(msg)
    return "Sent"


if __name__ == '__main__':
    app.run(debug=True)
