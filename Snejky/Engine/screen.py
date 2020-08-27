import numpy as np
import math
import pygame
import time

class Screen:
    def __init__(self, width, height, color=(255,255,255)):
        self.width = width
        self.height = height
        self.color = color

        self.blankScreen = np.zeros((width, height, 3), dtype=np.uint8)
        
        self.blankScreen[0:width, 0:height] =  color

        self.objHeap = Heap()

    def createScreen(self, screen):
        screen.fill(self.color)
        while (self.objHeap.count > 0):
            obj = self.objHeap.removeMax()
            if (len(obj.points) >= 3):
                pygame.draw.polygon(screen, obj.color, obj.points, 0)
                #pygame.draw.polygon(screen, obj.color, obj.points, 1)
            else:
                pygame.draw.lines(screen, obj.color, False, obj.points, 1)

    #vykresli celou scenu
    def drawScreen(self):
        self.visibilityScreen = np.zeros((self.width, self.height, 1), dtype=np.uint8)
        self.newScreen = self.blankScreen.copy()
        
        while (self.objHeap.count > 0):
            obj = self.objHeap.removeMax()
            self.drawTriangle(obj)
        
        
        return self.newScreen

    def drawGreenScreen(self, greenScreen):
        newScreen = self.blankScreen.copy()
        for x in range(0, self.width):
            for y in range(0, self.height):
                if (x < 1000 and y < 750):
                    if (self.greenCondition(greenScreen[(x,y)])):
                        newScreen[x, y] = greenScreen[(x,y)]
                    else:
                        while (self.objHeap.hasNext()):
                            obj = self.objHeap.next()
                            if (obj.isInTriangle(x, y)):
                                newScreen[x, y] = obj.color
                                break
                        self.objHeap.resetIterator
        return newScreen


    def drawTriangle(self, obj):
        x1 = obj.minX[0]
        x2 = obj.midX[0]
        x3 = obj.maxX[0]

        if (x1 < 0): x1 = 0
        if (x1 >= self.width): x1 = self.width-1
        
        if (x2 < 0): x2 = 0
        if (x2 >= self.width): x2 = self.width-1
        
        if (x3 < 0): x3 = 0
        if (x3 >= self.width): x3 = self.width-1
        
        for x in range(x1, x2):
            y1 = int(obj.a1*x + obj.b1)
            y2 = int(obj.a3*x + obj.b3)

            if (y1 < 0): y1 = 0
            if (y1 >= self.height): y1 = self.height
            if (y2 < 0): y2 = 0
            if (y2 >= self.height): y2 = self.height
            
            if (y1 <= y2):
                self.newScreen[x, y1:y2] = obj.color
            else:
                self.newScreen[x, y2:y1] = obj.color

        for x in range(x2, x3):
            y1 = int(obj.a2*x + obj.b2)
            y2 = int(obj.a3*x + obj.b3)

            if (y1 < 0): y1 = 0
            if (y1 >= self.height): y1 = self.height
            if (y2 < 0): y2 = 0
            if (y2 >= self.height): y2 = self.height

            if (y1 <= y2):
                self.newScreen[x, y1:y2] = obj.color
            else:
                self.newScreen[x, y2:y1] = obj.color
                
    #verejna metoda, ktera prida trojuhelnik do primarni fronty(haldy)
    #points = []
    def draw(self, points, distance, color, fill):
        self.objHeap.add(DrawnObject(points, distance, color, fill))


    def greenCondition(self, color):
        r = color[0]
        g = color[1]
        b = color[2]

        sm = r+g+b
        if (g != 0):
            if (g/(sm/100) >= 75): return False
        return True
                
