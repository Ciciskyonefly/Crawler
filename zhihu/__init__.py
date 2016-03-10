import gzip
import http.cookiejar
import re
import urllib
#error:403 Forbidden

def ungzip(data):
    try:
        print ("正在解压.......")
        data = gzip.decompress(data)
        print("解压完毕!")
    except:
        print("未经压缩，无须解压")
    return  data

def getXSRF(data):
    cer = re.compile('name=\"_xsrf\" value=\"(.*)\"',re.S)
    strlist = cer.findall(data)
    return strlist[0]
    
def getOpener(head):
    #deal with the cookies
    cj = http.cookiejar.CookieJar()
    pro = urllib.request.HTTPCookieProcessor(cj)
    opener = urllib.request.build_opener(pro)
    header = []
    for key,value in head.items():
        elem = (key,value)
        header.append(elem)
    opener.addheaders = header
    return opener

head = {
       "Accept": "text/html, application/xhtml+xml, image/jxr, */*",
        "Accept-Encoding": "gzip,deflate",
        "Accept-Language": "zh-Hans-CN,zh-Hans;q=0.5",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko",
        "DNT": "1",
        "Connection": "Keep-Alive",
        "Host": "www.zhihu.com"
        } 

url = 'http://www.zhihu.com/'
opener = getOpener(head)
op = opener.open(url)
data = op.read()
data = ungzip(data)
#解压
_xsrf = getXSRF(data.decode())

url += '#signin'
id = "13275429439"
password = '8678QQbz521'
postDict = {
            '_xsrf':_xsrf,
            'email':id,
            'password':password,
            'rememberme':'y'
            }
postData = urllib.parse.urlencode(postDict).encode()
try:
    op = opener.open(url,postData)
except urllib.request.HTTPError as e:
    if hasattr(e,"code"):
       print (e.code)
    if hasattr(e, "reason"):
        print (e.reason)
    else:
        print ("OK")
data = op.read()
data = ungzip(data)
print (data.decode())