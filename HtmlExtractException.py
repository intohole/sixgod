#coding=utf-8



class HtmlExtractException(Exception):
    
    
    def __init__(self,msg,code=None):
        Exception.__init__(self)
        self.msg = msg
        self.code = code
    
    
    def __str__(self):
        if self.code:
            return "%s,%s" % (self.msg , self.code)
        return self.msg
    
    
        