#vykreslovany objekt
class DrawnObject:
    def __init__(self, points, distance, color, fill):
        self.points = points
        self.distance = distance
        self.color = self.changeVisibility(color)
        self.fill = fill
        self.minMidMax()
        self.a1, self.b1 = self.function(self.minX, self.midX)
        self.a2, self.b2 = self.function(self.maxX, self.midX)
        self.a3, self.b3 = self.function(self.minX, self.maxX)

    def changeVisibility(self, color):
        if (len(color) == 4):
            A = color[3]/255
        else:
            A = 1
        R = int(color[0]*A)
        G = int(color[1]*A)
        B = int(color[2]*A)
        return (R,G,B)

    def isInTriangle(self, x, y):
        if (x >= self.minX[0] and x <= self.maxX[0]):
            if (x >= self.minX[0] and x <= self.midX[0]):
                y1 = self.a1*x + self.b1
                y2 = self.a3*x + self.b3

                if ((y >= y1 and y <= y2) or
                    (y <= y1 and y >= y2)):
                    return True
            elif (x >= self.midX[0] and x <= self.maxX[0]):
                y1 = a2*x + b2
                y2 = a3*x + b3

                if ((y >= y1 and y <= y2) or
                    (y <= y1 and y >= y2)):
                    return True
        return False

    def minMidMax(self):
        self.maxX = self.points[0]
        self.minX = self.points[0]

        for i in range(1, 3):
            if (self.maxX[0] < self.points[i][0]):
                self.maxX = self.points[i]
            if (self.minX[0] > self.points[i][0]):
                self.minX = self.points[i]
        self.midX = self.points[0]
        if (self.points[0] != self.maxX and self.points[0] != self.minX):
            self.midX = self.points[0]
        elif (self.points[1] != self.maxX and self.points[1] != self.minX):
            self.midX = self.points[1]
        elif (self.points[2] != self.maxX and self.points[2] != self.minX):
            self.midX = self.points[2]

    def function(self, point1, point2):
        if (point1[0] - point2[0] != 0):
            a = ((point1[1] - point2[1])/
                 (point1[0] - point2[0]))
        else:
            a = 1
            
        b = (point2[1] - a*point2[0])
        return a, b
        
        

#halda vykreslovanych objektu
class Heap:
    def __init__(self):
        self.count = 0
        self.iterator = 0
        self.objects = []
        self.objects.append(None)
    
    def add(self, obj):
        self.count += 1
        self.objects.append(obj)
        self.fixUp(self.count)      

    #vrati a odebere objekt s nejvetsim distance (1. prvek)
    def removeMax(self):
        first = self.objects[1]
        self.objects[1] = self.objects[self.count]
        self.objects.remove(self.objects[self.count])
        self.count -= 1
        self.fixDown(1)
        return first

    def hasNext(self):
        if (self.iterator+1 <= self.count):
            return True
        return False

    def next(self):
        if (self.hasNext):
            self.iterator += 1
            return self.objects[self.iterator]
        return None

    def resetIterator(self):
        self.iterator = 0

    def reset(self):
        self.count = 0
        self.objects = []
        self.objects.append(None)
        self.resetIterator()

    #opravi strom odshora
    def fixDown(self, index):
        if (2*index <= self.count):
            j = 2*index #index leveho potomka
            if ((j+1) <= self.count):
                if (self.objects[j+1].distance > self.objects[j].distance):
                    j += 1 #j je ted index nejvetsiho potomka
            if (self.objects[index].distance > self.objects[j].distance):
                return #vlastnost 2 je ok
            else:
                self.swap(j, index)
                self.fixDown(j)

    #opravi strom odzdola
    def fixUp(self, index):
        if (index == 1):
            return #je to koren
        j = int(index/2)
        if (self.objects[j].distance < self.objects[index].distance):
            self.swap(j, index)
            self.fixUp(j)
            
    #prohodi dva prvky
    def swap(self, p, n):
        tmp = self.objects[p]
        self.objects[p] = self.objects[n]
        self.objects[n] = tmp
        
#import random
#screen = Screen(500, 100, (255,0,0))
"""for i in range(0, 100):
    l = random.randrange(0, 9000)
    screen.drawObject([(1,1)], l, 4, 5)
    
for i in range(0, 100):
    print(screen.objHeap.removeMax().distance)"""
