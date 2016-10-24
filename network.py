import urllib
import urllib2
import cookielib

NETWORK_SPEED_TEST = 0
def getpage(url):
    user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'
    headers = { 'User-Agent':user_agent }
    request = urllib2.Request(url, headers = headers)
    if NETWORK_SPEED_TEST: print "recieving data"
    response = urllib2.urlopen(request)
    if NETWORK_SPEED_TEST: print "data recieved"
    return response.read()
