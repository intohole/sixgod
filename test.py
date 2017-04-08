#coding=utf-8
#!/usr/bin/env python





from vampire.htmlextract import HtmlExtract
import requests


if __name__== '__main__':
	html = requests.get('http://www.fabao365.com/fangchan/167193/')
        html.encoding="utf-8"
	ex = HtmlExtract()
	print ex.get_text(html.text)




