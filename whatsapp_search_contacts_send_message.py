from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep #better response
import sys

# Replace below path with the absolute path
# to chromedriver in your computer

friends_lists = ['Manikandan PM','Akshay wd'] 
'''Instead of above we can aprimorate this by import those:
import openpyxl #To read an Excel(.xlsx) file with contacts names
import docx  #To read a Word(.docx) file with the message
import PySimpleGUI #To create a user interface and use NSIS to make ".exe" 
pls check my project Wpp-Sender @valmsou
'''
driver = webdriver.Chrome('../chromedriver')

driver.get("https://web.whatsapp.com/")
wait = WebDriverWait(driver, 600)

group_title = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.RLfQR")))
search = driver.find_elements_by_xpath('//*[@id="side"]/div[2]/div/label/input')[0]

for friend in friends_lists:
	search.clear()
	search.send_keys(friend)
	wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "button._3Burg")))
	sleep(3)
	persons = driver.find_elements_by_class_name('_2wP_Y')
	print(len(persons))
	for person in persons:
		try:
			if person.text not in ['CHATS','MESSAGES']:
				person_title = person.find_element_by_class_name('_1wjpf')
				print(person_title.get_attribute("title"))
				person_contact = person.find_element_by_class_name('_2EXPL')
				person_contact.click()
				sleep(2)
				message = driver.find_elements_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')[0]
				message.send_keys("This is Testing Message from Selenium")

				sendbutton = driver.find_elements_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button')[0]
				sendbutton.click()
		except:
			print('Send sucessful to: {}',format(person)) 
			continue

driver.close()