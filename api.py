from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/apeiria")
def apeiria_page():
    return render_template('Apeiria.html')


@app.route("/honyaku")
def honyaku_page():
    return render_template('Honyaku.html')


@app.route("/jimonet")
def jimonet_page():
    return render_template('Jimonet.html')


@app.route("/deepunfolding")
def du_page():
    return render_template('DU.html')


if __name__ == "__main__":
    app.run()
