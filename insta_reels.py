from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



website ="https://www.instagram.com/"
path = "C:\\Users\\sumit\\Videos\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe"

service = Service(executable_path=path)
driver = webdriver.Chrome(service=service)
driver.get(website)

time.sleep(3)

try:
    username =  WebDriverWait(driver,20).until(
        EC.presence_of_element_located((By.XPATH,'//input[@name="username"]'))
    )
    #Enter your username here
    username.send_keys('sumit_username')
    time.sleep(2)

    password =  WebDriverWait(driver,20).until(
        EC.presence_of_element_located((By.XPATH,'//input[@name="password"]'))
    )
    #Enter your password here
    password.send_keys('sumit_password')
    time.sleep(2)

    login =  WebDriverWait(driver,20).until(
        EC.presence_of_element_located((By.XPATH,'//button[@class=" _acan _acap _acas _aj1- _ap30"]'))
    )
    login.click()
    
    time.sleep(2)
    list_of_buttons =  WebDriverWait(driver,20).until(
        EC.presence_of_element_located((By.XPATH,'//div[@class="x9f619 xxk0z11 xii2z7h x11xpdln x19c4wfv xvy4d1p"]'))
    )
    
    buttons = driver.find_elements(by="xpath",value='//div[@class="x9f619 xxk0z11 xii2z7h x11xpdln x19c4wfv xvy4d1p"]')
    
    fourth_button = buttons[5]  
    fourth_button.click()

    time.sleep(2)
    close_popup =  WebDriverWait(driver,20).until(
        EC.presence_of_element_located((By.XPATH,'//button[@class="_a9-- _ap36 _a9_1"]'))
    )
    close_popup.click()
    time.sleep(2)
    
    
    ele =  WebDriverWait(driver,20).until(
        EC.presence_of_element_located((By.XPATH, "//*[contains(@class, 'x1lliihq') and contains(@class, 'x193iq5w') and contains(@class, 'x6ikm8r') and contains(@class, 'x10wlt62') and contains(@class, 'xlyipyv') and contains(@class, 'xuxw1ft')]"))
    )
    print("found name")
    elements = driver.find_elements(By.XPATH, "//*[contains(@class, 'x1lliihq') and contains(@class, 'x193iq5w') and contains(@class, 'x6ikm8r') and contains(@class, 'x10wlt62') and contains(@class, 'xlyipyv') and contains(@class, 'xuxw1ft')]")
    for element in elements:
        #Enter your crush name(as saved in insta)
        if element.text == 'pookie':
            element.click()
    
    print("writing text")
    time.sleep(5)
    search_box =  WebDriverWait(driver,40).until(
        EC.presence_of_element_located((By.XPATH,'//p[@class="xat24cr xdj266r"]'))
    )
    # Enter your message
    search_box.send_keys('enter your message')
    print("send")
    time.sleep(5)
    send_btn = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.XPATH, "//div[text()='Send']"))
)

# Click the element
    send_btn.click()


except:
    print("error")
    driver.quit()

time.sleep(20)


# Close the browser
driver.quit()

