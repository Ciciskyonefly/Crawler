import urllib.request
import socket
import re
import sys
import os
#sucess,but still not clear with picture save
targetDir = r'E:/eclipse/Crawler/testSavePicture'

def saveFile(data):
    save_path = 'E:\douban.out'
    f_obj = open(save_path,'wb')
    f_obj.write(data)
    f_obj.close()

weburl  = "http://www.douban.com/"
headers= {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36'}
req = urllib.request.Request(url= weburl,headers= headers)
webPage = urllib.request.urlopen(req)#发送请求报文
contentBytes = webPage.read()
#print (contentBytes.decode("utf-8"))
content = contentBytes.decode("utf-8")
saveFile(contentBytes)
images = re.findall('<img src="(.*?)"',content,re.S)
i = 1
for image in images:
    print (image)
    try:
        urllib.request.urlretrieve(image,'%s.jpg'%i )
        i = i + 1
    except:
        print ("抛出异常")
