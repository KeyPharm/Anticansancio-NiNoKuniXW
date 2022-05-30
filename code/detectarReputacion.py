import pyautogui
import numpy as np
import time
import cv2
from imageFinder import imageFormatToCV2, printScreen, saveImageTemp, findImgOnSource, searchPngOnScreen, searchPngStringOnScreen, imageOffSet
import ctypes, sys

cuadroRep = cv2.imread("img/cuadroRep.png")
def hayBotonReputacionEnPantalla():
    global cuadroRep
    ix,iy,ixx,iyy = 0,0 ,1920,1080
    imageOffSet(0,0,1920,1080)
    imageScreen = imageFormatToCV2(printScreen(ix,iy,ixx,iyy)) # argumentos opcionales si es todo
    return findImgOnSource(cuadroRep, imageScreen,0.4)

""" def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

if is_admin(): #code of admin
    time.sleep(2)
    resultado = hayBotonReputacionEnPantalla()
    print (resultado)
    pyautogui.moveTo(resultado[0][0],resultado[0][1])
else:
    # Re-run the program with admin rights
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1) """