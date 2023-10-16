# https://github.com/Cesium01/b23tvGenerator
# https://github.com/willbe03/b23-remover-telegram-bot

import json
import random
import string
from urllib.parse import urlparse

import requests


def get_b23of(long_url):
    """
    Notice:
        Only *.bilibili.com/* links are supported.
    """

    def random_buvid():
        return (
            "".join(random.choices(string.digits + string.ascii_letters, k=32))
            + "infoc"
        )

    api = "https://api.bilibili.com/x/share/click"
    data = {
        "build": str(random.randint(6000000, 9000000)),
        "buvid": random_buvid(),
        "oid": long_url,
        "platform": random.choice(["android", "ios"]),
        "share_channel": "COPY",
        "share_id": "public.webview.0.0.pv",
        "share_mode": str(random.randint(1, 10)),
    }

    try:
        res = requests.post(api, data=data)
        res.raise_for_status()
        data = json.loads(res.content)
        if data["data"].__contains__("content"):
            return data["data"]["content"]
        else:
            return "Not available"
    except:
        return "Not available"


def access_b23_url_and_return_real_url(url):
    try:
        res = requests.head(url, allow_redirects=True)
        real_url = res.url
        r = urlparse(real_url)
        return r.scheme + "://" + r.netloc + r.path
    except:
        return "Not available"


def generate_short_url_from_short_url(short_url):
    long_url = access_b23_url_and_return_real_url(short_url)
    return get_b23of(long_url)


if __name__ == "__main__":
    test_url = "https://www.bilibili.com/"
    short = get_b23of(test_url)
    print(short)
    long = access_b23_url_and_return_real_url(short)
    print(long)
