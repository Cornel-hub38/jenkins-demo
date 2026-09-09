from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return "Hello from my Jenkins CI/CD demo application!, this is my demo to community rev from Cornel Earle test3 automate process"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
