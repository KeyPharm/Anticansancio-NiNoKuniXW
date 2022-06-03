from asyncio.windows_events import NULL
import pyautogui
import numpy as np
import time
import cv2
from imageFinder import imageFormatToCV2, printScreen, saveImageTemp, findImgOnSource, searchPngOnScreen, searchPngStringOnScreen, imageOffSet 
from languaje import myLanguaje

arrowDetectSCR = cv2.imread("img/missionCompletada.png")
botonAceptar = cv2.imread("img/botonAceptar.png")
if myLanguaje() == "ES":
    arrowDetectSCR = cv2.imread("img/missionCompletada.png")
    botonAceptar = cv2.imread("img/botonAceptar.png")
elif myLanguaje() == "PT":
    arrowDetectSCR = cv2.imread("img/PT/missionCompletada.png")
    botonAceptar = cv2.imread("img/PT/botonAceptar.png")

def hayBotonMisionCompletadaEnPantalla():
    global arrowDetectSCR
    ix,iy,ixx,iyy = 1552,994,1812,1070
    imageOffSet(0,0,1920,1080)
    imageScreen = imageFormatToCV2(printScreen(ix,iy,ixx,iyy)) # argumentos opcionales si es todo
    return findImgOnSource(arrowDetectSCR, imageScreen, 0.85)
def hayBotonAceptarEnPantalla():
    global botonAceptar
    ix,iy,ixx,iyy = 1552,994,1812,1070
    imageOffSet(0,0,1920,1080)
    imageScreen = imageFormatToCV2(printScreen(ix,iy,ixx,iyy)) # argumentos opcionales si es todo
    return findImgOnSource(botonAceptar, imageScreen, 0.85)