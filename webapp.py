import os
from flask import Flask, url_for, render_template, request
from flask import redirect
from flask import session

app = Flask(__name__)

app.secret_key=os.environ["SECRET_KEY"];   

@app.route('/', methods=["POST","GET"])
def renderStore():

    return render_template("store.html")
    
@app.route('/next1', methods=["POST","GET"])
def rendernext1():
    session["data1"]=request.form["data"]
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
    return render_template("end.html")
    
    
if __name__=="__main__":
    app.run(debug=True)
