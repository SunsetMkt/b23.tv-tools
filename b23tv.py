# https://github.com/Cesium01/b23tvGenerator
# https://github.com/willbe03/b23-remover-telegram-bot

import json
import random
import string
from urllib.parse import urlparse, urlunparse, parse_qs

import requests
from fake_useragent import UserAgent

ua = UserAgent()


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
    headers = {
        "user-agent": ua.random,
    }

    res = requests.post(api, data=data, headers=headers)
    res.raise_for_status()
    data = json.loads(res.content)
    if data["data"].__contains__("content"):
        return data["data"]["content"]
    else:
        return "Bilibili did not return a short url."


def access_b23_url_and_return_real_url(url):
    res = requests.head(url, allow_redirects=True)
    real_url = res.url
    parsed_url = urlparse(real_url)
    return (
        urlunparse((parsed_url.scheme, parsed_url.netloc, parsed_url.path, "", "", "")),
        real_url,
    )


if __name__ == "__main__":
    test_url = "https://www.bilibili.com/"
    short = get_b23of(test_url)
    print(short)
    long, original = access_b23_url_and_return_real_url(short)
    print(long)
