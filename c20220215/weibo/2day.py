import asyncio
import aiohttp
import pymysql
import requests
from datetime import datetime

wbid = {"吉林检察": "5093990523", "辽源西安检察": "5395116343", "公主岭检察": "5584068981"}

urls = [
    "https://weibo.com/ajax/statuses/mymblog?uid=5093990523", "https://weibo.com/ajax/statuses/mymblog?uid=5584068981",
    "https://weibo.com/ajax/statuses/mymblog?uid=5395116343",
]


async def aiodownload(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=headers) as wb:
            pass
              #  await 异步操作需要挂起 aiofiles


async def main():
    tasks = []
    for url in urls:
        tasks.append(aiodownload(url))
    await asyncio.wait(tasks)


if __name__ == '__main__':
    wb_data_list = []
    cookie = "SINAGLOBAL=9647412095234.6.1640246418846; UOR=www.baidu.com,weibo.com,www.baidu.com; SL_G_WPT_TO=zh; XSRF-TOKEN=gQuhF_75Ipqh5i-Laiw-MCZ6; SSOLoginState=1655426349; SL_GWPT_Show_Hide_tmp=1; SL_wptGlobTipTmp=1; _s_tentry=weibo.com; Apache=2841001404702.55.1655694166607; ULV=1655694166620:12:5:2:2841001404702.55.1655694166607:1655091898985; PC_TOKEN=4c215c9d42; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WF01YMUE2SQUse1CbGJT33q5JpX5KMhUgL.FozXeh2fSh.fSh-2dJLoI0qLxK-LBo.LBoeLxKqLBoMLBK2LxKBLBonLBoqLxK-L12qL1hnLxK-LBKqL1hzLxKBLB.BL1K-t; ALF=1687307360; SCF=AguY-Aj-Uaa6bVkTQCb9K5idnPXvJY2CmhVzApDg1Yb39oh4QsiT6AWVI0UWIKX5S6ibiZ_v5XRmatr7QglE1zg.; SUB=_2A25PtWCwDeRhGeRK61MU9CfJzzmIHXVsw9V4rDV8PUNbmtB-LVLRkW9NU3tst1lfMTVWwsOc-D0Gh-TqJSCDNwhJ; WBPSESS=fLtleuy1hZ_tMMSUlLky_guMBFx5g9XNCfQekiz42ZytU-PpQSiutZ1J6yxdxoR15af62BCJ_zTIIhhHc1i-7VnpaVIvsTq8LvA88bfNh0ype7lz3hD7vL3Ig0ese3pOKbr6qPG9EGFkE_Ouqkuhbw=="
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36',
        "cookie": cookie
    }
    asyncio.run(main())
