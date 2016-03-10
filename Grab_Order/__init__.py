import http.cookiejar
import re
import urllib
import urllib.request
import webbrowser
class Taobao:
    
    def __init__(self):
        self.loginURL = "https://login.taobao.com/member/login.jhtml"
        self.loginHeaders = {
            "Host":"login.taobao.com",
             "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64; rv:44.0) Gecko/20100101 Firefox/44.0",
            "Referer":"https://login.taobao.com/member/login.jhtml",
            "Content-Type":"application/x-www-form-urlencoded",
            "Connection":"keep-alive" 
                  }
        self.username = "13275429439"
        self.ua = "013#JxEA0QAnA2wAAAAAANefAAYBABnDwsHAv+Ko86Lts8Kg7JjgsN246NalxbfFBgEAGcPCwcC/5j5pOHslVDJCMkYqWz5iUD9fLV8GAQAZw8LBwL/rFkEQQx1sCnoKfhJjBlpoF3cFdwYBABnDwsHAv+qC1YTPkeC+zr7Kptey7tyry7nLBgEAGcPCwcC/7SR3Jmk3RiRQPEwkUTRsWilJO0kGAQAZw8LBwL/vWQxbFko5WStZL0EyVQs7SihUIAYBABnDwsHAv+/ThtWYyLfXpdehz7zfgbHA3q7eBgEAGcPCwcC/7p7JmNuF9JLikuaK+57C8J//jf8WAQAEzczLygYBABnDwsHAv/EIUwJNE2IAjPiAEH0YSHYFZRdlFgEABM3My8oFAQAaw8acmh0cGxoZVBkYQxJdA3IQfAhwAI3ouIYHAQAUw8LBwINtOGcqdgCM7p/wjuC65tQFAQAaw8aHhwUEAwIBPOnos+Kt84LgrNig8J34qJYHAQAGzc3My/MuBQEADM3IgYG6ubi3toxYVw0BABvHxsud9Zr9k+WXtoSz5a3iwfLB7Nv2xejU49QWAQAEzczLygIBAAbOzc7M/8oBAQAIzczKmq77SbEUAQAGzc6MlR3AFwEABM3MyskMAQA3+8v+yPHJ+sv5zPrAiLSJsYG5j7aD49Ln0bOHs4Li0Puersmuzq+eqcmszf6Y9ZC9heHZ4Obd6BMBAAvMyLOyt4Lc94O/2wsBAC/N5+bljP+K+YuwgFAjTStDLAVwDmIDYw0iQi5AEGIEbg9rGDhbNVM7VH0WfQhqBQMBACjNzMuXlpWUk5KRlRsaGRuysbCqCQgHBYB/fnjX1tXXiomIh4aFhIOCFgEABM3My8oGAQAHzbe2tbS2ewcBAAbNzMvKw5IWAQAEzczLygcBABTDw8LB+rnsu/aq3KjCs9y61Lbq2BYBAATNzMvKBwEAFMPDwsH8BFcGSRdmBHAcbARxFEx6BwEAFMPCwcCCxJfGidemxLDcrMSx1Iy6FgEABM3My8oGAQAZw8LBwL/r2Yzblsq52avZr8Gy1Yu7yqjUoAYBABnDwsHAv+kXQhFcBHMTYRNlC3gTTX0MahpqBgEAGcPCwcC/53MmdThoF3cFdwFvHH8hEWA+Tj4GAQAZw8LBwL/kaDNiLXMCYCxYIHAdeCgWZQV3BQ=="
        self.password2 = "97de1117b5f7a16c2ab898e0e59f5964f2d8f3f03d8d909e00619b9d25cd64f0716017b0d431f0ca34678b8683ddb6d081fddbf643fda485e6b04d347d857a5137b40bc6f77df78a6f56aa88dff08846367f579d2d36e63a8fca5f7837d27dbe5d51810df5b411f47e753d809e4a3a9d96a3b48d33084b8e7e42f3df1eb73fee"
        self.post = post = {
            'ua':self.ua,
            'TPL_password':'',
            "ncoSig":"",
            "ncoSessionid":"",
            "ncoToken":"919726a06ec550e14d3ffcb0eadf20bd2909898a",
            "slideCodeShow":"false",
            'loginsite':'0',
            'newlogin':'0',
            "TPL_redirect_url":"",
            'from':'tb',
            'fc':'default',
            'style':'default',            
            'css_style':'',
            "keyLogin":"false",
            "qrLogin":"true",
            "newMini":"false",
            "newMini2":"false",
            'tid':'',
             'loginType':'3',
            'minititle':'',
            'minipara':'',           
            'umto':'NaN',
            'pstrong':'',        
            'sign':'',
            'need_sign':'',        
            'isIgnore':'',
            'full_redirect':'',        
            'popid':'',
            'callback':'',
            'guf':'',
            'not_duplite_str':'',
            'need_user_id':'',
            'poy':'',
            'gvfdcname':'10',
            'gvfdcre':'',
            'from_encoding ':'',
            'sub':'',
            'TPL_password_2':self.password2,
            'loginASR':'1',
            'loginASRSuc':'1',
            'allp':'',
            'oslanguage':'zh-CN',
            'sr':'1440*900',
            'osVer':"",
            'naviVer':'firefox|44',        
            'TPL_username':self.username
        }
        self.postData = urllib.parse.urlencode(self.post).encode('utf-8')
        self.cookie = http.cookiejar.LWPCookieJar()
        self.cookieHandler = urllib.request.HTTPCookieProcessor(self.cookie)
        self.opener = urllib.request.build_opener(self.cookieHandler,urllib.request.HTTPHandler)       
        

    def getJ_Htoken(self):
        request = urllib.request.Request(self.loginURL, self.postData, self.loginHeaders)
        # 得到第一次登录尝试的相应
        response = self.opener.open(request)
        content = response.read().decode("gbk")
        print (content)
        tokenPattern = re.compile('id="J_HToken" value="(.*?)"', re.S)
        tokenMatch = re.findall(tokenPattern, content)
        if tokenMatch:
            print (tokenMatch)
            return tokenMatch
        
    def getSTBYToken(self,token):
        tokenURL = 'https://passport.alipay.com/mini_apply_st.js?site=0&token=%s&callback=stCallback6' % token
        request = urllib.request.Request(tokenURL)
        response = urllib.request.urlopen(request)
        #处理st，获得用户淘宝主页的登录地址
        pattern = re.compile('{"st":"(.*?)"}',re.S)
        result = re.search(pattern,response.read().decode("utf-8"))
        print (response.read().decode("utf-8"))
        #如果成功匹配
        if result:
            print (u"成功获取st码")
            #获取st的值
            st = result.group(1)
            print (st)
            return st
        else:
            print (u"未匹配到st")
            return False
    def main(self):
        token = self.getJ_Htoken()
        self.getSTBYToken(token)
        
