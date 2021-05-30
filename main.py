import pyautogui  # pip install pyautogui
from PIL import Image, ImageGrab  # pip install pillow
# from numpy import asarray
import time


def hit(key):
    pyautogui.keyDown(key)
    return


def isCollide(data):
    # the rectangle for cactus
    for x in range(515, 516):
        for y in range(227, 248):
            if data[x, y] < 100:
                hit("up")
                return
 # Rectangle for small catus
    for x in range(511, 512):
        for y in range(249, 256):
            if data[x, y] < 100:
                hit("up")
                return

#the rectangle for birds
    for x in range(517, 519):
        for y in range(188, 225):
            if data[x, y] < 100:
                hit("down")
                return
    return


if __name__ == "__main__":
    print("Hey.. Dino game about to start in 3 seconds")
    time.sleep(2)
    # hit('up')


    while True:
        image = ImageGrab.grab().convert('L')
        data = image.load()
        isCollide(data)

        # print(asarray(image))


'''
        # Draw the rectangle for cactus
        for x in range(515, 516):
            for y in range(227, 248):
                data[x, y] = 0

         #Rectangle for small catus
        for x in range(511, 512):
            for y in range(249, 256):
                data[x, y] = 200

        #Draw the rectangle for birds
        for x in range(517, 519):
            for y in range(188, 225):
                data[x, y] = 171

        image.show()
        break
'''