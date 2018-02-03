import pytesseract
import os
from PIL import Image
from selenium import webdriver  
import time
import threading
import math

def CleanText(text):
  text = text.replace(' ','')
  text = text.replace('\n','')
  text = text.replace('_','')
  text = text.replace('?','')
  return text

def RecognizeAndSearch(region, browser, isQuestion):
  text = pytesseract.image_to_string(region, lang = 'chi_sim')
  text = CleanText(text)
  idx_point = None
  idx_quote = []
  if isQuestion:
    for i in range(0,len(text)):
      if text[i] == '.':
        idx_point = i
        break      
      
  browser.get('http://www.baidu.com')  
  
  if not isQuestion:
    browser.find_element_by_id("kw").send_keys('"'+text+'"') 
    browser.find_element_by_id("su").click()
  else:
    if idx_point and idx_point+1 < len(text):
      text = text[idx_point+1:]

    for i in range(0,len(text)):
      if text[i] == '"':
        idx_quote.append(i)
    
    temp = int(math.floor(len(idx_quote) / 2))
    query = ''
    if temp > 0:
      for i in range(0,temp):
        query = query + text[idx_quote[i*2]+1:idx_quote[i*2+1]]
        query = query + ' '
    else:
      query = text    
    print query
    browser.find_element_by_id("kw").send_keys(query) 
    browser.find_element_by_id("su").click()
  

def SearchAnswer():
  # Screenshot
  os.system('adb shell screencap -p /sdcard/temp.png')
  os.system('adb pull /sdcard/temp.png')
  
  # OCR
  pytesseract.pytesseract.tesseract_cmd = 'D:\\Program Files\\Tesseract-OCR\\tesseract'

  tessdata_dir_config = '--tessdata-dir "D:\\Program Files\\Tesseract-OCR\\tessdata"'

  im = Image.open('temp.png')    
  
  box_q = (65,300,1020,650)
  box_c1 = (135,640,925,740)
  box_c2 = (135,825,925,925)
  box_c3 = (135,990,925,1090)
  
  region_q = im.crop(box_q)
  region_c1 = im.crop(box_c1)
  region_c2 = im.crop(box_c2)
  region_c3 = im.crop(box_c3)
  
  threads = []
  
  t0 = threading.Thread(target=RecognizeAndSearch,args=(region_q, browser_q, True,))
  threads.append(t0)
  t1 = threading.Thread(target=RecognizeAndSearch,args=(region_c1, browser_c1, False,))
  threads.append(t1)
  t2 = threading.Thread(target=RecognizeAndSearch,args=(region_c2, browser_c2, False,))
  threads.append(t2)
  t3 = threading.Thread(target=RecognizeAndSearch,args=(region_c3, browser_c3, False,))
  threads.append(t3)
  
  for t in threads:
    t.setDaemon(True)
    t.start()
  
browser_q = None
browser_c1 = None
browser_c2 = None
browser_c3 = None

browser_q = webdriver.Chrome()
browser_q.set_window_size(840,500)
browser_c1 = webdriver.Chrome()
browser_c1.set_window_size(840,500)
browser_c2 = webdriver.Chrome()
browser_c2.set_window_size(840,500)
browser_c3 = webdriver.Chrome()
browser_c3.set_window_size(840,500)
while True:
  inputs = raw_input('Enter anything but q for answer:')
  tickStart = time.time()
  if inputs != 'q':
    SearchAnswer()
  else:
    break
  tickEnd = time.time()
  print tickEnd - tickStart