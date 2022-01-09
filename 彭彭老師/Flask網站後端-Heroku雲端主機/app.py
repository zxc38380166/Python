from flask import Flask
app = Flask(__name__)
@app.route("/")
def home():
    return "Hello Flask"

@app.route("tets")
def Test():
    return "This is Test"

if __name__=="__main__":
    app.run()