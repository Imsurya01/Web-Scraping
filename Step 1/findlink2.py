from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
#options = webdriver.ChromeOptions()
#options.add_experimental_option('excludeSwitches', ['enable-logging'])
browser = webdriver.Chrome()
browser.get('https://play.google.com/store/apps')
buttons = browser.find_elements(By.XPATH,'//div/button[@aria-label="Search" and contains(@class, "VfPpkd-Bz112c-LgbsSe yHy1rc eT1oJ mN1ivc")]')
#path of search div


file = open("linkwithkey.txt", "a")


for button in buttons:
    button.click()
    data = browser.find_element(By.XPATH,"//input[starts-with(@class, 'HWAcU')]")
#path of search bar jisme keyword dalna hai
keywords = []
#keyword list
for first_letter in range(ord('r'), ord('z')+1):
     for second_letter in range(ord('a'), ord('z')+1):
         for third_letter in range(ord('a'), ord('z')+1):
             alphabet = chr(first_letter) + chr(second_letter) + chr(third_letter)
             keywords.append(alphabet)

for ram in keywords:   
#all possible keywords dalne k liye
    data.send_keys(ram)
    elements = browser.find_elements(By.XPATH,"//ul/li[starts-with(@class, 'YVhSle')]/a")
#path of suggested keywords


    try:
        for element in elements:

#all 5 suggestions scrap krne ke liye
            txt = element.text
            link = element.get_attribute('href')
#got the text and link
            file.write(txt)
            file.write("\n")
            file.write(link)
            file.write("\n")
#all 5 suggestions saved in text file
    except:
        time.sleep(1)

        
    data.clear()

#search bar cleared

file.close()    
