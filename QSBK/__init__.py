
import re
import urllib
from urllib.error import URLError


class QSBK:
    
    def __init__(self):
     #   self.pageIndex = 1
        self.user_agent =  "Mozilla/4.0(compatible;MSIE 5.5;Windows NT)"
        self.headers = {"User-Agent":self.user_agent}
        #存放段子的变量
        self.stories = []
        #存放程序是否继续运行变量
        self.enable = False
    def getPage(self):
        try:
            url = "http://www.qiushibaike.com/hot/"
            request = urllib.request(url,headers = self.headers)
            response = urllib.request.urlopen(request)
            pageCode = response.read().decode("utf-8")
            return pageCode
        except urllib.request.URLError as e:
            if hasattr(e,"reason"):
                print ("连接糗事百科失败,错误原因",e.reason)
                return None
    def getPageItems(self):        
            pageCode = self.getPage()
            if not pageCode:
                print "页面加载失败。。。。。。"
                return None
            pattern = re.compile('<div.*?class="article.*?</a>.*?<a.*?title="(.*?)".*?</div>.*?<div.*?class="content">(.*?)<!.*?</div>.*?<span.*?class="number.*?>(.*?)</i>',re.S)
            items = re.findall(pattern,pageCode)
            pageStories = []
            for item in items:
                haveImge = re.search("img",item[2])
                if not haveImge:
                    pageStories.append([item[0].strip(),item[1].strip(),item[1].strip()])
            return pageStories
            
            
            
            
            
            
            