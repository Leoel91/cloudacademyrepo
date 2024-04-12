import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestCloudacademy():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_cloudacademy(self):
    #Connect to cloudacademy.com and resize viewport 
    self.driver.get("https://cloudacademy.com/")
    self.driver.set_window_size(1920, 1080)
    
    #assertion on cloud academy 
    WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".header-logo > .logo-white")))
    elements = self.driver.find_elements(By.CSS_SELECTOR, ".header-logo > .logo-white")
    assert len(elements) > 0

    #click on search box and insert of correct string
    self.driver.find_element(By.CSS_SELECTOR, ".ais-SearchBox-input").click()
    self.driver.find_element(By.CSS_SELECTOR, ".ais-SearchBox-input").send_keys("aws,gcp and azure")
    self.driver.find_element(By.CSS_SELECTOR, ".ais-SearchBox-input").send_keys(Keys.ENTER)
    WebDriverWait(self.driver, 30).until(expected_conditions.presence_of_element_located((By.XPATH, "//input[@value=\'aws,gcp and azure\']")))
    
    #check correct typing string
    elements = self.driver.find_elements(By.XPATH, "//input[@value=\'aws,gcp and azure\']")
    assert len(elements) > 0
    
    #click on pricing button and wait for "Small teams" and  "Pricing and plans" strings
    self.driver.find_element(By.XPATH, "//a[@aria-label=\'Pricing\']").click()
    WebDriverWait(self.driver, 30).until(expected_conditions.presence_of_element_located((By.XPATH, "//div[@id=\'__next\']/div[2]/div/main/div/div[4]/div[1]/div[1]/div[1]/div/div/div[1]/div/div[1]/span[1][contains(text(),\'Small Teams\')]")))
    assert self.driver.find_element(By.XPATH, "//div[@id=\'__next\']/div[2]/div/main/div/div[4]/div[1]/div[1]/div[1]/div/div/div[1]/div/div[1]/span[1][contains(text(),\'Small Teams\')]").text == "Small Teams"
    assert self.driver.find_element(By.XPATH, "//h1").text == "Pricing and plans"

    #click on star now and await of "Everything you need!" strings
    self.driver.find_element(By.XPATH, "//a[contains(@href, '/pricing/plan/enterprise/checkout/?annually=1&seats=5')]").click()
    WebDriverWait(self.driver, 30).until(expected_conditions.presence_of_element_located((By.XPATH, "//*[@id=\"__next\"]/main/div/div[2]/div/div[1]/div/div/div/div[2]/div[2]/span")))
    assert self.driver.find_element(By.XPATH, "//*[@id=\"__next\"]/main/div/div[2]/div/div[1]/div/div/div/div[2]/div[2]/span").text == "Everything you need!"
    
    #fill registration form
    self.driver.find_element(By.XPATH, "//input[@name=\'first_name\']").send_keys("John")
    self.driver.find_element(By.XPATH, "//input[@name=\'last_name\']").send_keys("Appleseed")
    self.driver.find_element(By.XPATH, "//input[@name=\'email\']").send_keys("john.appleseed@test.com")
    self.driver.find_element(By.XPATH, "//input[@name=\'password\']").send_keys("J0hnAppleseed91")
    
    #checking registration form values
    elements = self.driver.find_elements(By.XPATH, "//input[@name=\'first_name\']")
    assert len(elements) > 0
    elements = self.driver.find_elements(By.XPATH, "//input[@name=\'last_name\']")
    assert len(elements) > 0
    elements = self.driver.find_elements(By.XPATH, "//input[@name=\'email\']")
    assert len(elements) > 0
    elements = self.driver.find_elements(By.XPATH, "//input[@name=\'password\']")
    assert len(elements) > 0
    
    
    