import wechatsogou # 导入库
ws_api = wechatsogou.WechatSogouAPI() # 初始化
# 可配置参数

name = '净月检察'

wechat = ws_api.search_gzh(name)
print(list(wechat))
w0 = ws_api.get_gzh_info(name)
print(w0)
name2 = "你好！警察节！致敬人民警察"

# w1 = ws_api.search_article(name)
# print(list(w1))

# w2 = ws_api.get_gzh_article_by_history(name)
# print(w2)