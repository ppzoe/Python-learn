# articles.py
import html
import requests
import utils

from urllib.parse import urlsplit


class Articles(object):
    """文章信息"""

    def __init__(self, appmsg_token, cookie):
        # 具有时效性
        self.appmsg_token = appmsg_token

        self.headers = {
            "User-Agent": "Mozilla/5.0 AppleWebKit/537.36 (KHTML， like Gecko) Version/4.0Chrome/57.0.2987.132 MQQBrowser/6.2 Mobile",
        "Cookie": cookie
        }

        self.data = {
            "is_only_read": "1",
        "is_temp_url": "0",
        "appmsg_type": "9",
        }

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

        appmsgext_url = "https://mp. weixin.qq.com/mp/getappmsgext?appmsg_token={}&x5=0".format(self.appmsg_token)
        self.data.update(url_params)

        appmsgext_json = requests.post(
            appmsgext_url, headers = self.headers, data = self.data).json()

        if "appmsgstat" not in appmsgext_json.keys():
            raise Exception(appmsgext_json)
        return appmsgext_json

if __name__ == '__main__':
    info = Articles(
        '1068_XQoMoGGBYG8Tf8k23jfdBr2H_LNekAAlDDUe2aG13TN2fer8xOSMyrLV6s-yWESt8qg5I2fJr1r9n5Y5', 'rewardsn=; wxtokenkey=777; wxuin=1681274216; devicetype=android-29; version=27001037; lang=zh_CN; pass_ticket=H9Osk2CMhrlH34mQ3w2PLv/RAVoiDxweAdyGh/Woa1qwGy2jGATJ6hhg7syTQ9nk; wap_sid2=COjq2KEGEnBPTHRVOHlYV2U4dnRqaWZqRXBqaWl3Xy1saXVWYllIVjAzdlM1VkNDNHgxeWpHOG9pckdkREMwTFEwYmNWMl9FZWtRU3pRRnhDS0pyV1BaZUVMWXN1ZWN0WnZ6aHFXdVBnbVhTY21BYnBSUXNCQUFBMLLAjfgFOA1AAQ==')
    a, b, c = info.read_like_nums(
        'https://mp.weixin.qq.com/s?__biz=MzA5MTcwMzEwNQ==&mid=2650654206&idx=1&sn=7d525b97b408dbd74b1be804a06502f1&chksm=887137d0bf06bec6e1c99512d910c1eef253a9665e6bc554b09623bf02301558cc0bc485232e&scene=126&sessionid=1642060122&key=f7f703924ac0da43818ad0a73b9d20')
    print(a, b, c)