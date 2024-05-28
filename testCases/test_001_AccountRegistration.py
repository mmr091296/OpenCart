import os.path

import pytest

from pageObjects.HomePage import HomePage
from pageObjects.AccountRegistrationPage import AccountRegistrationPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities.randomString import random_string_generator
class Test_001_AccountReg:
   # baseURL = "http://localhost/opencart/"
   baseURL = ReadConfig.getApplicationURL()
   logger = LogGen.loggen()

   @pytest.mark.regression
   def test_account_reg(self,setup):
       self.logger.info("**** test_001_AccountRegistration started *** ")
       print("**** test_001_AccountRegistration started *** ")
       self.driver = setup
       self.driver.get(self.baseURL)
       self.logger.info("Launching application")
       print("Launching application")
       self.driver.maximize_window()
       self.driver.implicitly_wait(3)
       self.hp=HomePage(self.driver)
       self.logger.info("clicking on MyAccount--> register")
       print("clicking on MyAccount--> register")
       self.hp.clickMyAccount()
       self.hp.clickRegister()
       self.regpage=AccountRegistrationPage(self.driver)
       self.regpage.setFirstName("John")
       self.regpage.setLastName("Canedy")
       self.regpage.setEmail(random_string_generator())
       self.regpage.setEmail(ReadConfig.getUseremail())
       self.regpage.setTelephone("65656565")
       self.regpage.setPassword(ReadConfig.getPassword())
       self.regpage.setConfirmPassword(ReadConfig.getPassword())
       self.regpage.setPrivacyPolicy()
       self.regpage.clickContinue()
       self.confmsg=self.regpage.getconfirmationmsg()
       if self.confmsg=="Your Account Has Been Created!":
           assert True
           self.driver.close()
       else:
           self.driver.save_screenshot(os.path.abspath(os.curdir)+"\\screenshots\\"+"test_account_reg33.png")
           self.driver.close()
           assert False
       self.logger.info("**** test_001_AccountRegistration finished *** ")
       print("clicking on MyAccount--> register")
