#!/usr/bin/env python
#catch the www.baidu.com
import urllib2

response = urllib2.urlopen("http://www.baidu.com")
print response.read()



