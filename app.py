from flask import Flask, render_template, request, redirect, url_for
from flask_mail import Mail, Message
from dotenv import load_dotenv
load_dotenv()
import os

app = Flask(__name__)

# Flask-Mail configuration
app.config['MAIL_SERVER'] = 'smtp.example.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.environ.get('username')
app.config['MAIL_PASSWORD'] = os.environ.get('password')

mail = Mail(app)

# Landing page
@app.route('/')
def index():
    return render_template('index.html')

# Route to handle form submission
@app.route('/submit_form', methods=['POST'])
def submit_form():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']

        # Sending email
        msg = Message('New Form Submission',
                      sender=os.environ.get('username'),
                      recipients=[os.environ.get('username')])
        msg.body = f"Name: {name}\nEmail: {email}\nMessage: {message}"
        mail.send(msg)

        return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
