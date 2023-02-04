import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import booking.constants as con

class Booking(webdriver.Chrome):
    def __init__(self,driver_path=r"c:/seleniumDriver",teardown=False) -> None:
        self.driver_path = driver_path
        self.teardown=teardown
        os.environ["PATH"]+=self.driver_path
        super(Booking,self).__init__()
    def load(self):
        self.get(con.url)
    def __exit__(self, exc_type, exc, traceback,):
        if self.teardown:
            self.quit()
    


