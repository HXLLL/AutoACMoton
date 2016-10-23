import re

def iscpp(code):
    pat= re.compile(".*?^\s*?#include.*?(int|void)\s*?main\s*?\(.*?\)", re.S+re.M)
    if re.search(pat, code): return True;
    return False

def isproblempage(page):
    pat = re.compile("<a href='submitpage\.php\?id=\d*?'>Submit</a>")
    if re.search(pat, page): return True
    return False
