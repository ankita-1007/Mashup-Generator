from flask import Flask,request,render_template
from download import Download
from flask_wtf import FlaskForm
from wtforms import FileField,SubmitField
from werkzeug.utils import secure_filename
import os
import zipfile
import io
from email.message import EmailMessage
import ssl
import smtplib

app = Flask(__name__)
# app.config['UPLOAD_FOLDER']='static/files'

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/',methods=['GET','POST'])
def getValue():
  # data=request.form
  
  
  singer=request.form['singer']
  Number=request.form['number']
  Number=int(Number)
  duration=request.form['duration']
  email=request.form['mail']
 
  # f=request.files['filename']
  # f.save(os.path.join(os.path.abspath(os.path.dirname(__file__)),app.config['UPLOAD_FOLDER'], secure_filename(f.filename)))

  # file = "static/files/"+f.filename
  # print(singer)
  # print(Number)
  # print(duration)
  # print(email)
  # print(data)
  try:
   Download(singer,Number,duration)

  except:
   
    return render_template('error.html')

     
  # result.to_csv("static/files/result.csv",index=False)
  email_sender = 'ankitasharma967672@gmail.com'
  # 'ridhimagupta0212@gmail.com'
  email_password = 'luteqppisuwuikis'
  buffer = io.BytesIO()
  with zipfile.ZipFile(buffer, 'w') as myzip:
        myzip.write(f"static/{singer}/mashup.mp3", arcname="mashup.mp3")
  buffer.seek(0)

  with open(f"static/{singer}/mashup.zip", "wb") as f:
        f.write(buffer.read())
  
  em = EmailMessage()
  em['From'] = email_sender
  em['Subject'] = 'Your mashup'
  em.set_content("Here is your Mashup")
  with open(f"static/{singer}/mashup.zip","rb") as fp:
    file_data=fp.read()


  em.add_attachment(file_data,maintype='application',subtype='mp3',filename="mashup.zip")

  context = ssl.create_default_context()
  email_receiver =email
  em['To'] =email_receiver
  with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.send_message(em)



  


  




  return render_template('pass.html')
# @app.route('/dataset',methods=['GET','POST'])
# def dataset():
#   file=request.form['file']
#   data=[]
#   with open(file) as f:
#     csvfile=csv.reader(f)
#     for row in csvfile:
#       data.append(row)

#   print(data)

#   return render_template('dataset.html',dataset=data)
 
  

   

  

if __name__ == '__main__':
  app.run(debug=True)

