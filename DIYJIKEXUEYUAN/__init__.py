'''
Created on 2016年3月8日

@author: Cici
'''
#error : can not loading picture
import os
import re
import urllib.request

#sucess//os.path.exists(),os.makedirs()
#===============================================================================
# targetDir = r'E:\eclipse\Crawler\DIYJIKEXUEYUA
# def destFile(path):
#     if not os.path.isdir(targetDir):
#         os.mkdir(targetDir)
#     pos = path.rindex('/')
#     t = os.path.join(targetDir,path[pos+1:])
#     return t
#  
#===============================================================================
# #===============================================================================
# url = "http://www.jikexueyuan.com/"
# req = urllib.request.Request(url)
# response = urllib.request.urlopen(req)
# contentBytes = response.read()
# content = contentBytes.decode("utf-8")
# images =  re.findall('<img src="(.*?)".*?class="lessonimg',content,re.S)
# i = 0
# for image in images:
#     print ("now downloding : " + image)
#     try:
#         urllib.request.urlretrieve(image,"%s.jpg"%i)
#         i = i + 1
#     except:
#         print ("抛出异常")
#===============================================================================
def savePicFile(path,picName):
    if not os.path.exists(path):
        os.makedirs(path)
    totalPath = path + "\\"+picName
    return totalPath 
    
    
path = "E:\eclipse\Crawler\DIYJIKEXUEYUAN"
FileName = "越南"
weburl  = "https://www.douban.com/photos/album/1620525301/"
headers= {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36'}
req = urllib.request.Request(url= weburl,headers= headers)
webPage = urllib.request.urlopen(req)#发送请求报文
contentBytes = webPage.read()
#print (contentBytes.decode("utf-8"))
content = contentBytes.decode("utf-8")
#saveFile(contentBytes)
images = re.findall('<img src="(.*?)"',content,re.S)
i = 1
for image in images:
    print (image)
    strname = image.split('.',-1)[-1]
    totalPath = path +"\\" +FileName
    try:
        urllib.request.urlretrieve(image,savePicFile(totalPath, "%s.%s"%(i,strname)))
        i = i + 1
    except:
        print ("抛出异常")

