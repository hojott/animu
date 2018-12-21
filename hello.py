from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hei Maailma!"

if __name__ == "__main__":
    app.run(debug=True)