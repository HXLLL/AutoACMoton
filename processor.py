import re
import identify

def html_ESC_decode(text):
    text = re.sub('&quot;','"',text)
    text = re.sub('&amp;','&',text)
    text = re.sub('&lt;','<',text)
    text = re.sub('&gt;','>',text)
    text = re.sub('&nbsp;',' ',text)
    return text

pattern_process_crayon_content = re.compile('(?s)<div class="crayon-line.*?>(.*?)</div>')
def process_crayon_content(content):
    res = ''
    lines = re.findall(pattern_process_crayon_content, content)
    for line in lines:
        res = res + re.sub('<span.*?>|</span>','',line) + '\n'
    return res
pattern_get_crayon_codes = re.compile('(?s)<td class="crayon-code">(.*?)</td>')
def get_crayon_codes(page):
    codes = re.findall(pattern_get_crayon_codes, page)
    res = []
    for code in codes:
        t = html_ESC_decode(process_crayon_content(code))
        if identify.iscpp(t): res.append(t)
    return res

pattern_process_intag_code_content_1 = re.compile('</div>')
pattern_process_intag_code_content_2 = re.compile('<.*?>')
pattern_process_intag_code_content_3 = re.compile('(?sm)^[ ]{,2}[\d]*')
def process_intag_code_content(code):
    print code
    code = re.sub(pattern_process_intag_code_content_1, '\n', code)
    code = re.sub(pattern_process_intag_code_content_2, '', code)
    code = re.sub(pattern_process_intag_code_content_3, '', code)
    return code

pattern_get_intag_codes = re.compile('(?s)<pre.*?>(.*?)</pre>|<code.*?>(.*?)</code>')
def get_intag_codes(page):
    codes = re.findall(pattern_get_intag_codes, page)
    res = []
    for code in codes:
        t = html_ESC_decode(process_intag_code_content(code))
        if identify.iscpp(t): res.append(t)
    return res

def getcodes(page):
    return (get_crayon_codes(page) + get_intag_codes(page))

pattern_gettitle = re.compile('<title>.*?</title>')
ojs = 'bzoj|poj|pku|hdu|zoj|uoj|lydsy|spoj|la|uva|codevs|vijos|tyvj|luogu'
texpr = '(?i)(' + ojs + r')[ -\]\)]{,3}p?([\d]{4})'
pattern_gettitle_t = re.compile(texpr)
def gettitle(page):
    ttitle = re.search(pattern_gettitle, page)
    if ttitle:
        title = html_ESC_decode(ttitle.group())
        res = re.findall(pattern_gettitle_t, title)
        return res
    else:
        return ""

pattern_getfirstresult = re.compile('(?s)<table align=center>.*?</table>')
results = 'Accepted|Presentation_Error|Wrong_Answer|Time_Limit_Exceed|Memory_Limit_Exceed|Output_Limit_Exceed|Runtime_Error|Compile_Error|Pending|Pending_Rejudging|Compiling|Running_&_Judging'
pattern_getfirstresult_results = re.compile(results)
def getfirstresult(page):
    statu_c = re.search(pattern_getfirstresult, page).group()
    res = re.search(pattern_getfirstresult_results, statu_c)
    if res:
        return res.group()
    else: 
        return ''

pattern_getsolutions = re.compile('(?s)<div class="result c-container .*?><h3 class="t"><a.*?href="(.*?)"')
def getsolutions(page):
    sols = re.findall(pattern_getsolutions, page)
    res = []
    for sol in sols:
        res.append(sol)
    return res

