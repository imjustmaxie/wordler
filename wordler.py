# -*- coding: utf-8 -*-
"""
Created on Sun Mar 20 02:01:20 2022

@author: Evan
"""

from selenium import webdriver
import os,sys
import json

urls = {
    1:"https://www.nytimes.com/games/wordle/index.html",
    2:"https://www.projecteugene.com/katapat.html",
        }
        
def wordle(bSpoiler=False):
    
    options = webdriver.EdgeOptions()
    options.headless = True
    service = os.path.dirname(__file__) + "\edgedriver\msedgedriver.exe"
    #print(service)
    driver = webdriver.ChromiumEdge(executable_path=service,options=options)
    
    inp = input("WORD SOLVER:\n1 - Wordle\n2 - Katapat\nEnter number here: ")
    if int(inp) in urls.keys():
        url = (urls[int(inp)])
        driver.get(url)
    else:
        sys.exit("Invalid input")
    
    scriptArray="""
    return localStorage.getItem(localStorage.key(0))
    """ 	
    result = driver.execute_script(scriptArray)
    result = json.loads(result)
    for k,v in result.items():
        if k == 'solution':
            if bSpoiler == False:
                print("Word of the Day: " + v.replace(v[1:],"☐☐☐☐").upper())
            if bSpoiler == True:
                print("Word of the Day: " + v.upper())
                
ip = input("Spoiler? (T/F): ")
if ip.lower() == 't':
    ip = True
elif ip.lower() == 'f':
    ip = False
wordle(ip)