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

# def load_driver():
#         # calling_request = request._pyfuncitem.name
#         driver = webdriver.Remote(
#             command_executor= 'http://127.0.0.1:4723/wd/hub',
#             desired_capabilities={                
#                 'platformName': 'Android',
#                 'automationName': 'UIAutomator2',
#                 'platformVersion': '8.0',
#                 'deviceName': '0045816737',
#                 "appPackage": "com.google.android.calculator",
#                 "appActivity": "com.android.calculator2.Calculator",
#                 "noReset": "true",
#                 "full-reset": "false"
#             }
#         )        

#         driver.implicitly_wait(10)
#         return driver


def load_driver():
        # calling_request = request._pyfuncitem.name
        driver = webdriver.Remote(
            command_executor= 'http://127.0.0.1:4723/wd/hub',
            desired_capabilities={                
                'automationName': 'UIAutomator2',
                'platformName': 'Android',                
                'platformVersion': '8.0',
                "noReset": "true",
                "full-reset": "false",
                "deviceName": "0045816737",
                "appPackage": "com.google.android.contacts",
                "appActivity": "com.android.contacts.activities.ContactsFrontDoor"                
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

def takeScreenshotElementById(id):    
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

def takeScreenshotElementAccessibilityId(id):
    global driver
    element = driver.find_element_by_accessibility_id(id)
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

def takeScreenshotElementXpath(id):
    global driver
    element = driver.find_element_by_xpath(id)
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
def highlightElementById(id, rectangleWidht = 5):    

    global driver
    
    idList = id.split(',')
    img = Image.open(io.BytesIO(driver.get_screenshot_as_png())).convert('RGB')
    for idItem in idList:
        element = driver.find_element_by_id(idItem.strip())
        location = element.location
        size = element.size        
        
        left = location['x']
        top = location['y']
        right = location['x'] + size['width']
        bottom = location['y'] + size['height']

        draw = ImageDraw.Draw(img)
        draw.rectangle(((int(left), int(top)), (int(right), int(bottom))), outline="#FF0000", width=rectangleWidht)    
    
    display(img)    

def highlightElementByAccessibilityId(id, rectangleWidht = 5):    

    global driver
    
    idList = id.split(',')
    img = Image.open(io.BytesIO(driver.get_screenshot_as_png())).convert('RGB')
    for idItem in idList:
        element = driver.find_element_by_accessibility_id(idItem.strip())
        location = element.location
        size = element.size        
        
        left = location['x']
        top = location['y']
        right = location['x'] + size['width']
        bottom = location['y'] + size['height']

        draw = ImageDraw.Draw(img)
        draw.rectangle(((int(left), int(top)), (int(right), int(bottom))), outline="#FF0000", width=rectangleWidht)    
    
    display(img)    

def highlightElementByXpath(xpath, rectangleWidht = 5):    

    global driver
    
    xpathList = xpath.split(',')
    img = Image.open(io.BytesIO(driver.get_screenshot_as_png())).convert('RGB')
    for xpathItem in xpathList:
        element = driver.find_element_by_xpath(xpathItem.strip())
        location = element.location
        size = element.size        
        
        left = location['x']
        top = location['y']
        right = location['x'] + size['width']
        bottom = location['y'] + size['height']

        draw = ImageDraw.Draw(img)
        draw.rectangle(((int(left), int(top)), (int(right), int(bottom))), outline="#FF0000", width=rectangleWidht)    
    
    display(img) 

def sleep(time_steep):
    time.sleep(time_steep)

# click
def clickByID(id):
    global driver
    driver.find_element_by_id(id).click()

def clickByAccessibilityId(id):
    global driver
    driver.find_element_by_accessibility_id(id).click()

def clickByXPath(xpath):
    global driver    
    driver.find_element_by_xpath(xpath).click()

# sendkeys
def sendKeysByID(id, text):
    global driver
    driver.find_element_by_id(id).sendKeys(text)

def sendKeysByAccessibilityId(id, text):
    global driver
    driver.find_element_by_accessibility_id(id).sendKeys(text)

def sendKeysByXpath(xpath, text):
    global driver
    driver.find_element_by_xpath(xpath).sendKeys(text)

# getText
def getTextById(id):
    global driver
    return driver.find_element_by_id(id).text

def getTextByAccessibilityId(id):
    global driver
    return driver.find_element_by_accessibility_id(id).text

def getTextByXpath(xpath):
    global driver
    return driver.find_element_by_xpath(xpath).text

# scrolltoElement
def scrolltoElementById(id):
    global driver, actions
    actions = TouchAction(driver)
    element = driver.find_element_by_id(id)
    print (element)
    actions.move_to(el=element).perform()

def scrolltoElementByAccessibilityId(id):
    global driver, actions
    actions = TouchAction(driver)
    element = driver.find_element_by_accessibility_id(id)
    print (element)
    actions.move_to(el=element).perform()

def scrolltoElementByXpath(xpath):
    global driver, actions
    actions = TouchAction(driver)
    element = driver.find_element_by_xpath(xpath)
    print (element)
    actions.move_to(el=element).perform()

def setLandscapeOrientation():
    driver.orientation = "LANDSCAPE"

def setPortraitOrientation():
    driver.orientation = "PORTRAIT"

def quit():
    global driver
    driver.quit()

# Operations with touch
# gtab
def tabById(id, pCount=1):
    global driver, actions
    actions = TouchAction(driver)
    actions.tap(driver.find_element_by_id(id), count=pCount)
    actions.release()
    actions.perform()

def tabByAccessibilityId(id, pCount=1):
    global driver, actions
    actions = TouchAction(driver)
    actions.tap(driver.find_element_by_accessibility_id(id), count=pCount)
    actions.release()
    actions.perform()

def tabByAccessibilityXpath(xpath, pCount=1):
    global driver, actions
    actions = TouchAction(driver)
    actions.tap(driver.find_element_by_xpath(xpath), count=pCount)
    actions.release()
    actions.perform()

# press
def pressById(id):
    global driver, actions    
    actions.press(driver.find_element_by_id(id))    
    actions.release()
    actions.perform()

def pressByAccessibility_id(id):
    global driver, actions    
    actions.press(driver.find_element_by_accessibility_id(id))    
    actions.release()
    actions.perform()

def pressByXpath(xpath):
    global driver, actions    
    actions.press(driver.find_element_by_xpath(xpath))
    actions.release()
    actions.perform()

# longPress
def longPressById(id, pDuration):
    global driver, actions    
    actions.long_press(driver.find_element_by_id(id), duration=pDuration)
    actions.release()
    actions.perform()

def longPressByAccessibilityId(id, pDuration):
    global driver, actions    
    actions.long_press(driver.find_element_by_accessibility_id(id), duration=pDuration)
    actions.release()
    actions.perform()

def longPressByXpath(id, pDuration):
    global driver, actions    
    actions.long_press(driver.find_element_by_xpath(id), duration=pDuration)
    actions.release()
    actions.perform()

# moveToDirection
def moveToDirectionByID(id, idDirection):    
    actions.press(driver.find_element_by_id(id))
    actions.move_to(driver.find_element_by_id(idDirection))
    actions.release()
    actions.perform()

def moveToDirectionByAccessibilityId(id, idDirection):    
    actions.press(driver.find_element_by_accessibility_id(id))
    actions.move_to(driver.find_element_by_accessibility_id(idDirection))
    actions.release()
    actions.perform()

def moveToDirectionByXpath(xpath, xpathDirection):    
    actions.press(driver.find_element_by_xpath(xpath))
    actions.move_to(driver.find_element_by_xpath(xpathDirection))
    actions.release()
    actions.perform()
