import pyautogui
import numpy as np
import time
import cv2
from imageFinder import imageFormatToCV2, printScreen, saveImageTemp, findImgOnSource, searchPngOnScreen, searchPngStringOnScreen, imageOffSet 


arrowDetectSCR = cv2.imread("img/flecha.png")
def hayFlechaEnPantalla():
    global arrowDetectSCR
    ix,iy,ixx,iyy = 934,988,987,1052
    imageOffSet(0,0,1920,1080)
    imageScreen = imageFormatToCV2(printScreen(ix,iy,ixx,iyy)) # argumentos opcionales si es todo
    return findImgOnSource(arrowDetectSCR, imageScreen)

def main():
    print ("Cambia de ventana antes de 2s")
    time.sleep(2)
    # printTiming("total")
    ix,iy,ixx,iyy = 934,988,987,1052
    imageOffSet(0,0,1920,1080)
    imageScreen = imageFormatToCV2(printScreen(ix,iy,ixx,iyy)) # argumentos opcionales si es todo
    arrow = cv2.imread("img/flecha.png")
    #cv2.imwrite("dif/test2.png",imageScreen)
    return findImgOnSource(arrow, imageScreen)
    """ cv2.imshow("pic", imageScreen)
    cv2.waitKey(0) """

    """ img = cv2.imread('img/volverAJugar.png')
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
    # saveScreenShoot()
    pyautogui.moveTo(searchPngStringOnScreen('img/volverAJugar.png',332, 176, 571, 513))
    pyautogui.moveTo(searchPngOnScreen(cv2.imread('img/volverAJugar.png'),332, 176, 571, 513)) """

    

if __name__ == "__main__":
    main()