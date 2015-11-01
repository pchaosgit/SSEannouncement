__author__ = 'pchaosgit'
__email__ = 'drifthua@gmail.com'
# -*-coding:utf-8-*-
# http://disclosure.szse.cn/m/search0425.jsp?stockCode=000998&startTime=2013-10-02&endTime=2015-10-18
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import selenium.webdriver.support.ui as ui
import datetime
from datetime import timedelta
import wget
import os
import tempfile
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import logging
import re

# logging.basicConfig(
#         level=logging.INFO, format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s', datefmt='%a, %d %b %Y %H:%M:%S')

logging.basicConfig(
        level=logging.DEBUG, format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s', datefmt='%a, %d %b %Y %H:%M:%S')

baseurl = "http://disclosure.szse.cn/m/search0425.jsp"
def getBrower(browserName="firefox"):
    if browserName.lower() == "firefox":
        return webdriver.Firefox()

def downloadannouncement(url, tagetfileName):
    file_name, file_ext = os.path.splitext(url)
    # todo 取得url内的文件后缀，加到filename
    filename = tempfile.gettempdir() + "/" + tagetfileName + file_ext
    if not os.path.isfile(filename):
        #使用以下语句，url长度可能会引起错误：“ urwid.canvas.CanvasError: Canvas text is wider than the maxcol specified“
        # logging.info("downloading: %{url} %{filename}" %{url ,  filename})
        #
        logging.info("downloading: {0} {1}".format(url, filename))
        wget.download(url, filename)
    else:
        logging.info("FileExist: " + url +  filename)

def getAllPDF(soup):
    for tag in soup.findAll('td', attrs={'class': 'td2'}):
        logging.debug("getAllPDF {0} {1}".format(tag, tag.text))
        span = tag.find('span', attrs={'class': 'link1'})
        logging.debug("getAllPDF getspan {0} {1}".format(span, span.text))
        # 去掉日期前后的括号：[]
        announcementDate = span.text[1:-1]
        announcementTitle = tag.find("a",attrs={'href': re.compile(".PDF")})
        global stcode
        filename = stcode + '_' + announcementDate + "_" + announcementTitle.text
        downloadannouncement(announcementTitle["href"], filename)

def saveToFile(filename = '', soup = None):
    with open(filename, "w") as text_file:
        text_file.write("{0}".format(soup))
    logging.info('saved file: {0} '.format(filename))

def getparams(urlparam):
    str="?"
    for k,v in urlparam.items():
        str += "&" + k
        str += "=" + v
    return str.lstrip("&")

def stockannouncementURL(stcode, startDate=datetime.date.today(), endDate= datetime.date.today()):
    global browser
    if endDate < startDate + timedelta(days = 7):
        startDate = endDate - timedelta(days = 7)
    urlparam = {"stockCode": stcode, "startTime": "{0}".format(startDate), "endTime": "{0}".format(endDate)}
    url = baseurl
    # r = browser.get("http://www.szse.cn/main/disclosure/rzrqxx/rzrqjy/")
    r = browser.get("http://disclosure.szse.cn/m/drgg.htm")
    if browser.find_element_by_xpath("//td"):
        logging.debug('find_element_by_xpath("//td")')
        return browser.get(url + getparams(urlparam))

def sseSearchbyhrefs(stcode):
    global browser
    wait = ui.WebDriverWait(browser, 15)
    try:
        r = stockannouncementURL(stcode)
        wait.until(lambda browser: browser.find_element_by_css_selector('td.page12'))
        logging.debug("browser.title: " + browser.title)
        logging.debug("td.td2" + browser.find_element_by_css_selector('td.td2').text)
    except ValueError:
         logging.debug("Oops! not find the announcement")
        pass

def testsse(stcode):
    stcode = stcode
    #sseSearch(stcode)
    sseSearchbyhrefs(stcode)

if __name__ == "__main__":
    logging.info(" started")
    browser = getBrower()
    try:
        browser.maximize_window()
        stcode = "000998"
        stcode = "000693"
        stcode = "300135"
        testsse(stcode)
        soup = BeautifulSoup(browser.page_source, 'lxml')

        if len(soup) > 1:
            for a in soup.findAll('div', {'class' : 'index'}):
                logging.info("soup.a {0}".format(a))
                for aa in soup.findAll('a', attrs={'href': re.compile("PDF")}):
                    logging.info("soup.a {0}".format(aa))
                    newlink = aa['href']
                    newlink = urljoin(baseurl, newlink)
                    aa['href'] = newlink
                logging.info("soup.a {0}".format(a.prettify()))
                # a = BeautifulSoup(a, 'lxml')
                saveToFile(os.path.join(tempfile.gettempdir(), '{0}.htm'.format(stcode)), a)
        getAllPDF(soup)
    finally:
        browser.close()
        logging.info(" Ended")
