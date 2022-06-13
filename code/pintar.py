from os import system
from update import getVersionControl
from languaje import myLanguaje

refresh = True
def pintar(str="", start = False):
    global refresh
    version = getVersionControl()
    lang = myLanguaje()
    hello = f""" 
 ███▄▄▄▄    ▄█       ███▄▄▄▄    ▄██████▄          ▄█   ▄█▄ ███    █▄  ███▄▄▄▄    ▄█  
███▀▀▀██▄ ███       ███▀▀▀██▄ ███    ███        ███ ▄███▀ ███    ███ ███▀▀▀██▄ ███  
███   ███ ███▌      ███   ███ ███    ███        ███▐██▀   ███    ███ ███   ███ ███▌ 
███   ███ ███▌      ███   ███ ███    ███       ▄█████▀    ███    ███ ███   ███ ███▌ 
███   ███ ███▌      ███   ███ ███    ███      ▀▀█████▄    ███    ███ ███   ███ ███▌ 
███   ███ ███       ███   ███ ███    ███        ███▐██▄   ███    ███ ███   ███ ███  
███   ███ ███       ███   ███ ███    ███        ███ ▀███▄ ███    ███ ███   ███ ███  
 ▀█   █▀  █▀         ▀█   █▀   ▀██████▀         ███   ▀█▀ ████████▀   ▀█   █▀  █▀   
                                                ▀                                   
   
Anticansancio for Ni No Kuni by OverCraft                                    v{version}

Languaje selected at settings.yaml [ES/EN/PT]:
 -{lang}
"""
    if start:
        print (hello)
        return
    if str!= "":
        if refresh:
            system("CLS")  
            print("" + hello + "\n" + str)
        else:
            print(str)