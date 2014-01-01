#coding=utf-8
#!/usr/bin/env python







class UtilException(Exception):

    def __init__(self, msg, code=None):
        self.msg = msg
        self.code = code

    def __str__(self):
        if self.code:
            return "%s,%s" % (self.msg, self.code)
        else:
            return self.msg


class HtmlExtractException(UtilException):
    pass


class NoDataReturn(UtilException):
    pass



class NoDataParser(UtilException):
	pass