#coding=utf-8


import urllib2
import urllib
import json
import random
import time
import re


code = {"gbk":"gbk",\
        "utf-8":"utf-8",
        "gb2312":"gb2312"}


_jload = json.loads
_urlencode = urllib.urlencode
lang_detect = re.compile("charset=([\w\d-]+)" ,  re.IGNORECASE)


class UtilException(Exception):
    
    
    def __init__(self , msg , code = None):
        self.msg = msg 
        self.code = code 
    
    def __str__(self):
        if code:
            return "%s,%s" % ( self.msg , self.code)
        else:
            return self.msg

class NoDataReturn(UtilException):
    pass



class HtmlExtractException(UtilException):
    pass

class NoResponseException(UtilException):
    pass


def get_url_reponse(baseurl , data = None ,header = {}):
    _response = None
    req = urllib2.Request(baseurl)
    if header and isinstance(header, dict):
        for _key,_val in header.items():
            req.add_header(_key, _val)
    if data:
        if isinstance(data, dict):
            data = urllib.urlencode(data)
        _response = urllib2.urlopen(req,data)
    else:
        _response = urllib2.urlopen(req)
    return _response

def get_html_string(baseurl , data = None ,header = {}):
    _response = get_url_reponse(baseurl , data ,header)
    if _response:
        _html = _response.read()
        _code = lang_detect.search(_html)
        _codeing = "gb2312"
        if _code:
            _codeing = _code.group()
            _codeing = _codeing[8:]
#             _codeing = _code.split("charset=")[1].split("\"")[0]
        if _codeing and _codeing.strip() != "":
            _html = _html.decode(_codeing,"ignore")
        return _html
    raise NoDataReturn,baseurl
    


def _get_url_data(baseurl , data = None ,header = {}, codemode = "gbk"):
    _response = get_url_reponse(baseurl , data ,header)
    if _response:
        return _response.read().decode(codemode,'ignore')
    else:
        raise NoResponseException,baseurl

def get_url_string(url , data = None):
    return  get_url_reponse(url).read()
    
    
def get_url_data(url , data = None,codemode = "gbk"):
    header = {}
    header["User-Agent"] =  "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/28.0.1500.71 Chrome/28.0.1500.71 Safari/537.36"
    header["content-type"] = "application/x-www-form-urlencoded" 
    return _get_url_data(url , data=data , header=header , codemode=codemode)
 
 
'''
功能：
    从一个含有json字符串中，提取json字符串（jsonp({"1":2})）
返回：
   
原理：
    
'''
def get_url_html_string(base_url ,  query  = None , data = None ,code="utf-8"):
    if query:
        url = queryurl(base_url, query)
    else:
        url = base_url
    return get_url_data(url,codemode = code , data= data)



def jsonstrtodict(jsonstr):
    datadict = None
    try:
        datadict = _jload(jsonstr)
    except Exception,e:
        raise  UtilException("JSON_DECODE_ERRO_%s" % e , 102)
    return datadict

def queryurl(baseurl,querydict):
    return "%s%s" % (baseurl,_urlencode(querydict))

'''
函数名称： randint
函数功能： 随机生成n位随机数
参数列表：
       n 随机生成的位数
返回值：
       整数型
'''
def randint(n):
    _num = 1
    if n > 1:
        for _ in range(n - 1):
            _num *= 10
    else:
        raise UtilException("NO_RIGHT_NUM",110)
    return random.randint(_num,(_num * 10) - 1)


def randintbyrang(_min,_max):
    if _min >= _max:
        raise UtilException("VALUE_IS_NOT_VALUE",113) 
    return random.randint(_min,_max)

def timems():
    return long(time.time()) * 1000


def getksTs():
    return "%s_%s" % (timems(),randint(4))

def getJsonp():
    return "jsonp%s" % (randint(4))

'''
功能：
    从一个含有json字符串中，提取json字符串（jsonp({"1":2})）
返回：
    json字符串 成功
    ValueError: substring not found 异常
原理：
    
'''
def getjson(data):
    return data[data.index("{"):data.rindex("}")+1]


def get_html_code(html):
    _code = lang_detect.search(html)
    if _code :
        return _code.group()[8:]
    else:
        return ''
    


if __name__ == "__main__":
    print get_html_string('http://world.haiwainet.cn/n/2013/1022/c232591-19831524.html')



