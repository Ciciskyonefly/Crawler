import urllib.request
import http.cookiejar
#声明一个CookieJar对象来保存cookie
filename  = "cc.txt"
cookie = http.cookiejar.MozillaCookieJar(filename)
#利用urllib.request库的HTTPCookieProcessor来创建cookie处理器
handler = urllib.request.HTTPCookieProcessor(cookie)
#通过handler来构建opener
opener = urllib.request.build_opener(handler)
#此处的open方法同urllib.request的urlopen的方法也可以传入request
response = opener.open("http://ww.baidu.com")
cookie.save(ignore_discard=True, ignore_expires=True)
for item in cookie:
    print ('Name = ' + item.name)
    print ("Value = " + item.value)


