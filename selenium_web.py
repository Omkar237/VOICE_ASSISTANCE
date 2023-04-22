from selenium import webdriver
from selenium.webdriver.chrome.service import Service

s = Service("'C:\\Users\Omkar A Kshirsagar\Downloads\chromedriver_win32\chromedriver.exe'")

class info():
    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(service=s, options=options)


    def get_info(self, query):
        self.query = query
        self.driver.get(url="https://www.wikipedia.org/")
        search = self.driver.find_element(by="xpath", value='//*[@id="searchInput"]')
        search.click()
        search.send_keys(query)

        enter = self.driver.find_element(by="xpath", value='//*[@id="search-form"]/fieldset/button')
        enter.click()







