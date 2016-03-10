import urllib
import urllib.request
import http.cookiejar
 
filename ="zhihucookie.txt"

cookie = http.cookiejar.MozillaCookieJar(filename)
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
values = {"uername":13275429439,"password":"8678QQbz521"} 
postdata = urllib.parse.urlencode(values).encode("utf-8")
url = " http://www.zhihu.com/#signin" 
result = opener.open(url)
cookie.save(ignore_discard=True,ignore_expires=True)
user_agent = "Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)"
headers = {"User-Agent":user_agent,
            "Connection":"keep-alive",
            "Accept-Language":"zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3"
           }
data = urllib.parse.urlencode(values)
binary_data = data.encode('utf-8')
try:
    request = urllib.request.Request(url,binary_data,headers=headers)
    response = urllib.request.urlopen(request) 
    print (response.read())
except urllib.request.HTTPError as e:
    if hasattr(e, "code"):
        print (e.code)
    if hasattr(e, "reason"):
        print (e.reason)
  
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
#===============================================================================
# page = 1
# url = 'http://www.qiushibaike.com/hot/page/' + str(page)
# user_agent = "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:44.0) Gecko/20100101 Firefox/44.0"
# headers ={"User-Agent":user_agent} 
# try:
#     request = urllib.request.Request(url,headers=headers)
#     response = urllib.request.urlopen(request)
#     print (response.read())
# except urllib.request.URLError as e:
#     if hasattr(e,"code"):
#         print (e.code)
#     if hasattr(e,"reason"):
#         print (e.reason)
#===============================================================================