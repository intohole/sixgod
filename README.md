sixgod pyton 网页正文提取
=====================================

思想
-------------------------
*  基于行块分布函数的通用网页正文抽取  
*  优势： 线性时间、不建DOM树、与HTML标签无关



:::python  
      
         from htmlextract import HtmlExtract  
         from util import *  


         h = HtmlExtract()  
         html = util.get_html_string("http://finance.jfinfo.com/news/20131022/00311378.shtml")  
         print h.get_text(html) #返回新闻正文提取