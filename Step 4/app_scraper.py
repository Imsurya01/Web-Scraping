import selenium 
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options 
options = Options()
options.add_argument("--headless")


def scrp_sugg(keyword):

    driver.get(f"{keyword}")

    #return sugg

driver = selenium.webdriver.Chrome(options=options)
def main():

   # data_file = open("appdata.txt", "a")
    my_file = open("onlylink_list.txt", "r")
    data = my_file.read()
    data_into_list = data.split("\n")
    

    

    for i in data_into_list:
        data_file = open("separated .csv", "a")
        try:

            scrp_sugg(i)
        
            app_name = driver.find_element(By.CLASS_NAME,"vWM94c").text
            rating_dwnlds = driver.find_elements(By.CLASS_NAME,"wVqUob")
            link = driver.find_element(By.XPATH , "//body/c-wiz[2]/div[1]/div[1]/c-wiz[1]/c-wiz[1]/c-wiz[1]/section[1]/div[1]/div[1]/a[1]").get_attribute('href')
            rating_review= rating_dwnlds[0].text.replace('\n',' ').replace('star','star`')
            downloads= rating_dwnlds[1].text.replace('\n',' ')
        
            data_file.write(app_name)
            print (app_name)
            data_file.write("`")
            data_file.write(rating_review)
            data_file.write("`")
            data_file.write(downloads)
            data_file.write("`")
            data_file.write(link)
            data_file.write("\n")    
            
        except:
            pass

main()

