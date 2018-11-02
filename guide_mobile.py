import re 
import os
import pytest
import textwrap
from appium import webdriver
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO
import time

def load_driver():
        # calling_request = request._pyfuncitem.name
        driver = webdriver.Remote(
            command_executor= 'http://127.0.0.1:4723/wd/hub',
            desired_capabilities={                
                'platformName': 'Android',
                'automationName': 'UIAutomator2',
                'platformVersion': '8.0',
                'deviceName': '0045816737',
                "appPackage": "com.google.android.calculator",
                "appActivity": "com.android.calculator2.Calculator",
                "noReset": "true",
                "full-reset": "false"
            }
        )        

        driver.implicitly_wait(10)
        return driver

driver = None
screenshotName = None

def init():
    global driver, screenshotName
    driver = load_driver()
    screenshotName = 0

def click(id):
    global driver
    driver.find_element_by_id(id).click()

def takeScreenshot():
    global driver, screenshotName
    screenshotName+=1
    driver.save_screenshot(str(screenshotName)+".png")

def takeScreenshotElement(id):    
    global driver, screenshotName
    element = driver.find_element_by_id(id)
    location = element.location
    size = element.size
    png = driver.get_screenshot_as_png()
    img = Image.open(BytesIO(png))
    left = location['x']
    top = location['y']
    right = location['x'] + size['width']
    bottom = location['y'] + size['height']
    img = img.crop((int(left), int(top), int(right), int(bottom)))
    img.height    
    screenshotName+=1
    img.save(str(screenshotName)+".png")
    
def sendKeys(id, text):
    global driver
    driver.find_element_by_id(id).sendKeys(text)

# highlight
def highlightElement(id, rectangleWidht = 5):    

    global driver, screenshotName
    screenshotName+=1
    nameImg = str(screenshotName)+".png"
    driver.save_screenshot(nameImg)

    element = driver.find_element_by_id(id)
    location = element.location
    size = element.size
    
    img = Image.open(nameImg).convert('RGB')
    left = location['x']
    top = location['y']
    right = location['x'] + size['width']
    bottom = location['y'] + size['height']

    draw = ImageDraw.Draw(img)
    draw.rectangle(((int(left), int(top)), (int(right), int(bottom))), outline="#FF0000", width=rectangleWidht)    
    del draw

    img.save(nameImg)
    

def getText(id):
    global driver
    return driver.find_element_by_id(id).text

def scrolltoElement(id):
    global driver
    return driver.find_element_by_id(id).location_once_scrolled_into_view

def quit():
    global driver
    driver.quit()