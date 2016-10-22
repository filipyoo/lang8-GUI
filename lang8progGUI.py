# GUI program to read yamasv's entries from lang8, whose entries were scraped by the program in scrapeLang8.py file
# The lang8progGUI.vbs is a file to launch a .bat file without opening a terminal Windows 
# Each entry is stored in a .txt file with a number, the most recent has the greatest number
# pyuic5 -x lang8UI.ui -o lang8UI.py
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from lang8UI import Ui_Dialog
import os, sys
from random import randint


class Lang8UIprogram(Ui_Dialog):

	def __init__(self, dialog):
		Ui_Dialog.__init__(self)
		self.setupUi(dialog)

		# When the GUI is launch, it displays the last entry read, by checking it ou from the lastReadEntryIndex.txt file
		self.last_read_entry_index = int(open("lastReadEntryIndex.txt").read())
		last_read_entry_text = open("yamasvEntries\\%d.txt" % self.last_read_entry_index, encoding="utf-8").read()
		self.current_page = self.last_read_entry_index
		self.currentPageDisplay.setText(str(self.current_page)+"/"+str(entries_total))
		self.textBrowser.setPlainText(last_read_entry_text)


		# To make your GUI elements available to the rest of the object, preface them with self.
		# random, previous and next page is precede by "self", ortherwise it can't be a "global" variable 
		self.random_page_index = randint(1, entries_total)
		random_page_text = open("yamasvEntries\\%d.txt" % self.random_page_index, encoding="utf-8").read()

		self.next_page_index = self.current_page + 1 if self.current_page < entries_total else self.current_page
		next_page_text = open("yamasvEntries\\%d.txt" % self.next_page_index, encoding="utf-8").read()

		self.previous_page_index = self.current_page - 1 if self.current_page > 1 else self.current_page
		previous_page_text = open("yamasvEntries\\%d.txt" % self.previous_page_index, encoding="utf-8").read()

		# Describe what function to call, when the specific button is clicked 
		self.randomButton.clicked.connect(self.randomPageDisplay(random_page_text))
		self.nextButton.clicked.connect(self.nextPageDisplay(next_page_text))
		self.previousButton.clicked.connect(self.previousPageDisplay(previous_page_text))
		self.pageSearchButton.clicked.connect(self.searchPage)


	def randomPageDisplay(self, *args):
		def randomPage():
			self.random_page_index = randint(1, entries_total)
			random_page_text = open("yamasvEntries\\%d.txt" % self.random_page_index, encoding="utf-8").read()
			self.textBrowser.setPlainText(random_page_text)
			self.current_page = self.random_page_index
			self.currentPageDisplay.setText(str(self.current_page)+"/"+str(entries_total))
			f = open("lastReadEntryIndex.txt", "w")
			f.write(str(self.current_page))
			f.close()
			# updateScreenWith(self, random_page_index)
		return randomPage

	def nextPageDisplay(self, *args):
		def nextPage():
			self.next_page_index = self.current_page + 1 if self.current_page < entries_total else self.current_page
			next_page_text = open("yamasvEntries\\%d.txt" % self.next_page_index, encoding="utf-8").read()
			self.textBrowser.setPlainText(next_page_text)
			self.current_page = self.next_page_index
			self.currentPageDisplay.setText(str(self.current_page)+"/"+str(entries_total))
			f = open("lastReadEntryIndex.txt", "w")
			f.write(str(self.current_page))
			f.close()
			# updateScreenWith(self, next_page_index)
		return nextPage

	def previousPageDisplay(self, *args):
		def previousPage():
			self.previous_page_index = self.current_page - 1 if self.current_page > 1 else self.current_page
			previous_page_text = open("yamasvEntries\\%d.txt" % self.previous_page_index, encoding="utf-8").read()
			self.textBrowser.setPlainText(previous_page_text)
			self.current_page = self.previous_page_index
			self.currentPageDisplay.setText(str(self.current_page)+"/"+str(entries_total))
			f = open("lastReadEntryIndex.txt", "w")
			f.write(str(self.current_page))
			f.close()
			# updateScreenWith(self, previous_page_index)
		return previousPage


	# def updateScreenWith (self, page_to_display_index):
		# page_to_display_text = open("yamasvEntries\\%d.txt" % self.page_to_display_index, encoding="utf-8").read()
		# self.textBrowser.setPlainText(page_to_display_text)
		# self.current_page = self.page_to_display_index
		# self.currentPageDisplay.setText(str(self.current_page)+"/"+str(entries_total))

	def searchPage(self, *args):
		if self.pageSearchLine.text().isnumeric() and int(self.pageSearchLine.text()) in range (1,entries_total+1):
			page_to_search = int(self.pageSearchLine.text())  
			searched_page_text = open("yamasvEntries\\%d.txt" % page_to_search, encoding="utf-8").read()
			self.textBrowser.setPlainText(searched_page_text)
			self.current_page = page_to_search
			self.currentPageDisplay.setText(str(self.current_page)+"/"+str(entries_total))
			f = open("lastReadEntryIndex.txt", "w")
			f.write(str(self.current_page))
			f.close()
		



if __name__ == '__main__':

	entries_total = len(os.listdir("yamasvEntries"))

	app = QtWidgets.QApplication(sys.argv)
	dialog = QtWidgets.QDialog() 
	prog = Lang8UIprogram(dialog)
	dialog.show()
	sys.exit(app.exec_())
