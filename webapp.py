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
    print(session["data2"])
    return render_template("addToCart.html")
    
@app.route('/checkout',methods=["POST","GET"])
def renderCheckout():
    if "emailsincart" not in session:
        return redirect(url_for("renderStore"))
    return render_template("checkout.html",itzemsincart=session["emailsincart"])

@app.route('/bought',methods=["POST","GET"])
def renderBought():
    if "emailsbeingsent" not in session:
        return redirect(url_for("renderStore"))
    items = session["emailsincart"]
    session["emailsincart"] = 0
    return render_template("bought.html",emailsincart=str(emails))
    
if __name__=="__main__":
    app.run(debug=True)
