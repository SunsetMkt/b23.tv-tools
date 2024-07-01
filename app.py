import flask

import b23tv

app = flask.Flask(__name__)


@app.route("/")
def index():
    return flask.render_template("index.html")


@app.route("/get")
def get():
    try:
        url = flask.request.args.get("url").strip()
        if not url.startswith("http"):
            url = "http://" + url
        return {"short": b23tv.get_b23of(url), "original": url}
    except:
        import traceback

        return {
            "msg": "服务器故障。",
            "original": url,
            "traceback": traceback.format_exc(),
        }


@app.route("/parse")
def parse():
    try:
        url = flask.request.args.get("url").strip()
        if not url.startswith("http"):
            url = "http://" + url
        cleaned, original = b23tv.access_b23_url_and_return_real_url(url)
        return {"cleaned": cleaned, "original": original}
    except:
        import traceback

        return {
            "msg": "输入的不是标准URL或服务器故障。",
            "original": original,
            "traceback": traceback.format_exc(),
        }


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=18080, debug=True)
