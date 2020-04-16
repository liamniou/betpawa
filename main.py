from flask import Flask, render_template, flash, request

app = Flask(__name__)


@app.route("/")
def root():
    return 'Success!'


@app.route("/ping")
def ping():
    return 'Ok'


if __name__ == "__main__":
    app.run(host='0.0.0.0')
