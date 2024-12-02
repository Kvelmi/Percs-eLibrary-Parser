from selenium.webdriver.chrome.options import Options


CAPTCHA_URL = "captcha"
AUTHOR_URL = "author_profile"

chrome_options = Options()
#chrome_options.add_argument('--headless')  Работа в фоновом режиме
chrome_options.add_argument('--disable-gpu')  
chrome_options.add_argument('--no-sandbox')  
chrome_options.add_argument('--disable-dev-shm-usage') 
chrome_options.add_argument('--remote-debugging-port=9222')
chrome_options.add_argument("--disable-3d-apis")
chrome_options.add_argument('--ignore-certificate-errors') # Последние два для теста
chrome_options.add_argument('--allow-running-insecure-content')
