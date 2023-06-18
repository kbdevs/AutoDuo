from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import chromedriver_autoinstaller
import requests
import json
import time
import os
chromedriver_autoinstaller.install()

chrome_options = webdriver.ChromeOptions()
# chrome_options.binary_location = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'
# chrome_options.add_argument("--headless=new")
# chrome_options.add_argument("--desktop-window-1080p")
# chrome_options.add_argument("load-extension=/Users/kb/Library/Application Support/Google/Chrome/Default/Extensions/cjpalhdlnbpafiamejdnhcphjbkeiagm/1.49.2_38")

driver1 = webdriver.Chrome(options=chrome_options)
driver1.get('https://www.duolingo.com')
print("Starting browser 1...")

while True:
            try:
                # Find the element with the specified XPath
                element = driver1.find_element(By.XPATH, '//*[@id="root"]/div[2]/div/div[2]/div/div[1]/div/div[2]')
                
                # Continue with your code after the element is found
                # For example, you can click on the element
                
                
                # Exit the loop if the element is found
                break
            except:
                # Print a message or handle the exception as needed
                print("Element not found. Retrying in 3 seconds...")
                
                # Delay for 3 seconds before retrying
                time.sleep(3)

driver2 = webdriver.Chrome(options=chrome_options)
driver2.get('https://www.duolingo.com')
print("Starting browser 2...")

while True:
            try:
                # Find the element with the specified XPath
                element = driver2.find_element(By.XPATH, '//*[@id="root"]/div[2]/div/div[2]/div/div[1]/div/div[2]')
                
                # Continue with your code after the element is found
                # For example, you can click on the element
                
                
                # Exit the loop if the element is found
                break
            except:
                # Print a message or handle the exception as needed
                print("Element not found. Retrying in 3 seconds...")
                
                # Delay for 3 seconds before retrying
                time.sleep(3)

driver3 = webdriver.Chrome(options=chrome_options)
driver3.get('https://www.duolingo.com')
print("Starting browser 3...")


while True:
            try:
                # Find the element with the specified XPath
                element = driver3.find_element(By.XPATH, '//*[@id="root"]/div[2]/div/div[2]/div/div[1]/div/div[2]')
                
                # Continue with your code after the element is found
                # For example, you can click on the element
                
                
                # Exit the loop if the element is found
                break
            except:
                # Print a message or handle the exception as needed
                print("Element not found. Retrying in 3 seconds...")
                
                # Delay for 3 seconds before retrying
                time.sleep(1)




is_first_iteration = True
while True:
    
        print("Reopening lesson...")
        reopen = driver1.find_element(By.XPATH, "//*[@id='root']/div[2]/div/div[2]/div/div[2]/div[1]/section[2]/div/div[11]/div/div/button")
        reopen.click()
        print("Reopening lesson 2...")
        reopen = driver2.find_element(By.XPATH, "//*[@id='root']/div[2]/div/div[2]/div/div[2]/div[1]/section[2]/div/div[11]/div/div/button")
        reopen.click()
        print("Reopening lesson 3...")
        reopen = driver3.find_element(By.XPATH, "//*[@id='root']/div[2]/div/div[2]/div/div[2]/div[1]/section[2]/div/div[11]/div/div/button")
        reopen.click()

        time.sleep(3)

        print("Reopening lesson again...")
        reopen2 = driver1.find_element(By.XPATH, "//*[@id='root']/div[2]/div/div[2]/div/div[2]/div[1]/section[2]/div/div[11]/div[2]/div/div[1]/div/a")
        reopen2.click()
        print("Reopening lesson again 2...")
        reopen2 = driver2.find_element(By.XPATH, "//*[@id='root']/div[2]/div/div[2]/div/div[2]/div[1]/section[2]/div/div[11]/div[2]/div/div[1]/div/a")
        reopen2.click()
        print("Reopening lesson again 3...")
        reopen2 = driver3.find_element(By.XPATH, "//*[@id='root']/div[2]/div/div[2]/div/div[2]/div[1]/section[2]/div/div[11]/div[2]/div/div[1]/div/a")
        reopen2.click()

        time.sleep(10)
  
        if is_first_iteration:
            print("Opening script...")
            with open('script.txt', 'r') as file:
                script = file.read()

            print("Executing script...")
            driver1.execute_script(script)
            print("Executing script 2...")
            driver2.execute_script(script)
            print("Executing script 3...")
            driver3.execute_script(script)

            time.sleep(5)

            print("Solving...")
            start = driver1.find_element(By.ID, "solveAllButton")
            start.click()
            print("Solving 2...")
            start = driver2.find_element(By.ID, "solveAllButton")
            start.click()
            print("Solving 3...")
            start = driver3.find_element(By.ID, "solveAllButton")
            start.click()

            is_first_iteration = False

        while True:
            try:
                # Find the element with the specified XPath
                element = driver1.find_element(By.XPATH, '//*[@id="root"]/div[2]/div/div[2]/div/div[1]/div/div[2]')
                element = driver2.find_element(By.XPATH, '//*[@id="root"]/div[2]/div/div[2]/div/div[1]/div/div[2]')
                element = driver3.find_element(By.XPATH, '//*[@id="root"]/div[2]/div/div[2]/div/div[1]/div/div[2]')
                
                # Continue with your code after the element is found
                # For example, you can click on the element
                
                time.sleep(1)
                # Exit the loop if the element is found
                break
            except:
                # Print a message or handle the exception as needed
                print("Element not found. Retrying in 1 second...")
                
                # Delay for 3 seconds before retrying
                time.sleep(1)

   
