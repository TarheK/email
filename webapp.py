import os
from flask import Flask, url_for, render_template, request
from flask import redirect
from flask import session

app = Flask(__name__)

app.secret_key=os.environ["SECRET_KEY"];   

@app.route('/', methods=["POST","GET"])
def renderStore():
    if "emailsbeingsent" not in session or "clear" in request.args:
        session["emailsincart"] = 0
        print("skrt")
        session["email_a"] = 0
        session["email_b"] = 0
        session["email_c"] = 0
        
        
    return render_template("store.html",emailsbeingsent=session["emailsbeingsent"])
    

@app.route('/addToCart',methods=["POST","GET"])
def renderAddToCart():
    session["emailsbeingsent"] += 1
    if request.args["email"]=="a":
        session["email_a"] += 1
    
    elif request.args["email"]=="b":
        session["email_b"] += 1
        
    elif request.args["email"]=="c":
        session["email_c"] += 1
    return render_template("addToCart.html", item_name = "Email " + str(request.args["email"]))
    
@app.route('/checkout',methods=["POST","GET"])
def renderCheckout():
    if "emailsbeingsent" not in session:
        return redirect(url_for("renderStore"))
    return render_template("checkout.html",itzemsincart=session["emailsbeingsent"])

@app.route('/bought',methods=["POST","GET"])
def renderBought():
    if "emailsbeingsent" not in session:
        return redirect(url_for("renderStore"))
    items = session["emailsbeingsent"]
    session["emailsbeingsent"] = 0
    return render_template("bought.html",emailsbeingsent=str(emails))
    
if __name__=="__main__":
    app.run(debug=True)
