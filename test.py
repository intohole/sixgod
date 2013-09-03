#coding=utf-8




import util


import re
# python 正则 . 除换行符任意一个字符
clear_entre = re.compile("\n")
script_regx = re.compile("<script.*?>.*?</script>",re.IGNORECASE)
dto_regx = re.compile("<!DOCTYPE.*?>")
comment_regx = re.compile("<!--.*?-->")
style_regx = re.compile("<style.*?>.*?</style>")


html = util.get_url_data("http://news.gmw.cn/newspaper/2013-08/21/content_1987269.htm",codemode='utf-8')
x = clear_entre.sub("",html)
x = script_regx.sub("",x)
for h in x.split("\r"):
    print h
    print "******************"