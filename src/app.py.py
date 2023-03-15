from flask import flask

app = flask(__name__)

@app.route("/")
def index():
    return "hello , world !"

    
if __name__== "__name__":
    app.run()



