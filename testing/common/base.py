from selenium import  webdriver
from selenium.webdriver.support.wait import  WebDriverWait
from  selenium.webdriver.common.by import By
class Base(object):
    def __init__(self,driver,timeout,t):
        self.driver = driver
        self.timeout=timeout
        self.t=t


    def findElement( self,loctor):
        ele = WebDriverWait(self.driver,self.timeout,self.t).until(lambda x: x.find_element(*loctor))
        return ele
    # def is_xists(self,loctor):
    #     try:
    #         WebDriverWait(driver,self,10,0.5).until(lambda x: x.find_element(*loctor))
    #         return True
    #     except:
    #         return False

    # def element_is_disappeared(self, locator):
    #     is_disappeared = WebDriverWait(self.driver,10, 0.5, (ElementNotVisibleException)).until_not(lambda x: x.find_element(*locator).is_displayed())
    #     print (is_disappeared)
    def sendKeys(self,loctor,text):
        ele = self.findElement(loctor)
        ele.send_keys(text)
    def click(self,loctor):
        ele = self.findElement(loctor)
        ele.click()
    def is_element_exsit(self,loctor):
        try:
            self.findElement(loctor)
            return True
        except:
            return False
if __name__=="__main__":
    driver = webdriver.Chrome()
    driver.get("https://bosslogin.test.zbjdev.com/cp-index3?appid=23592&back_url=https%3A%2F%2Fworkbench.test.zbjdev.com%2Fyanxuan%2Fsaap%2Flist")
    zentao = Base(driver,10,0.5)
    loc1 = (By.ID, "ember10")
    loc2 = (By.ID, "ember11")
    loc3 = (By.ID, "ember12")
    zentao.sendKeys(loc1,"yulang")
    zentao.sendKeys(loc2,"123456")
    zentao.click(loc3)


