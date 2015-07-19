#coding=utf-8
#!/usr/bin/env python





from vampire.htmlextract import HtmlExtract
from vampire.utils import network
import requests


if __name__== '__main__':
	html = requests.get('http://i.ifeng.com/news/sharenews.f?aid=80121810')
	ex = HtmlExtract()
	print ex.get_text(html.text)




