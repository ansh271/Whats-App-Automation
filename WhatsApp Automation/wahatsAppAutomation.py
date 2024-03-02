import time

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

names = input("Enter Phone Number or Name : ")
message = input("Enter your Message : ")
n = int(input("How many times you want to send message : "))
print("Sending Messages please wait......")

names = list(names.split(","))

driver = webdriver.Chrome()
driver.maximize_window()
# opening WhatsApp
driver.get("https://web.whatsapp.com/")

# wait for the page to fully load

# taking time to log in and waiting for 30 seconds
time.sleep(40)

for i in range(len(names)):
    # selecting search button using its XPATH
    element = driver.find_element(By.XPATH, '//*[@id="side"]/div[1]/div/div/button')
    action = ActionChains(driver)
    action.click(on_element=element)  # clicking on Search button
    action.send_keys(names[i])  # sending text to search the person
    action.send_keys(Keys.ENTER)  # pressing ENTER
    action.perform()  # performing all the above actions
    text = 'Type a message'  # text for finding element by its Content

    for j in range(n):
        # getting element by its content
        element = driver.find_element(By.XPATH, '//div[contains(text(), "' + text + '")]')
        action.click(on_element=element)  # clicking on the element
        action.send_keys(message)  # sending the message
        action.send_keys(Keys.ENTER)  # pressing ENTER
        action.perform()  # performing all the above actions
time.sleep(8)  # wait for 8 sec
print("Your messages are sent.")  # completed
