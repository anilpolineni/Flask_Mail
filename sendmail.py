import os
from flask_mail import Mail, Message
from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import FileField, StringField, validators
app = Flask(__name__)
import os
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY
app.config.update(
	DEBUG=True,
	#EMAIL SETTINGS
	MAIL_SERVER='smtp.gmail.com',
	MAIL_PORT=465,
	MAIL_USE_SSL=True,
	MAIL_USERNAME = 'anilpolineni008@gmail.com',
	MAIL_PASSWORD = 'anil@1234'
	)
mail = Mail(app)

class FileForm(FlaskForm):
    file_ = FileField('Some file')
    addr = StringField('Address', [validators.InputRequired()])

@app.route('/',methods=["POST","GET"])
def send_mail():
	form = FileForm()
	if request.method=="POST":
		try:
			to = request.form["to"]
			subject = request.form["subject"]
			message = request.form["message"]
			print("\n\n\n\n",to,subject,message)
			# image = request.files['file']
			# print("file\n\n\n\n",image)
			msg = Message(subject,
			  sender="noreply@testing@gmail.com",
			  recipients=[to])
			msg.body = message
			# with app.open_resource("download.jpg") as fp:
			msg.attach(form.file_.data.filename,
            'application/octect-stream',
            form.file_.data.read())
			print("\n\n\n",msg)    
			mail.send(msg)
			return ' Successfully Mail sent!'
		except Exception as e:
			return(str(e)) 
	else:
		return render_template("index.html", form=FileForm())

if __name__ == '__main__':
    app.run(host='', port=5000)
