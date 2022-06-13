import datetime
from math import trunc
from cgitb import text
from pprint import isreadable
import time
from tracemalloc import start
from imageFinder import imageFormatToCV2, printScreen, saveImageTemp, findImgOnSource, searchPngOnScreen, searchPngStringOnScreen, imageOffSet 
import numpy as np
import cv2
from pintar import pintar


def isImagePerFound(array1 = [0,0,0],array2 = [0,0,0]):
    if (array1 [0] == 174 and array2[0] == 174) and (array1 [1] == 212 and array2[1] == 212) and (array1 [2] == 82 and array2[2] == 82):
        return True
    return False

def foundPixelFast(tablaColor):
    lastColor = [174,212,82]
    contador = 2 #es el número real. 1 ,2 , 3 sin empezar en 0. el bucle se sale en 1921
    #el primer pixel no es el color turquesa, empieza en el segundo pixel
    for y in range(1,1920):
        x = tablaColor[0][y]
        if not (x[0] == lastColor[0] and x[1] == lastColor[1] and x[2] == lastColor[2]):
            lastColor = x
            break
        contador = contador + 1
    if contador == 1921:
        contador = 1920
    return contador

def calcPorcentaje(imageScreen):
    porcentaje = (foundPixelFast(imageScreen) * 100) / 1920
    return porcentaje

isRunning = False
isSetted = False
startTimeRunning = 0
startPorcentaje = 0
texto = ""
lastPixelPerfectanje = 0
lastPixelPerfectanjeTime = 0
diff = ""


def getExpPerHour():
    global texto,isRunning,isSetted
    if isRunning and isSetted and texto != "":
        returnTexto = "" + texto + " Time leveling: " + str (datetime.timedelta(seconds =(trunc((time.time()*1000 - startTimeRunning)/1000)))) + "s"
        if diff != "":
            returnTexto = returnTexto + "\nDetected Exp Pixel Bar change after: " + str (diff) + "s"
        return returnTexto
    return ""

def disableExpPerHour():
    global isRunning,startTimeRunning,startPorcentaje,texto,isSetted,lastPixelPerfectanje,lastPixelPerfectanjeTime, diff
    isRunning = False
    startTimeRunning = 0
    startPorcentaje = 0
    isSetted = False
    texto = ""
    lastPixelPerfectanje = 0
    lastPixelPerfectanjeTime = 0
    diff = ""

def expPerHourTick():
    global isRunning, startTimeRunning, startPorcentaje, texto, isSetted, lastPixelPerfectanje,lastPixelPerfectanjeTime,diff
    ix,iy,ixx,iyy = 0,1080-1,1920,1080
    imageOffSet(0,0,1920,1080)
    imageScreen = imageFormatToCV2(printScreen(ix,iy,ixx,iyy))
    if len(imageScreen[0])==1920 and (isImagePerFound(imageScreen[0,1],imageScreen[0,2])):
        if isRunning:
            currentP = calcPorcentaje(imageScreen)
            if startPorcentaje > currentP:
                disableExpPerHour()
                return
            else:
                if startPorcentaje - currentP != 0:
                    if not isSetted:
                        #start now
                        isSetted=True
                        startPorcentaje=currentP
                        startTimeRunning= time.time() * 1000
                        texto = "Percentage Per Hour = " + "0%"
                        lastPixelPerfectanje=currentP
                        lastPixelPerfectanjeTime = time.time()*1000
                        return
                    if lastPixelPerfectanje != currentP:
                        diff = datetime.timedelta(seconds =trunc(((time.time()*1000 - lastPixelPerfectanjeTime)/1000)))
                        lastPixelPerfectanje = currentP
                        lastPixelPerfectanjeTime = time.time()*1000
                    texto = "Percentage Per Hour = " + str(round((currentP - startPorcentaje) / (time.time() * 1000 - startTimeRunning) * 3600000,2))+"%"
                else:
                    texto = "Percentage Per Hour = " + "0%"
        else:
            isRunning = True
            startTimeRunning= time.time() * 1000
            startPorcentaje = calcPorcentaje(imageScreen)


lastDetect = 0
detected = False


if __name__ == "__main__":
    time.sleep(60)
