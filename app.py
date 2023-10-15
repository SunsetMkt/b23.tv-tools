import flask

import b23tv

app = flask.Flask(__name__)


@app.route("/")
def index():
    return flask.render_template("index.html")


@app.route("/get")
def get():
    url = flask.request.args.get("url")
    return b23tv.get_b23of(url)


@app.route("/parse")
def parse():
    url = flask.request.args.get("url")
    return b23tv.access_b23_url_and_return_real_url(url)


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=18080, debug=True)
