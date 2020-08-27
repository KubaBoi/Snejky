from PIL import Image, ImageDraw
import math

def isColor(isColor, color, delay):
    if (isColor[0] - delay <= color[0] <= isColor[0] + delay and
        isColor[1] - delay <= color[1] <= isColor[1] + delay and
        isColor[2] - delay <= color[2] <= isColor[2] + delay):
        return True
    return False

img = Image.open("envr.png")
rgbImg = img.convert("RGB")
pixels = rgbImg.load()

red = []

maxX = 0
minX = 400
maxY = 0
minY = 400

for x in range(0,400):
    for y in range(0, 400):
        if (isColor(pixels[x,y], (255,0,0), 2)):
            if (maxX < x): maxX = x
            if (minX > x): minX = x
            if (maxY < y): maxY = y
            if (minY > y): minY = y

print(maxX, minX, maxY, minY)


