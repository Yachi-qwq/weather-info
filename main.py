import requests
from requests_html import HTMLSession
import pyfiglet
from datetime import datetime

s = HTMLSession()

try:
    def weather():
        stadt_input = input("Stadt/Ort name: ")
        link = f'https://www.google.com/search?q=weather+{stadt_input}'

        r = s.get(link, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'})

        defentition = r.html.find('span#wob_dc', first=True).text #km/h
        temp = r.html.find('span#wob_tm', first=True).text #first=True stps returning lits °
        niederschlag = r.html.find('span#wob_pp', first=True).text #%
        wind = r.html.find('span#wob_ws', first=True).text #km/h
        Luftfeuchte = r.html.find('span#wob_hm', first=True).text
        #ort = r.html.find('span#wob_loc', first=True).text 
        #date = r.html.find('span#wob_dts', first=True).text #km/h
        now = datetime.now()
        time = now.strftime("%H:%M:%S")

        #layout
        banner = pyfiglet.figlet_format("Wetter")
        print(banner + "\nMade by Yachi.")
        print("." * 40)
        print(f"[{time}] Weather info to {stadt_input}:")
        print("\n ")
        print(f"temp: {defentition} - {temp}°C\n niederschlag: {niederschlag}\n  Luftfeuchte: {Luftfeuchte}\n   wind: {wind}")
        x = "-"
        print("\n" + x*39)

        lmao = input("press the enter key to close . . .")
    weather()

except AttributeError:
    lamo = input("nothing found! Press the enter key to start again . . .\n")
    weather()
