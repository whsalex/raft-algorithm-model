#!/usr/bin/env python

'''
   This library is used for analyse config file.
'''

import re
from pprint import pprint

CONFIG_LOCATION = "./CONFIGS"

configs = {}

def _strip_comments_and_spaces(line):
    ''' Remove the comments and spaces'''
    return line.split('#')[0].strip()

class Config_Parser(object):
    def __init__(self):
        self.confname = CONFIG_LOCATION
        self.conf     = {}

    def _parser_conf(self):
        for line in self.lines:
            if line == "":
                continue

            pattern = re.compile("^(\S*)\s*=\s*(\S*)")
            
            result = re.match(pattern, line)
            if result is not None:
                self.conf[result.groups()[0]] = result.groups()[1]
    
    def read_conf(self):
        fd = open(self.confname, "r")
        self.lines = [ _strip_comments_and_spaces(line) for line in fd.readlines() if line != "" ]
        fd.close()

        self._parser_conf()

    def do_conf(self):
        configs = self.conf

    def get_value(self, para):
        return self.conf.get(para, "NULL")

    def print_conf(self):
        pprint(self.lines)
        print ("========= Configs ===========")
        pprint(self.conf)


def test_main():
    global CONFIG_LOCATION
    CONFIG_LOCATION = "../../CONFIGS"

    conf = Config_Parser()
    conf.read_conf()
    conf.print_conf()

if __name__ == "__main__":
    test_main()
