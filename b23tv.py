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

    api = "http://api.bilibili.com/x/share/click"
    data = {
        "build": "6500300",
        "buvid": random_buvid(),
        "oid": long_url,
        "platform": "android",
        "share_channel": "COPY",
        "share_id": "public.webview.0.0.pv",
        "share_mode": "3",
    }
    res = requests.post(api, data=data)
    res.raise_for_status()
    data = json.loads(res.content)
    if data["data"].__contains__("content"):
        return data["data"]["content"]
    else:
        return "Not available"


def access_b23_url_and_return_real_url(url: str):
    res = requests.get(url, allow_redirects=True)
    real_url = res.url
    r = urlparse(real_url)
    return r.scheme + "://" + r.netloc + r.path
