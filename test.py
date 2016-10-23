import re

page = """
123123123123
000asiei<title>sai[bzoj]1010</title>1992
112<title>poj-1010bbbb</title>hh
sieiiiacoh
eidn
"""
expr = '<title>(.*?)</title>'
ttitle = re.search(re.compile(expr, re.S), page)


ojs = 'bzoj|poj|pku|hdu|zoj|uoj|lydsy|spoj|la|codevs|vijos|tyvj|luogu'
if ttitle:
    texpr = r'(' + ojs + r')[ -\]\)]{,3}p?([\d]{4})'
    title = ttitle.group().lower()
    res = re.findall(texpr, title)
    print res
else:
    print '!!'
