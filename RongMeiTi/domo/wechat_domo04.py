# articles.py
import html
import requests
import utils

from urllib.parse import urlsplit


class Articles(object):
    """文章信息"""

    def __init__(self,appmsg_token, cookie):
        # 具有时效性
        self.appmsg_token = appmsg_token

        self.headers = {
        "User-Agent": "Mozilla/5.0 AppleWebKit/537.36 (KHTML， like Gecko) Version/4.0Chrome/57.0.2987.132 MQQBrowser/6.2 Mobile",
        "Cookie": cookie
        }

        self.data = {"is_only_read": "1", "is_temp_url": "0", "appmsg_type": "9"}

    def read_like_nums(self, article_url):
        """获取数据"""
        appmsgstat = self.get_appmsgext(article_url)["appmsgstat"]
        return appmsgstat["read_num"], appmsgstat["old_like_num"], appmsgstat["like_num"]

    def get_params(self, article_url):
        """
        获取到文章url上的请求参数
        :param article_url: 文章 url
        :return:
        """
        # url转义处理
        article_url = html.unescape(article_url)
        """获取文章链接的参数"""
        url_params = utils.str_to_dict(urlsplit(article_url).query, "&", "=")
        return url_params

    def get_appmsgext(self,article_url):
        """
        请求阅读数
        :param article_url: 文章 url
        :return:
        """
        url_params = self.get_params(article_url)

        appmsgext_url = "https://mp.weixin.qq.com/mp/getappmsgext?appmsg_token={}&x5=0".format(self.appmsg_token)
        self.data.update(url_params)

        appmsgext_json = requests.post(
            appmsgext_url, headers = self.headers, data = self.data).json()

        if "appmsgstat" not in appmsgext_json.keys():
            raise Exception(appmsgext_json)
        else:
            return appmsgext_json

if __name__ == '__main__':
    info = Articles('1151_SPQ6Ijiyr9GAfBcRgLKq8BYNTmy47lckSKbFdqm2qmkT6xwsxv3zd8g-vA9FiB6SUcEFjI8jsNRb8k1E', "rewardsn=; wxtokenkey=777; wxuin=3653668868; devicetype=Windows11x64; version=6305002e; lang=zh_CN; pass_ticket=sRqZhafJvja+g4eg/RzIOviezOqVnuBE0xuq/4k13FBJWuO7MIaJmZpOTC/9LXOm; appmsg_token=1151_XIHJfadtnYdfELr2OVjFBxR0NIqFWDkuwlV37pvlgd-6m2K8yravSjykFSwkmUyj__eXrjH0YWJ7F_DV; wap_sid2=CISgms4NEooBeV9IT2hfdFYxRk5GLTVIaW9INS1BLWRoVWsxdTJyNXR2Yk1XRDE3emRFNy00SVBNd2hFSUUyV0RZbjl0bTZ3NjV5NC1lQUJlWl9XLTR2SGZaekY2aXVfRDk4N3Fqb0ZtYWhhWUNfNmhxM3FaMTU5UFNLcEptSnVWQ1BaSmNYVEQ5empsMFNBQUF+MLuZgpAGOA1AAQ==")
    a = info.read_like_nums('https://mp.weixin.qq.com/s/P1Y2vr1Fyfa7tVbZw7ZcMA')
    print(a)