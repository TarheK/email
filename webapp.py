import os, datetime
from flask import Flask, url_for, render_template, request
from flask import redirect
from flask import session
from flask_mail import Mail,Message 

app = Flask(__name__)

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'ameliatarhekot@gmail.com'
app.config['MAIL_PASSWORD'] = os.environ["password"]
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

mail = Mail(app)

app.secret_key=os.environ["SECRET_KEY"];   

@app.route('/', methods=["POST","GET"])
def renderStore():
    var=datetime.datetime.now().strftime("%m, month, %d, day, %H, hour, %M, min")
    return render_template("store.html",VAR=var)
    
@app.route('/next1', methods=["POST","GET"])
def rendernext1():
    session["data1"]=request.form["name"]
    print(session["data1"])
    return render_template("sent.html")

@app.route('/next2',methods=["POST","GET"])
def rendernext2():
    session["data2"]=request.form["data"]
    print(request.form["data"])
    print(session["data2"])
    return render_template("addToCart.html")
    
@app.route('/next3',methods=["POST","GET"])
def rendernext3():
    session["data3"]=request.form["data"]
    print(request.form["data"])
    print(session["data3"])
    return render_template("checkout.html")

@app.route('/next4',methods=["POST","GET"])
def rendernext4():
    session["data4"]=request.form["data"]
    print(request.form["data"])
    print(session["data4"])
    return render_template("bought.html")
    
@app.route('/next5',methods=["POST","GET"])
def rendernext5():
    session["data5"]=request.form["data"]
    print(request.form["data"])
    print(session["data5"])
    
    attachData="data1,data2,data3,data4,data5\n\"%s\",\"%s\",\"%s\",\"%s\",\"%s\""%(session["data1"],session["data2"],session["data3"],session["data4"],session["data5"])
    
    msg = Message('Hello', sender = 'ameliatarhekot@gmail.com', recipients = ['ameliatarhekot@gmail.com'])
    msg.attach("data.csv","text/csv",attachData)
    
    mail.send(msg)
    
    return render_template("end.html")
    
    
    
if __name__=="__main__":
    app.run(debug=True)
