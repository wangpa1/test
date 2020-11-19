from testing.common.base import Base
from selenium import webdriver
from  selenium.webdriver.common.by import By
class Login(Base):
    loc1 = ("id", "ember10")
    loc2 = ("id", "ember11")
    loc3 = ("id", "ember12")


    def input_username(self,username):
        self.sendKeys(self.loc1,username)

    def input_password(self,psw):
        self.sendKeys(self.loc2,psw)

    def click_login(self):
        self.click(self.loc3)


if __name__ == "__main__":
    driver = webdriver.Chrome()
    driver.get("https://bosslogin.test.zbjdev.com/cp-index3?appid=23592&back_url=https%3A%2F%2Fworkbench.test.zbjdev.com%2Fyanxuan%2Fsaap%2Flist")
    zentao = Login(driver,10,0.5)
    zentao.input_username("yulang")
    zentao.input_password("123456")
    zentao.click_login()

