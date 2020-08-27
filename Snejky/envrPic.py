from PIL import Image, ImageDraw
import math
img = Image.new("RGB", (400, 400), color=(255,255,255))
pixels = img.load()

#tap = Image.open("tapeta.png")
#rgbImg = tap.convert("RGB")

for x in range(0, 400):
    for y in range(0, 400):
        if (math.sqrt((x-200)*(x-200) + (y-150)*(y-150)) < 20):
            pixels[(x, y)] = (0,255,0)
            
        if (int(math.sqrt((x-200)*(x-200) + (y-250)*(y-250))) == 20):
            pixels[(x, y)] = (0,255,0)

        if (int(math.sqrt((x-150)*(x-150) + (y-200)*(y-200))) == 20):
            pixels[(x, y)] = (255,0,0)
            
        if (math.sqrt((x-250)*(x-250) + (y-200)*(y-200)) < 20):
            pixels[(x, y)] = (255,0,0)

"""for y in range(0, 400):
    pixels[(200, y)] = (0,255,0) #y
    pixels[(y, 200)] = (255,0,0) #x"""

img.save("envr.png")
print("hotovo")
