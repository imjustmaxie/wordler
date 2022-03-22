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
    21:"https://www.nsfwordle.com/",
    22:"https://lordcris.github.io/wordle-bg/",
    23:"https://esperanto.cat/wordleo/",
    24:"https://hulihua.net/",
    25:"https://palabro-silk.vercel.app/",
    26:"https://buddhistuniversity.net/wordle-thai/",
        }
        
def wordle(bSpoiler=False):
    
    options = webdriver.EdgeOptions()
    options.headless = True
    service = os.path.dirname(__file__) + "\edgedriver\msedgedriver"
    if sys.platform == 'win32':
        service += ".exe"
    elif sys.platform == 'linux':
        service += "_linux"
    elif sys.platform == 'darwin':
        service += "_mac"
    
    driver = webdriver.ChromiumEdge(executable_path=service,options=options)

    lists = ['solution','board','games']
    
    inp = input("""WORDLER (WORD GUESS REVEALER):

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
21 - NSFWordle
22 - Уърдли (Bulgarian Wordle)
23 - Wordleo (Esperanto Wordle)
24 - Hulihua (Hawaiian Wordle)
25 - Palabro (Brazilian Portuguese Wordle)
26 - เวิร์ดเดลไทย (Thai Wordle)

Enter number here: """)
    if int(inp) in urls.keys():
        url = urls[int(inp)]
        driver.get(url)
    else:
        sys.exit("Invalid input.\nExiting...")
    
    scriptArray=""" for (var kay in localStorage) {
        return localStorage.getItem(localStorage.key(kay))
    }
    
    """
    result = driver.execute_script(scriptArray)
    try:
        result = json.loads(result)
    except TypeError:
        sys.exit("Error")
    os.system('cls')
    for k,v in result.items():
        if k in lists:
            if bSpoiler == False:
                print("First Letter of the Day: " + v[:1].upper())
            if bSpoiler == True:
                print("Word of the Day: " + v.upper())

ip = input("Allow Word of the Day spoiler? (Y/N): ")
if ip.lower() == 'y':
    ip = True
elif ip.lower() == 'n':
    ip = False
else:
    sys.exit("Invalid input.\nExiting...")
wordle(ip)