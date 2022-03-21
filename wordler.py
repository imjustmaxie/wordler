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
    3:"https://arwordle.netlify.app/",
    4:"https://kelmaly.com/",
    5:"https://levantdle.netlify.app/",
    6:"https://jordle.jovid.win/home",
    7:"https://woertchen.sofacoach.de/",
    8:"https://hshabdak1.d3kupkqgygqmeu.amplifyapp.com/",
    9:"https://taximanli.github.io/kotobade-asobou/",
    10:"https://tlembung.vercel.app/",
    11:"https://malay-wordle.netlify.app/",
    12:"https://words.hk/static/bopomofo-wordle/",
    13:"https://nakosung.github.io/wordle/",
    14:"https://facle.netlify.app/",
    15:"https://omtamil.com/soladle/",
    16:"https://slivce.com/",
    17:"https://www.bundle.app/wordle-tr/",
    18:"https://weredle.netlify.app/",
    19:"https://bts-wordle.vercel.app/",
    20:"https://www.emotele.xyz/",
        }
        
def wordle(bSpoiler=False):
    
    options = webdriver.EdgeOptions()
    options.headless = True
    service = os.path.dirname(__file__) + "\edgedriver\msedgedriver.exe"
    #print(service)
    driver = webdriver.ChromiumEdge(executable_path=service,options=options)

    lists = ['solution','board','games']
    
    inp = input("""WORD SOLVER:

1 - Wordle
2 - Katapat (Malay Wordle)
3 - AlWird (Arabic Wordle)
4 - Kelmaly (Arabic Wordle)
5 - Levantdle (Levantine Arabic Wordle)
6 - Jordle
7 - Wörtchen (German Wordle)
8 - शब्दल (Hindi Wordle)
9 - Kotobade Asobou (Japanese Wordle)
10 - Tlembung (Javanese Wordle)
11 - Malay-Wordle (Malay Wordle)
12 - 注音版 Wordle (Mandarin BOPOMOFO Wordle)
13 - Wordle (한글 풀어쓰기 5자) (Korean Wordle)
14 - Facle (Scottish Gaelic Wordle)
15 - சொல்லாடல் (Tamil Wordle)
16 - Слівце (Ukrainian Wordle)
17 - Wordle TR (Turkish Wordle)
18 - Weredle (Wordle with Werewolf twist)
19 - BTS Wordle
20 - Emotele (Twitch Emote Wordle)

Enter number here: """)
    if int(inp) in urls.keys():
        url = (urls[int(inp)])
        driver.get(url)
    else:
        sys.exit("Invalid input")
    
    scriptArray=""" for (var kay in localStorage) {
        return localStorage.getItem(localStorage.key(kay))
    }
    
    """
    result = driver.execute_script(scriptArray)
    result = json.loads(result)
    for k,v in result.items():
        if k in lists:
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