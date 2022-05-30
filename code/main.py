import ctypes, sys
from sqlite3 import TimestampFromTicks
import time
import mss
import pyautogui
#from cv2 import cv2
import cv2
import numpy as np
from detectarReputacion import hayBotonReputacionEnPantalla
from imageFinder import printScreen,saveImageTemp
from detectFlecha import hayFlechaEnPantalla
from detectAceptar import hayBotonMisionCompletadaEnPantalla,hayBotonAceptarEnPantalla
from update import update

timeBefore = 0
pyautogui.PAUSE = 0.001
pyautogui.FAILSAFE = False
def initTiming():
    global timeBefore
    timeBefore = time.time() * 1000

def printTiming(string=""):
    global timeBefore
    print (string + " " + str(time.time() * 1000 - timeBefore ))

def main():
    state = "flecha"
    lastSpace = 0
    #initTiming()
    #time.sleep(2)
    #printTiming("Programa total exec time:")
    hello = """ 
 ███▄▄▄▄    ▄█       ███▄▄▄▄    ▄██████▄          ▄█   ▄█▄ ███    █▄  ███▄▄▄▄    ▄█  
███▀▀▀██▄ ███       ███▀▀▀██▄ ███    ███        ███ ▄███▀ ███    ███ ███▀▀▀██▄ ███  
███   ███ ███▌      ███   ███ ███    ███        ███▐██▀   ███    ███ ███   ███ ███▌ 
███   ███ ███▌      ███   ███ ███    ███       ▄█████▀    ███    ███ ███   ███ ███▌ 
███   ███ ███▌      ███   ███ ███    ███      ▀▀█████▄    ███    ███ ███   ███ ███▌ 
███   ███ ███       ███   ███ ███    ███        ███▐██▄   ███    ███ ███   ███ ███  
███   ███ ███       ███   ███ ███    ███        ███ ▀███▄ ███    ███ ███   ███ ███  
 ▀█   █▀  █▀         ▀█   █▀   ▀██████▀         ███   ▀█▀ ████████▀   ▀█   █▀  █▀   
                                                ▀                                   
   
Anticansancio para Ni No Kuni by OverCraft                                    v0.1
"""
    print (hello)
    time.sleep(2)
    par=True
    while True:
        if state == "flecha":
            if par:
                flechaEncontrada = hayFlechaEnPantalla()
                if flechaEncontrada[0]:
                    pyautogui.keyDown('space')
                    time.sleep(1/30)
                    pyautogui.keyUp('space')
                    time.sleep(1/30)
                    lastSpace = time.time() * 1000
                else:
                    par=False
            else:
                botonMisionEncontrado = hayBotonMisionCompletadaEnPantalla()
                if botonMisionEncontrado[0]:
                    #print("----",botonMisionEncontrado[0],"sdf",botonMisionEncontrado[1])
                    pyautogui.moveTo(1485,1020) #botonMisionEncontrado[0][0], botonMisionEncontrado[0][1])
                    pyautogui.click()
                    time.sleep(1/3)
                    pyautogui.moveTo(163,199)
                    pyautogui.click()
                    pyautogui.moveTo(0,0)
                    #comprobar si reputaciones
                    time.sleep(5)
                    botonRepu = hayBotonReputacionEnPantalla()
                    if botonRepu[0]:
                        print("->",botonRepu)
                        pyautogui.moveTo(botonRepu[0][0]+30,botonRepu[0][1]+30) 
                        pyautogui.click()
                        time.sleep(1/3)
                        pyautogui.moveTo(1160,770)
                        pyautogui.click()
                botonAceptado = hayBotonAceptarEnPantalla()
                time.sleep(1/5)
                if botonAceptado[0]:
                    #print("----",botonMisionEncontrado[0],"sdf",botonMisionEncontrado[1])
                    pyautogui.moveTo(1485,1020) #botonMisionEncontrado[0][0], botonMisionEncontrado[0][1])
                    pyautogui.click()
                    time.sleep(1/3)
                    pyautogui.moveTo(0,0)
                par=True

        if (time.time() * 1000 ) - lastSpace > 1000:
            time.sleep(1/2)
        else:
            time.sleep(1/30)

def elevate():
    def is_admin():
        try:
            return ctypes.windll.shell32.IsUserAnAdmin()
        except:
            return False

    if is_admin(): #code of admin
        main()
    else:
        # Re-run the program with admin rights
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)

def getNewUpdate():
    import os, requests, zipfile, io, shutil, sys
    from pathlib import Path
    dir = os.getcwd()
    r = requests.get("https://github.com/KeyPharm/Anticansancio-NiNoKuniXW/archive/refs/heads/main.zip", stream=True)
    if r:
        z = zipfile.ZipFile(io.BytesIO(r.content))
        if "Anticansancio-NiNoKuniXW-main/" in z.namelist():
            source_dir = dir + "\\" + "Anticansancio-NiNoKuniXW-main\\"
            target_dir = dir + "\\"
            z.extractall(dir)
            shutil.copytree(source_dir, target_dir, dirs_exist_ok=True)
            #shutil.rmtree(source_dir)
        print("Restarting...")
        sys.stdout.flush()
        os.execl(sys.executable, 'python code\\main.py', *sys.argv[1:])

if __name__ == '__main__':
    if not update():
        getNewUpdate()
    elevate()
#<time.sleep(5)