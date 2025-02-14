from datetime import datetime as dt
from flask import Flask, render_template, request, send_from_directory
import os,requests
from smtplib import  SMTP

response=requests.get("https://api.npoint.io/d4656264c8ac08d072a5")

res=response.json()


today=dt.now().date()

app=Flask(__name__)

@app.route("/")
def home():
    
    return render_template("index.html",post=res, date=today)


@app.route("/<page>")
def pages(page):

    return render_template(f"{page}")


@app.route("/<int:index>")
def post(index):
    post_no=res[index-1]
    return  render_template("post.html",post=post_no, date=today, bg_img=post_no["image_url"])

@app.route("/submit",methods=['POST','GET'])
def contact():
   contacts={}
   if request.method=="POST":
       contacts={
           "name": request.form["NAME"],
           "e-mail":request.form["EMAIL"],
           "phone_number":request.form["PHONE_NUMBER"],
           "message":request.form["MSG"]
       }
   sender_email = "dbmurali1507@gmail.com"
   app_pass = os.environ.get("APP_PASSWORD")
   to_mail="areadb15@gmail.com"
   viewer_email=contacts["e-mail"]
   viewer_name=contacts["name"]
   viewer_phone=contacts["phone_number"]
   viewer_msg=contacts["message"]

   server=SMTP("smtp.gmail.com", 587)
   server.starttls()
   server.login(user=sender_email,password=app_pass)

   server.sendmail(from_addr= sender_email,to_addrs=to_mail,msg=f"Subject:Message From {viewer_name} (my_blog)\n\n{viewer_msg}\n\n\n Contact details:\n e-mail: {viewer_email}\n contact number: {viewer_phone}")
   print("Mail send")

   return "<h1>FORM SUBMITTED</h1>"




if __name__=="__main__":
    app.run(debug=True)
