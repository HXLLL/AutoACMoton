import network
import processor

def grab_code(url):
    page = network.getpage(url)
    problem = processor.gettitle(page)
    code = processor.getcodes(page)
    return { "problem":problem, "code":code}

def grab_from_baidu_page(keyword):
    page = network.getpage('https://www.baidu.com/s?wd=%s' % keyword)
    sol_pages = processor.getsolutions(page)
    return sol_pages
