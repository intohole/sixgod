#coding=utf-8
#!/usr/bin/env python





from vampire.htmlextract import HtmlExtract
from vampire.utils import network



if __name__== '__main__':
	html = network.get_html_string('http://i.ifeng.com/news/sharenews.f?aid=80121810')
	ex = HtmlExtract()
	print ex.get_text(html)




