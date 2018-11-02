import re 
import os
import pytest
import textwrap
from appium import webdriver
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO
import time
from guide_mobile import *

arquivo = open("calculadora.md")

regex = re.compile(r'```(?:javascript|js)([\s\S]+?)```')

matches = regex.findall(arquivo.read())
for command in matches :
    exec(command)
