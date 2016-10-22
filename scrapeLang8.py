from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from requests.auth import HTTPBasicAuth
import webbrowser, requests, bs4, sys, os, time


# connection parameters
# ----------------------------------------------------------------------
proxies = {
  'http': 'http://LU10600:fantasynoki0_@www-deny.wrc.melco.co.jp:9515',
  'https': 'http://LU10600:fantasynoki0_@www-deny.wrc.melco.co.jp:9515' #https is used and not http
}

myUserName = "philippe_khin@hotmail.fr"
myPassword = "fantasynoki0"

login_url = "https://lang-8.com/login"
yamasvPage = "http://lang-8.com/605858/journals?page="

service_args = [
    '--proxy=www-deny.wrc.melco.co.jp:9515',
    '--proxy-type=https',
    '--proxy-auth=LU10600:fantasynoki0_'
    ]
# ----------------------------------------------------------------------



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

entry_index = 1441 # from 1 to 14xx...
first_page = 1 
last_page = 4 # when he starts explaining Japanese usages

print ("Start downloading....\n")
for page_index in reversed(range(first_page, last_page+1)):
	print ("Now downloading page: " + str(page_index))
	browser.get(yamasvPage + str(page_index))
	# time.sleep(3)	
	entries_page = browser.page_source
	soup = bs4.BeautifulSoup(entries_page,"lxml")
	# f = open("ok.txt", "w", encoding="utf-8")
	# f.write(str(soup))
	entries_elem = soup.select('.journal_title a')
	for entry in reversed(entries_elem):
		entry_link = entry.get("href")
		browser.get(entry_link)
		# time.sleep(3)	
		entry_page = browser.page_source
		soup = bs4.BeautifulSoup(entry_page,"lxml")
		# f = open("okok.txt", "w", encoding="utf-8")
		# f.write(str(soup))
		entry_text = soup.select('#body_show_ori')
		# print (type(entry_text))
		# print (str(entry_text[0]))
		entry_text = str(entry_text[0]).replace("<div id=\"body_show_ori\">", "").replace("</div>","").replace("<br/>","\n")
		# print (entry_text)
		f = open("yamasvEntries\\" +str(entry_index)+ ".txt","w", encoding="utf-8")
		f.write(entry_text)
		f.close()
		entry_index += 1


print ("\n----------------------------------\nDONE downloaded all entries.\n")





# TODO :
# OK -- interesting posts are from the 76th page
# DONE -- put each entry in a file (so totalFile = 20*76)
# DONE -- name them with a number (1 to 14xx...)
# another script to check out if yamasv has posted new entry, by checking the entry date (class .journal_date)
# if yes, download it and put in new file, with the latest number as a name
# implement GUI, with next/previous entry button, and random button, update new entry...
# DONE -- loop over page and entries reversly to get the most recent entry with the biggest number of entry_index