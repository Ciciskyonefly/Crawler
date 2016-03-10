import re

import urllib
import urllib.request
from pip._vendor.distlib.compat import raw_input
#
class Tool:
    removeImg = re.compile('<img.*?>| {7}|')
    removeAddr = re.compile("<a.*?>|</a>")
    replaceLine = re.compile('<tr>|<div>|</div>|</p>')
    replaceTD = re.compile('<td>')
    replacePara = re.compile('<p.*?>')
    replaceBR = re.compile('<br><br>|<br>')
    removeExtraTag = re.compile('<.*?>')
    def replace(self,x):
        x = re.sub(self.removeImg,"",x)
        x = re.sub(self.removeAddr,"",x)
        x = re.sub(self.replaceLine,"\n",x)
        x = re.sub(self.replaceTD,"\t",x)
        x = re.sub(self.replacePara,"\n    ",x)
        x = re.sub(self.replaceBR,"\n",x)
        x = re.sub(self.removeExtraTag,"",x)
        return x.strip()


class BDTB:
    
    def __init__(self, baseUrl, seeLZ,floorTag):
        self.tool = Tool()
        self.baseURL = baseUrl
        self.seeLZ = '?see_lz=' + str(seeLZ)
        self.floorTag = floorTag
        self.defaultTitle = u"百度贴吧1"
        self.floor = 1
    
    def getPage(self, pageNum):
        try:
            url = self.baseURL + self.seeLZ + '&pn=' + str(pageNum)
            request = urllib.request.Request(url)
            response = urllib.request.urlopen(request)
            return response.read().decode("utf-8")
        except urllib.request.URLError as e:
            if(hasattr(e, "reason")):
                print ("连接百度贴吧失败，错误原因", e.reason)
                return None
    def getTitle(self,page):
        pattern = re.compile('<h3 class=.*?title="(.*?)" style="width: 396px">', re.S)
        result = re.search(pattern, page)
        if result:
            print (result.group(1).strip())
    def getNumPage(self,page):
        pattern = re.compile('<li class="l_reply_num.*?</span>.*?<span.*?>(.*?)</span>', re.S)
        result = re.search(pattern, page)
        if result :
            print (result.group(1).strip())
            return result.group(1).strip()
        else:
            return None

    def getContent(self, page):
        pattern = re.compile('<div id="post_content_.*?>(.*?)</div>', re.S)
        items = re.findall(pattern, page)
        floor = 1
        contents = []
        for item in items:
            #将文本进行去除标签处理，同时在前后加入换行符
            content = "\n" + self.tool.replace(item) + "\n"
            contents.append(content)
        print (contents)    
        return contents
            
    def selfFileTitle(self,title): 
        if title is not None:
            self.file = open(title + ".txt","w+")
        else:
            self.file = open(self.defaultTitle+".txt","w+")
         
    def writeData(self,contents):
        for item in contents:
            if self.floorTag == '1' :
                floorLine = "\n"+str(self.floor)+u"--------------------"
                self.file.write(floorLine)
                self.file.write(item)
                self.floor += 1
    def start(self):
        indexPage = self.getPage(1)
        pageNum = self.getNumPage(indexPage)
        title = self.selfFileTitle(self.getTitle(indexPage))
        if pageNum == None :
            print ("URL已失效，请重试")
            return 
        try:
            print ("该帖子共有"+pageNum+"页")
            for i in range(1,int(pageNum)+1):
                print ("正在写入第"+str(i)+"页。。。。。。。。")
                page = self.getPage(i)
                contents = self.getContent(page)
                self.writeData(contents)
        except IOError as e:
            print ("写入异常，原因" + e.message)
             
                
            
baseURL = 'http://tieba.baidu.com/p/3138733512'
seeLZ = raw_input("是否只获取楼主发言，是输入1，否输入0\n")
floorTag = raw_input("是否写入楼层信息，是输入1，否输入0\n")
bdtb = BDTB(baseURL,seeLZ,floorTag)
bdtb.start()

