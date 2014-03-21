sixgod pyton 网页正文提取
=====================================

思想
-------------------------
*  基于行块分布函数的通用网页正文抽取  
*  优势： 线性时间、不建DOM树、与HTML标签无关



:::python  
      
         from vampire.htmlextract import HtmlExtract  
         from vampire.utils import network  
         
         h = HtmlExtract()  
         html = network.get_html_string("http://finance.jfinfo.com/news/20131022/00311378.shtml")  
         print h.get_text(html) #返回新闻正文提取