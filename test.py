#coding=utf-8




import util



html = util.get_url_data("http://www.chinanews.com/fz/2013/08-28/5213451.shtml")

for h in html.split("\n"):
    print h
    print "******************"