#!/usr/bin/env python
# coding=utf-8

import json
import sys
from Trie import Trie
reload(sys)
sys.setdefaultencoding('utf-8')

json_string = '{"a":{"a1":1,"a2":2},"arry":[{"a1":1,"a2":2},{"a1":1,"a2":2},{"a1":1,"a2":2},{"a1":1,"a2":2}]}'
trie = Trie()


class JsonClear(object):

    def clear_json(self, json_string):
        __json_trie = {}
        json_dict = json.loads(json_string)
        self.__parser(json_dict, __json_trie)
        print __json_trie

    def __parser(self, data, __json_trie, _level=0):
        if isinstance(data, dict):
            for _key, _val in data.items():
                print _key
                __json_trie[_key] = _level
                self.__parser(_val, __json_trie, _level + 1)
        elif isinstance(data, list):
            for _val in data:
                self.__parser(_val, __json_trie, _level + 1)


if __name__ == '__main__':
    j = JsonClear()
    j.clear_json(json_string)
