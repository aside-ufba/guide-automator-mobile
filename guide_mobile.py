import re 
import os
import pytest
import textwrap
from appium import webdriver
from PIL import Image, ImageDraw, ImageFont
import io
import time
from IPython.display import display
from appium.webdriver.common.touch_action import TouchAction

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
actions = None

def init():
    global driver
    driver = load_driver()    
    actions = TouchAction(driver)

def takeScreenshot():    
    display(Image.open(io.BytesIO(driver.get_screenshot_as_png())))

def takeScreenshotElement(id):    
    global driver
    element = driver.find_element_by_id(id)
    location = element.location
    size = element.size
    png = driver.get_screenshot_as_png()
    img = Image.open(io.BytesIO(png))
    left = location['x']
    top = location['y']
    right = location['x'] + size['width']
    bottom = location['y'] + size['height']
    img = img.crop((int(left), int(top), int(right), int(bottom)))    
    display(img)

# highlight
def highlightElement(id, rectangleWidht = 5):    

    global driver
    element = driver.find_element_by_id(id)
    location = element.location
    size = element.size
    
    img = Image.open(io.BytesIO(driver.get_screenshot_as_png())).convert('RGB')
    left = location['x']
    top = location['y']
    right = location['x'] + size['width']
    bottom = location['y'] + size['height']

    draw = ImageDraw.Draw(img)
    draw.rectangle(((int(left), int(top)), (int(right), int(bottom))), outline="#FF0000", width=rectangleWidht)    
    
    display(img)    

def sleep(time_steep):
    time.sleep(time_steep)

def click(id):
    global driver
    driver.find_element_by_id(id).click()

def sendKeys(id, text):
    global driver
    driver.find_element_by_id(id).sendKeys(text)

def getText(id):
    global driver
    return driver.find_element_by_id(id).text

def scrolltoElement(id):
    global driver
    return driver.find_element_by_id(id).location_once_scrolled_into_view

def setLandscapeOrientation():
    driver.orientation = "LANDSCAPE"

def setPortraitOrientation():
    driver.orientation = "PORTRAIT"

def quit():
    global driver
    driver.quit()

# Operations with touch
def tab(id, pCount=1):
    global driver, actions
    actions.tap(driver.find_element_by_id(id), count=pCount)
    actions.release()
    actions.perform()

def press(id):
    global driver, actions
    actions = TouchAction(driver)
    actions.press(driver.find_element_by_id(id))    
    actions.release()
    actions.perform()

def longPress(id, pDuration):
    global driver, actions
    actions = TouchAction(driver)
    actions.long_press(driver.find_element_by_id(id), duration=pDuration)
    actions.release()
    actions.perform()

def move_to_direction(id, idDirection):
    actions = TouchAction(driver)
    actions.press(driver.find_element_by_id(id))
    actions.move_to(driver.find_element_by_id(idDirection))
    actions.release()
    actions.perform()

