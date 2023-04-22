from selenium import webdriver
from selenium.webdriver.chrome.service import Service


s = Service("'C:\\Users\Omkar A Kshirsagar\Downloads\chromedriver_win32\chromedriver.exe'")


class music_one():
    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(service=s, options=options)


    def play(self, query):
        self.query = query
        self.driver.get(url="https://www.youtube.com/results?search_query=" + query)
        video = self.driver.find_element("xpath", value='//*[@id="video-title"]/yt-formatted-string')
        video.click()



