import json
from datetime import datetime as dt
from flask import Flask, render_template,request

import requests


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
   with open("contact.txt","a") as file:
    file.write(str(contacts)+"\n")

    return "<h1>FORM SUBMITTED</h1>"




if __name__=="__main__":
    app.run(debug=True)
