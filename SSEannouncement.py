__author__ = 'pchaosgit'
__email__ = 'drifthua@gmail.com'
# -*-coding:utf-8-*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import selenium.webdriver.support.ui as ui
import datetime
import wget
import tempfile
from bs4 import BeautifulSoup

def login(username,password):
    browser = webdriver.Firefox()
    browser.get("http://weibo.com/login.php")

    user = browser.find_element_by_xpath("//*[@id='pl_login_form']/div[5]/div[1]/div/input")
    user.send_keys(username, Keys.ARROW_DOWN)

    passwd = browser.find_element_by_xpath("//*[@id='pl_login_form']/div[5]/div[2]/div/input")
    passwd.send_keys(password, Keys.ARROW_DOWN)

    vcode = browser.find_element_by_xpath("//*[@id='pl_login_form']/div[5]/div[3]/div/input")
    if vcode:
        code = raw_input("verify code:")
        if code:
            vcode.send_keys(code, Keys.ARROW_DOWN)

    browser.find_element_by_xpath("//*[@id='pl_login_form']/div[5]/div[6]/div[1]/a/span").click()

    print( browser.find_element_by_xpath("//*[@id='v6_pl_content_homefeed']/div[2]/div[3]/div[1]/div[1]/div[3]/div[1]/a[1]").get_attribute("usercard"))

def getBrower(browserName="firefox"):
    return webdriver.Firefox()

def test():
    username = "email"
    passwd = "passwd"
    login(username, passwd)

def testsse(stcode):
  stcode = stcode
  #sseSearch(stcode)
  sseSearchbyhrefs(stcode)

def  sseSearch(stcode):
    browser = webdriver.Firefox()
    wait = ui.WebDriverWait(browser, 10)
    browser.get("http://www.sse.com.cn/disclosure/listedinfo/announcement/")
    #browser.get("http://www.sse.com.cn/assortment/stock/list/stockdetails/announcement/index.shtml?COMPANY_CODE=600401&productId=600401&bt=%E5%85%A8%E9%83%A8&static=t")
    #assert "公司公告" in driver.title
    #assert "productId" in driver.text
    sseInput = browser.find_element_by_xpath("//*[@id='productId']")
    sseInput.send_keys(stcode)
    sseInput.send_keys(Keys.RETURN)
    wait.until(lambda browser: browser.find_element_by_css_selector('a._blank'))

def stockannouncementURL(stcode, startDate=datetime.date.today( ), endDate= datetime.date.today( )):
    global browser
    urlparam = {"COMPANY_CODE": stcode, "productId": stcode, "bt": "全部", "static": "t"}
    url = "http://www.sse.com.cn/assortment/stock/list/stockdetails/announcement/index.shtml"
    return browser.get(url + getparams(urlparam))

def  sseSearchbyhrefs(stcode):
    global browser
    wait = ui.WebDriverWait(browser, 10)
    r = stockannouncementURL(stcode)
    #assert "productId" in r.text
    wait.until(lambda browser: browser.find_element_by_xpath("//div[@id='announcementDiv']"))
    print("browser.title: " + browser.title)
    #assert stcode in browser.title
    print(browser.find_element_by_xpath("//div[@id='announcementDiv']").text)

def getparams(urlparam):
    str="?"
    for k,v in urlparam.items():
        str += "&" + k
        str += "=" + v
    return str.lstrip("&")

def downloadannouncement(url, tagetfileName):
    filename = tempfile.gettempdir() + "/" + tagetfileName
    if not os.path.isfile(filename):
        print("downloading:", url, filename)
        wget.download(url, filename)
    else:
        print("FileExist:", url, filename)

def getAllPDF(soup):
    for tag in soup.find_all("div", {"id":"announcementDiv"}):
        for tagchild in tag.findAll("tr"):
            if len(tagchild.findAll("a")):
                taggrandchild = tagchild.findAll("td")
                filename = taggrandchild[1].string + "_" + taggrandchild[2].string + "_" + taggrandchild[4].string + "_" + taggrandchild[0].string
                for greatgrandson in taggrandchild[0].findAll("a"):
                    downloadannouncement(greatgrandson["href"], filename)

if __name__ == "__main__":
    browser = getBrower()
    try:
        stcode = "600177"
        browser.maximize_window()
        testsse(stcode)
        soup = BeautifulSoup(browser.page_source, 'lxml')
        getAllPDF(soup)
    finally:
        browser.close()

