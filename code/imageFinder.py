from glob import glob
from turtle import width
import cv2
import time
import mss
import pyautogui
import numpy as np

timeBefore = 0
#offset es la esquina donde empieza la pantalla
gOffSetY = 282
gOffSetX = 68
#ancho y largo de la pantalla
gWidth = 960
gHeight = 540
def imageOffSet(x,y,w,h):
    global gOffSetY
    global gOffSetX
    global gWidth
    global gHeight
    gOffSetY = y
    gOffSetX = x
    gWidth = w
    gHeight = h

def initTiming():
    global timeBefore
    timeBefore = time.time() * 1000

def printTiming(string=""):
    global timeBefore
    print (string + " " + str(time.time() * 1000 - timeBefore))

gMonitorNumber = 1
def setMonitorNumber(m=1):
    gMonitorNumber = m
def printScreen(offSetX=0, offSetY=0, maxX=0, maxY=0):
    with mss.mss() as sct:
        global gMonitorNumber
        monitor_number = gMonitorNumber
        mon = sct.monitors[monitor_number]

        # The screen part to capture
        global gOffSetY
        global gOffSetX
        width = gWidth
        height = gHeight
        if maxX != 0 and offSetX!=0 and offSetX < maxX:
            width = maxX - offSetX
        if maxY != 0 and offSetY!=0 and offSetY < maxY:
            height = maxY - offSetY
        monitor = {
            "top": mon["top"] + gOffSetY + offSetY,  # 100px from the top
            "left": mon["left"] + gOffSetX + offSetX,  # 100px from the left
            "width": width,
            "height": height,
            "mon": monitor_number,
        }
        image = sct.grab(monitor)
        return image

def imageFormatToCV2(image):
    if image is not None:
        preArrayNp = np.array(image)
        return preArrayNp[:,:,:3]

def findImgOnSource(img, source, rango = 0.8 ):
    result = cv2.matchTemplate(source,img,cv2.TM_CCOEFF_NORMED)
    #cv2.imshow("tal", result)
    #cv2.waitKey(0)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    
    if max_val >= rango:
        return max_loc, max_val
    return [None,None]

def saveImageTemp(image, file="out"):
    if image is not None:
        mss.tools.to_png(image.rgb, image.size, output="test/"+file+".png")

def saveScreenShoot():
    saveImageTemp(printScreen(), str(time.time()))


#precision en la igualdad de las imágenes
precision = 0.9
def setPrecision(p):
    global precision
    precision = p
# ix iy ixx iyy its a rect optional inside screen
def searchPngStringOnScreen(string, ix = 0,iy = 0,ixx = 0,iyy = 0):
    if string is not None:
        imageScreen = imageFormatToCV2(printScreen(ix,iy,ixx,iyy))
        img = cv2.imread(string)
        if img is not None:
            ancho = img.shape[0]
            alto = img.shape[1]
            global precision
            rectangles, value = findImgOnSource(img,imageScreen,precision)
            if rectangles is None or len(rectangles) == 0:
                return [None,None]
            else:
                x,y= rectangles[0], rectangles[1]
                # print ("ancho y alto", ancho, alto)
                return gOffSetX+ x+ ix + (alto//2), gOffSetY+ y+iy + (ancho//2)
    return [None,None]

def searchPngOnScreen(img, ix = 0,iy = 0,ixx = 0,iyy = 0):
    if img is not None:
        imageScreen = imageFormatToCV2(printScreen(ix,iy,ixx,iyy))
        #img = cv2.imread(string)
        if img is not None:
            ancho = img.shape[0]
            alto = img.shape[1]
            global precision
            rectangles, value = findImgOnSource(img,imageScreen,precision)
            if rectangles is None or len(rectangles) == 0:
                return [None,None]
            else:
                x,y= rectangles[0], rectangles[1]
                # print ("ancho y alto", ancho, alto)
                return gOffSetX+ x+ ix + (alto//2), gOffSetY+ y+iy + (ancho//2)
    return [None,None]

def main():
    print ("Cambia de ventana antes de 2s")
    time.sleep(2)
    initTiming()
    # printTiming("total")
    ix,iy,ixx,iyy = 370,209,570,280
    imageScreen = imageFormatToCV2(printScreen(ix,iy,ixx,iyy)) # argumentos opcionales si es todo
    img = cv2.imread('img/volverAJugar.png')
    #result = cv2.matchTemplate(search,imageScreen,cv2.TM_CCOEFF_NORMED)
    #cv2.imshow("Original", result)
    #cv2.waitKey(0)
    rectangles, value = findImgOnSource(img,imageScreen,0.9)
    if rectangles is None or len(rectangles) == 0:
        print ("no encontrado")
    else:
        print ("encontrado")
        # x, y, w, h = rectangles[0]
        # centerX = x+w/2
        # centerY = y+y/2
        # print ("first match rectangles", x, y, w, h)
        # pyautogui.moveTo(x,y)
        x,y= rectangles[0], rectangles[1]
        pyautogui.moveTo(gOffSetX+ x+ ix, gOffSetY+ y+iy)
        print (rectangles, value)
    printTiming("total")
    # saveScreenShoot()
    pyautogui.moveTo(searchPngStringOnScreen('img/volverAJugar.png',332, 176, 571, 513))
    printTiming("ps")
    pyautogui.moveTo(searchPngOnScreen(cv2.imread('img/volverAJugar.png'),332, 176, 571, 513))
    printTiming("p")

    

if __name__ == "__main__":
    main()