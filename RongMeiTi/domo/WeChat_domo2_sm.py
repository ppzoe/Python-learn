
count= 1

url_response = """
<script>
    setTimeout(function(){window.location.href='%s'}, 1700);
</script>
</html>
"""
# class TencentCloudPepline:
#     def __init__(self):
#         self.pool = PooledDB(pymysql,2,
#                              host="",
#                              user="root",
#                              passwd='root',
#                              db="",
#                              port=3306,
#                              setsession=['SET AUTOCOMMIT = 1']
#                              )
#         self.conn = self.pool.connection()
#         self.cursor = self.conn.cursor()
#         logger.info('connect success')
#
#     def select(self):
#         sql = 'select url from wechat_article order byid desc;'
#         self.cursor.execute(sql)
#         res = self.cursor.fetchall()
#         return res

# pepline_ = TencentCloudPepLine()
# url_list = list(pepline_.select())
url_list = [
    'https://mp.weixin.qq.com/s?__biz=MzA5MTcwMzEwNQ==&mid=2650654206&idx=1&sn=7d525b97b408dbd74b1be804a06502f1&chksm=887137d0bf06bec6e1c99512d910c1eef253a9665e6bc554b09623bf02301558cc0bc485232e&scene=126&sessionid=1642060122&key=f7f703924ac0da43818ad0a73b9d20'
    'https://mp.weixin.qq.com/s?__biz=MjM5NDg4OTEwMQ==&mid=21356451668772979&idx=1&sn=8d3038302a4d355f0da16fd4add6f261&chksm=bc6672918b11fb872be9d092ff609b61e47a87a66930abdc26a113dce9da0caab91514415db9&key=2049c8e06c26cfa5d9dc86f0c05003581a1410d8951805f4d3a1d5694e544'
]
def response(flow):
    start_url = flow.request.url
    if 'timestamp=' in start_url:
        permanent_url = flow.response.headers.get('location')
        print(flow.response.headers)
        print('permanent url : ', permanent_url)
    if 'biz=' in flow.request.url:
        url = url_list.pop()
        print(111111)
        # for i in flow.response.headers:
        #     print(i)
        #     print('==='*10)
        flow.response.headers.pop('content-security',None)
        flow.response.headers.pop('strict-transport-security',None)
        flow.response.headers['cache.cantrol'] = 'no-cache, no-store, must-revalidata'
        flow.response.text = flow.response.text.replace('</html>.url response % url')
"""
https://mp.weixin.qq.com/s?__biz=MjM5NDg4OTEwMQ==&mid=2668772979&idx=1&sn=8d3038302a4d355f0da16fd4add6f261&chksm=bc6672918b11fb872be9d092ff609b61e47a87a66930abdc26a113dce9da0caab91514415db9&key=2049c8e06c26cfa5d9dc86f0c05003581a1410d8951805f4d3a1d5694e544
"""
import collections
import random
from enum import Enum
import mitmproxy
from mitmproxy import ctx,http
from mitmproxy.exceptions import TlsProtocolException
from mitmproxy.proxy.protocol import TlsLayer, RawTCPLayer

# 下面的代码 用来绕过tls协议（证书错误导致）
class InterceptionResult(Enum):
    success = True
    failure = False
    skipped = None

# class _TlsStrategy:
#     def __init__(self):

