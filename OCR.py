import pytesseract
import os
from PIL import Image
from selenium import webdriver  
import time

def SearchAnswer():
  # Screenshot
  os.system('adb shell screencap -p /sdcard/temp.png')
  os.system('adb pull /sdcard/temp.png')
  
  # OCR
  pytesseract.pytesseract.tesseract_cmd = 'D:\\Program Files\\Tesseract-OCR\\tesseract'

  tessdata_dir_config = '--tessdata-dir "D:\\Program Files\\Tesseract-OCR\\tessdata"'

  im = Image.open('temp.png')
  box = (65,300,1020,650)
  region = im.crop(box)
  text = pytesseract.image_to_string(region, lang = 'chi_sim')
  text = text.replace(' ','')
  text = text.replace('\n','')
  text = text.replace('_','')
  text = text.replace('?','')
  for i in range(0,len(text)):
    if text[i] == '.':
      break
  print text

  # Search results 
  options.get('http://www.baidu.com')  
  
  if i+1 < len(text):
    options.find_element_by_id("kw").send_keys(text[i+1:]) 
    options.find_element_by_id("su").click()

options = None

options = webdriver.Chrome()  
options.maximize_window()
while True:
  inputs = raw_input('Enter anything but q for answer:')
  tickStart = time.time()
  if inputs != 'q':
    SearchAnswer()
  else:
    break
  tickEnd = time.time()
  print tickEnd - tickStart