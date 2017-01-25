from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from requests.auth import HTTPBasicAuth
import webbrowser, requests, bs4, sys, os, time


login_url = "https://lang-8.com/login"
yamasvPage = "http://lang-8.com/605858/journals?page="


def login(browser, login_url):
	browser.get(login_url)
	browser.maximize_window()
	browser.implicitly_wait(1)
	userNameElem = browser.find_element_by_id('username')
	userNameElem.send_keys(myUserName)
	passwordElem = browser.find_element_by_id('password')
	passwordElem.send_keys(myPassword)
	passwordElem.submit()
	time.sleep(1)	
	# without waiting, the website doesn't have time to log in et register the information.


# ----------------------------------------- MAIN ----------------------------------------------------

#USING PHANTOMJS for headless browsing (without opening a mozilla window)
# browser = webdriver.PhantomJS(r"C:\Users\LU10600\Documents\phantomjs-2.1.1-windows\bin\phantomjs.exe", service_args=service_args)
browser = webdriver.PhantomJS(r"C:\Program Files\phantomjs-2.1.1-windows\bin\phantomjs.exe")

# LOG in lang8
login(browser, login_url)

entry_index = 1 # from 1 to 14xx...
first_page  = 1 
last_page   = 10 # when he starts explaining Japanese usages

print ("Start downloading....\n")
for page_index in reversed(range(first_page, last_page+1)):
	print ("Now downloading page: " + str(page_index))
	browser.get(yamasvPage + str(page_index))
	entries_page = browser.page_source
	soup         = bs4.BeautifulSoup(entries_page,"lxml")
	entries_elem = soup.select('.journal_title a')
	for entry in reversed(entries_elem):
		entry_link  = entry.get("href")
		browser.get(entry_link)
		entry_page  = browser.page_source
		soup        = bs4.BeautifulSoup(entry_page,"lxml")
		entry_text  = soup.select('#body_show_ori')
		entry_text  = str(entry_text[0]).replace("<div id=\"body_show_ori\">", "").replace("</div>","").replace("<br/>","\n")
		f           = open("yamasvEntries\\" + str(entry_index) + ".txt","w", encoding="utf-8")
		f.write(entry_text)
		f.close()
		entry_index = entry_index + 1


print ("\n----------------------------------\n")
print("DONE downloaded all entries.\n")