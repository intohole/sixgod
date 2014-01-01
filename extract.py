#!/usr/bin/env python
# coding=utf-8


from BeautifulSoup import BeautifulSOAP
import sys
sys.path.append("./utils")

from pexceptions import NoDataParser
import network

class ExtractNewsInfo(object):

	 def __init__(self):
		 self.__soup = None

	 def parser(self , html):
	 	 self.clear()
	 	 self.__soup = BeautifulSOAP(html)


	 def get_tilte(self):
	 	 if self.__soup:
	 	 	return self.__soup.html.head.title.text
	 	 raise NoDataParser("没有调用解析")

	 def __get_mata(self ,  name):
	 	if self.__soup:
	 		__keywords = self.__soup.find('meta' , attrs= {'name': name})
	 	 	if __keywords:
	 	 		return __keywords['content']
	 	return None

	 def get_key_words(self):
	 	 return self.__get_mata( 'keywords')


	 def get_description(self):
	 	 return self.__get_mata('description') 
	 	 




	 def clear(self):
	 	 if self.__soup:
	 	 	self.__soup = None



if __name__ == '__main__':
	extract = ExtractNewsInfo()
	html = network.get_html_string("http://news.xinhuanet.com/politics/2013-12/31/c_118787397.htm")
	extract.parser(html)
	print extract.get_description()