taobao = Taobao()
taobao.main()


        
        # self.proxy = urllib.request.ProxyHandler(self.proxyURL)
        # self.opener =urllib.request.build_opener(self.proxy)
        # urllib.request.build_opener(self.opener)
        # response = urllib.request.urlopen(self.loginURL)
    #===========================================================================
    #     #=======================================================================
    # def needIdenCode(self):
    #     request = urllib.request.Request(self.url,self.postData,self.loginHeaders)
    #     response = self.opener.open(request)
    #     content = response.read().decode("gbk") 
    #     status = response.getcode()
    #     if status == 200:
    #         print (u"获取请求成功")
    #         pattern = re.compile(u'\u8bf7\u8f93\u5165\u9a8c\u8bc1\u7801',re.S)
    #         result = re.search(pattern, content)
    #         if result:
    #             print (u"此次安全验证异常，您需要输入验证码")
    #             return content
    #         else:
    #             print (u"此次安全验证通过，您这次不需要输入验证码")
    #             return False
    #     else:
    #         print (u"获取请求失败")
    # def getIdenCode(self,page):
    #     pattern = re.compile('<img id="J_StandardCode_m.*?data-src="(.*?)"',re.S)
    #     
    #     
    #     
    #     
    # def main(self):
    #     needResult = self.needIdenCode()
    #===========================================================================
            
