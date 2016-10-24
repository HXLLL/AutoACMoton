import re
import time
import urllib
import urllib2
import cookielib

import processor
import identify

class BZOJBot:
    def __init__(self):
        self.cookiejar = cookielib.CookieJar()
        self.opener=urllib2.build_opener(urllib2.HTTPCookieProcessor(self.cookiejar))
        return None

    def login(self, _username, _password):
        loginurl = 'http://www.lydsy.com/JudgeOnline/login.php'
        postdata = urllib.urlencode({ 
                    'user_id':_username, 
                    'password':_password })
        self.username = _username
        self.password = _password
        self.opener.open(loginurl, postdata)

    def logout(self):
        logouturl = 'http://www.lydsy.com/JudgeOnline/logout.php'
        self.opener.open(logouturl)
    
    def sendheartbeat(self):
        self.opener.open('http://www.lydsy.com/JudgeOnline/')

    def submit_code(self, pid, code):
        submiturl = 'http://www.lydsy.com/JudgeOnline/submit.php'
        postdata = urllib.urlencode({
                    'id':pid,
                    'language':'1', #cpp
                    'source':code })
        return self.opener.open(submiturl, postdata).read()

    def can_submit_code(self, pid):
        problemurl = 'http://www.lydsy.com/JudgeOnline/problem.php?id=%d' % pid
        problem_page = self.opener.open(problemurl).read()
        if identify.isproblempage(problem_page):return True
        return False

    def getresult(self, pid):
        expr_status_f = 'Accepted|Presentation_Error|Wrong_Answer|Time_Limit_Exceed|Memory_Limit_Exceed|Output_Limit_Exceed|Runtime_Error|Compile_Error'
        url = 'http://www.lydsy.com/JudgeOnline/status.php?user_id=%s&problem_id=%d' % (self.username, pid)

        print 'judging...'
        page = self.opener.open(url).read()
        statu = processor.getfirstresult(page)
        cnt = 0
        while not re.match(expr_status_f, statu):
            ++cnt
            if(cnt>130):
                statu = ''
                break
            time.sleep(1)
            page = self.opener.open(url).read()
            statu = processor.getfirstresult(page)
        return statu

