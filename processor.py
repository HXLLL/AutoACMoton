import re
import identify

def html_ESC_decode(text):
    text = re.sub('&quot;','"',text)
    text = re.sub('&amp;','&',text)
    text = re.sub('&lt;','<',text)
    text = re.sub('&gt;','>',text)
    text = re.sub('&nbsp;',' ',text)
    return text

def process_crayon_content(content):
    res = ''
    l_expr = '<div class="crayon-line.*?>(.*?)</div>'
    pat = re.compile(l_expr, re.S)
    
    lines = re.findall(pat, content)
    for line in lines:
        res = res + re.sub('<span.*?>|</span>','',line) + '\n'
    return res

def get_crayon_codes(page):
    expr = '<td class="crayon-code">(.*?)</td>'
    codes = re.findall(re.compile(expr, re.S), page)

    res = []
    for code in codes:
        t = html_ESC_decode(process_crayon_content(code))
        if identify.iscpp(t): res.append(t)
    return res

def a(data):
    ic = re.search("<div.*?>(.*?)</div>", data).group(1)
    return ic + '\n'
    
def process_code_tag_content(code):
    code = re.sub("<div.*?>.*?</div>", a, code)
    code = re.sub("<.*?>", '', code)
    code = re.sub(re.compile("^[ ]{,2}[\d]*", re.S+re.M), '', code)
    return code

def get_intag_codes(page):
    expr = '<pre.*?>(.*?)</pre>|<code.*?>(.*?)</code>'
    codes = re.findall(re.compile(expr, re.S), page)
    res = []
    for code in codes:
        t = html_ESC_decode(process_code_tag_content(code))
        if identify.iscpp(t): res.append(t)
    return res


def getcodes(page):
    return (get_crayon_codes(page) + get_intag_codes(page))

def gettitle(page):
    expr = '<title>.*?</title>'
    ttitle = re.search(re.compile(expr, re.S), page)

    ojs = 'bzoj|poj|pku|hdu|zoj|uoj|lydsy|spoj|la|uva|codevs|vijos|tyvj|luogu'
    if ttitle:
        title = html_ESC_decode(ttitle.group().lower())
        texpr = '(' + ojs + r')[ -\]\)]{,3}p?([\d]{4})'
        res = re.findall(texpr, title)
        return res
    else:
        return ""

def getfirstresult(page):
    results = 'Accepted|Presentation_Error|Wrong_Answer|Time_Limit_Exceed|Memory_Limit_Exceed|Output_Limit_Exceed|Runtime_Error|Compile_Error|Pending|Pending_Rejudging|Compiling|Running_&_Judging'
    expr = '<table align=center>.*?</table>'
    statu_c = re.search(re.compile(expr, re.S), page).group()
    res = re.search(re.compile(results), statu_c)
    if res:
        return res.group()
    else: 
        return ''

def getsolutions(page):
    expr = '<div class="result c-container .*?><h3 class="t"><a.*?href="(.*?)"'
    sols = re.findall(re.compile(expr, re.S), page)
    res = []
    for sol in sols:
        res.append(sol)
    return res

