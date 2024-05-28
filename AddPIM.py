'''
Project 1 : Selenium with python
___Add new employee in PIM module___
Test Case ID: TC_PIM_01
A User should be able to add a new employee in the PIM and should see a message for successful employee addition
'''

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep
class Orange:
   def __init__(self, url):
      #initializing the url
       self.url = url
      #initializing the chrome webdriver
       self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

   def boot(self):

       self.driver.get(self.url)

       sleep(3)
       #Maximizing the window
       self.driver.maximize_window()

   def quit(self):
       #Quiting function
       self.driver.quit()

   def AddPIM(self):

       self.boot()
       sleep(3)
       username = self.driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input')
       #Passing username value
       username.send_keys("Admin")
       password = self.driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input')
       #Passing password value
       password.send_keys("admin123")
       loginbutton = self.driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button')
       #Clicking on login button
       loginbutton.click()
       sleep(3)
       #Clicking on PIM module
       PIM=self.driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a')
       PIM.click()
       sleep(3)
       #Adding employee details inside PIM module
       addpim=self.driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[1]/button')
       addpim.click()
       sleep(3)
       #Passing firstname, lname, empid values into their respective textboxes
       fname=self.driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[1]/div/div/div[2]/div[1]/div[2]/input')
       fname.send_keys("Jasmine")
       Lname=self.driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[1]/div/div/div[2]/div[3]/div[2]/input')
       Lname.send_keys("Rose")
       empid=self.driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[2]/div/div/div[2]/input')
       empid.send_keys("3456")
       #Saving the details by clicking on the save button
       save1=self.driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[2]/button[2]')
       save1.click()
       sleep(5)
       #Enter some more personal details inside the same module
       personal_detail=self.driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[1]/a')
       personal_detail.click()
       sleep(5)
       military=self.driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[4]/div/div[1]/div/div[2]/input')
       military.send_keys("No")
       sleep(5)
       #Saving the page
       save2=self.driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[5]/button')
       save2.click()
       sleep(5)
       self.quit()
       print("New employee is added successfully !!!")

#Passing URL into the class to perform all the above activities
obj = Orange("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
#Calling AddPIM function
obj.AddPIM()