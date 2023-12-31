from flask import Flask, render_template


def create_app() -> Flask:

    app = Flask(__name__)

    @app.route("/")
    def index() -> str:
        return render_template("index.html", content = "Hello world!")

    return app