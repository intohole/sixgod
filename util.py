#coding=utf-8


import urllib2
import urllib
from HtmlExtractException import HtmlExtractException
import json
import random
import time

code = {"gbk":"gbk",\
        "utf-8":"utf-8"}


_jload = json.loads
_urlencode = urllib.urlencode

def _get_url_reponse(baseurl , data = None ,header = {}):
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


def _get_url_data(baseurl , data = None ,header = {}, codemode = "gbk"):
    _response = _get_url_reponse(baseurl , data ,header)
    if _response:
        if not code.has_key(codemode):
            raise HtmlExtractException("NO_RIGHT_DECODE",101)
        return _response.read().decode(codemode)

def get_url_string(url , data = None):
    return  _get_url_reponse(url).read()
    
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
def get_url_info(query , base_url , data = None ,code="utf-8"):
    url = queryurl(base_url, query)
    return get_url_data(url,codemode = code , data= data)



def jsonstrtodict(jsonstr):
    datadict = None
    try:
        datadict = _jload(jsonstr)
    except Exception,e:
        raise  HtmlExtractException("JSON_DECODE_ERRO_%s" % e , 102)
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
        for i in range(n - 1):
            _num *= 10
    else:
        raise HtmlExtractException("NO_RIGHT_NUM",110)
    return random.randint(_num,(_num * 10) - 1)


def randintbyrang(_min,_max):
    if _min >= _max:
        raise HtmlExtractException("VALUE_IS_NOT_VALUE",113) 
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


if __name__ == "__main__":
    print getjson("jsonp(})")



