#!/usr/bin/env python

import lib.Getconf.getconf as getconf

# Check the config file reading
conf=getconf.Config_Parser()
conf.read_conf()
