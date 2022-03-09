from flask import Flask, request, render_template
app = Flask(__name__)

from textblob import TextBlob

@app.route("/",methods=["GET","POST"])
def index():
    if request.method == "POST":
        text = request.form.get("text")
        print(text)
        r = TextBlob(text).sentiment
        return(render_template("index.html",result=r))
    else:
        return(render_template("index.html",result="2"))

if __name__ == "__main__":
    app.run()