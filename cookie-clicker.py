import random
import pyautogui
import time
import argparse

parser = argparse.ArgumentParser("cookie-clicker.py")
parser.add_argument('-c', '--count', help="How many clicking?", type=int, default=100)
args = parser.parse_args()

runCount = args.count
randomRun = random.randint(runCount - 25, runCount + 25)

# Normal
normalLocation = pyautogui.locateOnScreen("normal-cookie.png", grayscale=True, confidence=0.5)
normalX, normalY = pyautogui.center(normalLocation)
clickX = random.randint(normalX - 6, normalX + 6)
clickY = random.randint(normalY - 6, normalY + 6)
clickTime = round(random.uniform(0.005, 0.009), 6)

for i in range(randomRun):
    clickTime = round(random.uniform(0.004, 0.005), 6)
    pyautogui.click(clickX, clickY)
    print(i, "/", randomRun, " | Clicked: ", clickX, " x ", clickY, " -- ", clickTime)

    if random.randint(1, 100) > 90:
        clickX = random.randint(normalX - 6, normalX + 6)
        clickY = random.randint(normalY - 6, normalY + 6)
        time.sleep(round(random.uniform(0.004, 0.005), 6))
