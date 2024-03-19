from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from datetime import datetime
import time

#Initializing driver
driver = webdriver.Chrome()
driver.maximize_window()

#Open home page
driver.get("https://demo.evershop.io/")
#driver.find_element(By.XPATH,'//a[@href="/account/login"]')
driver.find_element(By.XPATH,'//a[@href="/account/login"]').click()

'''#Create account
driver.find_element(By.XPATH,'//a[@href="/account/register"]')
.click()
driver.find_element(By.XPATH,'//input[@name="full_name"]')
.send_keys('Pepe')
driver.find_element(By.XPATH,'//input[@name="email"]')
.send_keys('pepe@gmail.com')
driver.find_element(By.XPATH,'//input[@name="password"]')
.send_keys('Pepe123')
driver.find_element(By.XPATH,'//button[@class="button primary"]')
.click()
#End Create account'''

#log in
driver.find_element(By.XPATH,'//input[@name="email"]').send_keys('pepe@gmail.com')
driver.find_element(By.XPATH,'//input[@name="password"]').send_keys('Pepe123')
driver.find_element(By.XPATH,'//button[@type="submit"]').click()
time.sleep(1)
driver.find_element(By.XPATH,'//a[@href="/men" and contains(text(),"Men")]').click()
time.sleep(1)

#first item selected
driver.find_element(By.XPATH,'//img[@src="/assets/catalog/1034/3600/plv7632-Green-list.png"]').click()
driver.find_element(By.XPATH,'//a[@href="#" and contains(text(),"M")]').click()
driver.find_element(By.XPATH,'//a[@href="#" and contains(text(),"Blue")]').click()
time.sleep(1)
driver.find_element(By.XPATH,'//button[@class="button primary outline"]').click()
time.sleep(1)

#Second item selected
driver.find_element(By.XPATH,'//a[@href="/men" and contains(text(),"Men")]').click()
driver.find_element(By.XPATH,'//img[@src="/assets/catalog/4477/5876/plv3335-Pink-list.png"]').click()
driver.find_element(By.XPATH,'//input[@name="qty"]').clear()
driver.find_element(By.XPATH,'//input[@name="qty"]').send_keys('2')
driver.find_element(By.XPATH,'//a[@href="#" and contains(text(),"X")]').click()
driver.find_element(By.XPATH,'//a[@href="#" and contains(text(),"Black")]').click()
time.sleep(1)
driver.find_element(By.XPATH,'//button[@class="button primary outline"]').click()
time.sleep(1)

#Third item selected
driver.find_element(By.XPATH,'//a[@href="/women"]').click()
driver.find_element(By.XPATH,'//img[@src="/assets/catalog/6634/7682/plv3753-Pink-list.png"]').click()
driver.find_element(By.XPATH,'//input[@name="qty"]').clear()
driver.find_element(By.XPATH,'//input[@name="qty"]').send_keys('3')
driver.find_element(By.XPATH,'//a[@href="#" and contains(text(),"X")]').click()
driver.find_element(By.XPATH,'//a[@href="#" and contains(text(),"Pink")]').click()
time.sleep(1)
driver.find_element(By.XPATH,'//button[@class="button primary outline"]').click()
time.sleep(1)

#Go to the shopping cart and chechout
driver.find_element(By.XPATH,'//a[@class="add-cart-popup-button"]').click()
time.sleep(1)
driver.find_element(By.XPATH,'//a[@href="/checkout"]').click()
time.sleep(1)

#Verify the Addres checkbox is present
try:
    element = driver.find_element(By.XPATH,'//span[contains(text(),"My billing address is same as shipping address")]')
except NoSuchElementException:
    print ("Not found")
else:
    print("found")
    element.click()

#Filling the shipping address
element = driver.find_element(By.XPATH,'//input[@name="address[full_name]"]')
element.clear()
element.send_keys('Pepe Lucho')
element = driver.find_element(By.XPATH,'//input[@name="address[telephone]"]')
element.clear()
element.send_keys('987654321')
element = driver.find_element(By.XPATH,'//input[@name="address[address_1]"]')
element.clear()
element.send_keys('av anywhere')
element = driver.find_element(By.XPATH,'//input[@name="address[city]"]')
element.clear()
element.send_keys('Peru')
time.sleep(1)
element = Select(driver.find_element(By.XPATH,'//select[@id="address[country]"]'))
element.select_by_index(2)
#time.sleep(1)
element = Select(driver.find_element(By.XPATH,'//select[@id="address[province]"]'))
element.select_by_index(1)
time.sleep(1)
element = driver.find_element(By.XPATH,'//input[@name="address[postcode]"]')
element.clear()
element.send_keys('123456')

#Verifying the shipping method is present
try:
    element = driver.find_element(By.XPATH,'(//span[@class="pl-1"])[1]')
except NoSuchElementException:
    print("not found")
else:
    element.click()

#Click continue to payment
driver.find_element(By.XPATH,'//button[@class="button primary"]').click()
time.sleep(1)

#select Visa
element = driver.find_element(By.XPATH,'//form[@id="checkoutPaymentForm"]/div[3]/div[3]/div/div/div/div[1]/a').click()
time.sleep(1)
driver.execute_script('window.scrollBy(0,500)')
time.sleep(1)

#Payment switching to the iframe
iframe = driver.find_element(By.XPATH,'//*[@id="card-element"]/div/iframe')
driver.switch_to.frame(iframe)
time.sleep(1)
driver.find_element(By.XPATH,'//*[@id="root"]/form/div/div[2]/span[1]/span[2]/div/div[2]/span/input').send_keys('4242 4242 4242 4242')
driver.find_element(By.XPATH,'//input[@name="exp-date"]').send_keys('04/24')
driver.find_element(By.XPATH,'//input[@name="cvc"]').send_keys('242')

#Swithching to default webpage to click on place order
driver.switch_to.default_content()
driver.find_element(By.XPATH,'//button[@class="button primary"]').click()
time.sleep(5)
dateTime = datetime.now().strftime("%d-%m-%Y%H:%M:%S")
print(dateTime)
strDateTime = str(dateTime)
driver.get_screenshot_as_file('C:/Users/user/OneDrive/Workspace/Project01/files/img3.png')
print("Test succeed: "+strDateTime)
time.sleep(1)
driver.close()

