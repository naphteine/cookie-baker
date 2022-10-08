import pyautogui
import time
import random
import argparse
from os import listdir, remove, system
from os.path import isfile, join
from datetime import datetime

print('Press Ctrl-C to quit.')

parser = argparse.ArgumentParser("cookie-baker.py")

parser.add_argument('-x', '--posX', help="X position", type=int, default=0)
parser.add_argument('-y', '--posY', help="Y position", type=int, default=0)
parser.add_argument('-ww', '--width', help="Window width", type=int, default=1370)
parser.add_argument('-wh', '--height', help="Window height", type=int, default=768)
args = parser.parse_args()

windowX = args.posX
windowY = args.posY
windowW = args.width
windowH = args.height

luckyLocation = None
tryNo = 0
luckyPath = "lucky-cookies"
luckyFiles = [f for f in listdir(luckyPath) if isfile(join(luckyPath, f))]
print(luckyFiles)

today = datetime.now()
today = today.strftime("%Y-%m-%d_%H-%M-%S")
luckyFile = "lucky-shot-" + today + ".png"
print(luckyFile)

print(luckyFiles[4])
exiter = False

try:
    while True:
        # Display mouse location
        x, y = pyautogui.position()
        print("X: ", x, " Y: ", y)

        # Take screenshot
        try:
            print("Removing lucky shot")
            remove(luckyFile)
        except:
            print("Not found!")
            
        print("Taking luckyshot")
        screenShot = pyautogui.screenshot(luckyFile)

        # Search for all images
        print("Searching for golden.. Try: ", tryNo)
        for i in luckyFiles:
            luckyLocation = pyautogui.locateAll(join(luckyPath, i), screenShot, region=(windowX, windowY, windowW, windowH), grayscale=True, confidence=.8)

            for pos in luckyLocation:
                luckyX, luckyY = pyautogui.center(pos)
                print("FOUND\tClicking @ ", luckyX, luckyY)
                pyautogui.click(luckyX, luckyY)
                exiter = True

            if exiter is True:
                exiter = False
                luckyLocation = None
                break
            
        tryNo += 1
except KeyboardInterrupt:
    print('\nCookie Baker is done with cookies.')
