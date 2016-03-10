import os
import re
import tool
import urllib
import urllib.request



class Spider:
    
    def __init__(self):
        self.siteURL = 'http://mm.taobao.com/json/request_top_list.htm'
        self.tool = tool.Tool()
    
    def getPage(self,pageIndex):
        url = self.siteURL + "?page" + str(pageIndex)
        request = urllib.request.Request(url)
        response = urllib.request.urlopen(request)
        return response.read().decode("gbk")
    
    def getContents(self,pageIndex):
        page = self.getPage(pageIndex)
        pattern = re.compile('<div class="list-item".*?pic-word.*?<a href="(.*?)".*?<img src="(.*?)".*?<p class="top".*?<a.*?>(.*?)</a>.*?<strong>(.*?)</strong>.*?<span>(.*?)</span>', re.S)
        items = re.findall(pattern, page)
        contents = []
        for item in items :
           contents.append(["http:"+item[0],"http:"+item[1],item[2],item[3],item[4]])
        return contents
#    "====================伪装成用户登录"
    def getDetailPage(self,infoURL):
        response = urllib.request.urlopen(infoURL)
        return response.read().decode("gbk")

    def getBrief(self,page):
        pattern = re.compile('<div class="mm-aixiu-content".*?>(.*?)<!--',re.S)
        result = re.search(pattern,page)
        if result:
            return self.tool.replace(result.group(1))
        else :
            print ("EROOR")
  
    
    def getAllImg(self,page):
        pattern = re.compile('<div class="mm-aixiu-content".*?>(.*?)<!--',re.S)
        #个人信息页面所有代码
        content = re.search(pattern,page)
        #从代码中提取图片
        patternImg = re.compile('<img.*?src="(.*?)"',re.S)
        images = re.findall(patternImg,content.group(1))
        return images
    
    def saveImgs(self,images,name):
        number = 1
        print (u"发现",name,u"共有",len(images),u"张照片")
        for imageURL in images:
            splitPath = imageURL.split('.')
            fTail = splitPath.pop()
            if len(fTail)>3:
                fTail = "jpg"
            fileName = name + "/" + str(number) + "." + fTail
            self.saveImg(imageURL, fileName)
            number += 1    
    def saveIcon(self,iconURL,name):
        splitPath = iconURL.split('.')
        fTail = splitPath.pop()
        fileName = name + "/icon." + fTail
        self.saveImg(iconURL,fileName)
        
    def saveBrief(self,content,name):
        fileName = name + "/" + name + ".txt"
        f = open(fileName,"w+")
        print (u"正在偷偷保存她的个人信息",fileName)
        f.write(content.encode("gbk"))
            
    def saveImag(self,imageURL,fileName):
        u = urllib.request.urlopen(imageURL)
        data = u.read()
        f = open(fileName,'wb')
        f.write(data)
        print (u"正在悄悄保存她的一张图片为",fileName)
        f.close()
        
    def mkdir(self,path):
        path = path.strip()
        isExists = os.path.exists(path)
        if not isExists:
            print (u"偷偷新建了名字叫做",path,u'的文件夹')
            os.makedirs(path)
            return True
        else :
            print (u"名为",path,'的文件夹已经创建成功')
            return False
        
    def savePageInfo(self,pageIndex):
        contents = self.getContents(pageIndex)
        for item in contents:
            #item[0]个人详情URL,item[1]头像URL,item[2]姓名,item[3]年龄,item[4]居住地
            print (u"发现一位模特,名字叫",item[2],u"芳龄",item[3],u",她在",item[4])
            print (u"正在偷偷地保存",item[2],"的信息")
            print (u"又意外地发现她的个人地址是",item[0])
            detailURL = item[0]
            detailPage = self.getDetailPage(detailURL)
          #  print (detailPage)
            brief = self.getBrief(detailPage)
            images = self.getAllImg(detailPage)
            self.mkdir(item[2])
            self.saveBrief(brief, item[2])
            self.saveIcon(item[1],item[2])
            self.saveImgs(images,item[2])
    def savePagesInfo(self,startPage,endPage):
        for i in range(startPage,endPage+1):
            print (u"正在偷偷寻找第",i,u"个地方，看看MM们在不在")
            self.savePageInfo(i)
            
spider = Spider()
spider.savePagesInfo(1, 2)