import ctypes, sys
from sqlite3 import TimestampFromTicks
import time
import mss
import pyautogui
#from cv2 import cv2
import cv2
import numpy as np
from languaje import myLanguaje
from detectarReputacion import hayBotonReputacionEnPantalla
from imageFinder import printScreen,saveImageTemp
from update import update, getNewUpdate, getVersionControl
from detectFlecha import hayFlechaEnPantalla,haySaltarEnPantalla
from detectAceptar import hayBotonMisionCompletadaEnPantalla,hayBotonAceptarEnPantalla
from expPerhour import expPerHourTick,getExpPerHour,disableExpPerHour
from pintar import pintar

timeBefore = 0
pyautogui.PAUSE = 0.001
pyautogui.FAILSAFE = False
def initTiming():
    global timeBefore
    timeBefore = time.time() * 1000

def printTiming(string=""):
    global timeBefore
    print (string + " " + str(time.time() * 1000 - timeBefore ))

def mouseClick(s=0.200):
    pyautogui.mouseDown()
    time.sleep(s)
    pyautogui.mouseUp()
    return

lastCheckVActive = 0
lastStateVA = False
def isVentanaActiva():
    global lastCheckVActive, lastStateVA
    if (time.time() * 1000) - lastCheckVActive > 2000:
        lastCheckVActive = time.time() * 1000
        ventana = pyautogui.getWindowsWithTitle("CrossWorlds")
        if len(ventana) != 0:
            if ventana[0].isActive:
                lastStateVA = True
                return True
        lastStateVA = False
    return lastStateVA




def main():
    state = "flecha"
    lastSpace = 0
    lastSaltar = 0
    lastTimeExp = 0
    pintar(start = True)
    time.sleep(2)
    par=True
    while True:
        if not isVentanaActiva():
            # disableExpPerHour()
            time.sleep(1)
            continue
        if state == "flecha":
            if par:
                flechaEncontrada = hayFlechaEnPantalla()
                if flechaEncontrada[0]:
                    saltarEncontrado = [None,None]
                    if (time.time() * 1000) -  lastSaltar > 500:
                        saltarEncontrado = haySaltarEnPantalla()
                        lastSaltar = time.time() * 1000
                    if saltarEncontrado[0]:
                        pyautogui.moveTo(1357,830)
                        mouseClick()
                        pyautogui.moveTo(1920/2,1080/2)
                        time.sleep(1/10)
                    else:
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
                    pyautogui.moveTo(1485,1020)
                    mouseClick()
                    time.sleep(1/2)
                    pyautogui.moveTo(163,199)
                    mouseClick()
                    pyautogui.moveTo(1920/2,1080/2)
                    #comprobar si reputaciones
                    time.sleep(5)
                    botonRepu = hayBotonReputacionEnPantalla()
                    if botonRepu[0]:
                        #print("->",botonRepu)
                        pyautogui.moveTo(botonRepu[0][0]+30,botonRepu[0][1]+30) 
                        mouseClick()
                        time.sleep(1/2)
                        pyautogui.moveTo(1160,770)
                        mouseClick()
                botonAceptado = hayBotonAceptarEnPantalla()
                time.sleep(1/5)
                if botonAceptado[0]:
                    pyautogui.moveTo(1485,1020)
                    mouseClick()
                    time.sleep(1/2)
                    pyautogui.moveTo(1920/2,1080/2)
                par=True
        if time.time() * 1000 - lastTimeExp > 3000:
            lastTimeExp = time.time() * 1000
            #expPerHourTick()
            pintar (getExpPerHour())
        if (time.time() * 1000 ) - lastSpace > 10000:
            time.sleep(1/2)
        else:
            time.sleep(1/100)

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

if __name__ == '__main__':
    if not (len(sys.argv) >=2 and sys.argv[1] == "DEV"):
        if not update():
            getNewUpdate()
    elevate()