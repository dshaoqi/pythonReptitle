#!/usr/bin/env python
# -*- coding:utf-8 -*-
import urllib
import urllib2
import re

class FirstRep:
    def __init__(self):
        self.pageIndex=1
        self.user_agent='Mozilla/4.0 (compatible;MSIE 5.5;Windows NT)'
        self.headers={'User-Agent':self.user_agent}
        self.stories=[]
        self.enable=False
        self.url='http://www.qiushibaike.com/hot/page/'
        self.pattern=r'<div class="content">'

    def getPage(self,PageIndex):
        try:
            request=urllib2.Request(self.url+str(self.pageIndex),headers=self.headers)
            #pageIndex+=1;
            response=urllib2.urlopen(request)
            pageCode=response.read().decode('utf-8')
            return pageCode

        except urllib2.URLError,e:
            if hasattr(e,"reason"):
                print "连接失败，错误原因",e.reason
                return None


    def getPageElement(self,pageIndex):
        pageCode=self.getPage(pageIndex)
        if not pageCode:
            print "页面加载失败"
            return False
        self.pageIndex+=1
        items=re.findall(self.pattern,pageCode)
        pageStories=[]
        for item in items:
            self.stories.append([item])
        return True

t=FirstRep()
t.getPageElement(1)
for i in t.stories:
    print i
