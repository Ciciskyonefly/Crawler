import urllib
import urllib.request

import re


url = "http://www.qiushibaike.com/hot/"
user_agent = "Mozilla/4.0(compatible;MSIE 5.5;Windows NT)"
headers = {"User-Agent" : user_agent}
try:
    request = urllib.request.Request(url,headers= headers)
    response = urllib.request.urlopen(request)
    content = response.read().decode("utf-8")
    pattern  = re.compile('<div.*?class="article.*?</a>.*?<a.*?title="(.*?)".*?</div>.*?<div.*?class="content">(.*?)<!.*?</div>.*?<div(.*?)<span.*?class="number.*?>(.*?)</i>',re.S)
    items = re.findall(pattern, content)
    for item in items:
        haveImg = re.search("img", item[2])
        print (item[0],item[1],item[3])
except urllib.request.URLError as e:
    if hasattr(e, "code"):
        print (e.code)
    if hasattr(e, "reason"):
        print (e.reason)
