import pyautogui
import numpy as np
import time
import cv2
from imageFinder import imageFormatToCV2, printScreen, saveImageTemp, findImgOnSource, searchPngOnScreen, searchPngStringOnScreen, imageOffSet 
from languaje import myLanguaje


arrowDetectSCR = cv2.imread("img/flecha.png")
saltarD = cv2.imread("img/saltar.png")

if myLanguaje() == "ES":
    saltarD = cv2.imread("img/saltar.png")
elif myLanguaje() == "EN":
    saltarD = cv2.imread("img/EN/saltar.png")
elif myLanguaje() == "PT":
    saltarD = cv2.imread("img/PT/saltar.png")

def hayFlechaEnPantalla():
    global arrowDetectSCR
    ix,iy,ixx,iyy = 934,988,987,1052
    imageOffSet(0,0,1920,1080)
    imageScreen = imageFormatToCV2(printScreen(ix,iy,ixx,iyy)) # argumentos opcionales si es todo
    return findImgOnSource(arrowDetectSCR, imageScreen)

def haySaltarEnPantalla():
    global saltarD
    ix,iy,ixx,iyy = 1279,800,1428,850
    imageOffSet(0,0,1920,1080)
    imageScreen = imageFormatToCV2(printScreen(ix,iy,ixx,iyy)) # argumentos opcionales si es todo
    return findImgOnSource(saltarD, imageScreen)

def main():
    exit()

if __name__ == "__main__":
    main()