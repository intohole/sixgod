#coding=utf-8



import json
import random
import time
import re
from pexceptions import *




_jload = json.loads
_urlencode = urllib.urlencode
lang_detect = re.compile("charset=([\w\d-]+)" ,  re.IGNORECASE)







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
    pass



