import urllib
import urllib2
import cookielib

class POJBot:
    cookiejar = cookielib.CookieJar()
    opener=urllib2.build_opener(urllib2.HTTPCookieProcessor(cookiejar))

    def __init__(self):
        return None

    def login(self, username, password):
        loginurl = 'http://poj.org/login'
        postdata = urllib.urlencode({ 
                'user_id1':username, 
                'password1':password })
        self.opener.open(loginurl, postdata)

    def logout(self):
        logouturl = 'http://poj.org/login?action=logout'
        self.opener.open(logouturl)

    def submit_code(self, pid, code):
        submiturl = 'http://poj.org/submit'
        postdata = urllib.urlencode({
                    'problem_id':1000,
                    'language':'0', #cpp
                    'source':code })
        res = self.opener.open(submiturl, postdata)
