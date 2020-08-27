import math
from Engine.vector import Vector

class Vertex:
    def __init__(self, x, y, z):
        self.Position = Vector(x, y, z)

    def drawVertex(self, camera):
        self.isInFront = self.isInFrontOfCamera(camera)
        x, y = self.findProjection(camera)
        return (x, y)

    #vypocita a vrati souradnice vykresleni na obrazovce
    def findProjection(self, camera):
        G = self.findG(camera)

        g = G.newVector(camera.S)
        if (g.length() != 0):
            #uhel mezi g a u (u S)
            alpha = g.angle(camera.u)

            #uhel mezi g a kolmici na u
            beta = math.pi - (math.pi/2 + alpha)

            x = abs(g.length() * math.sin(alpha))*1000
            y = abs(g.length() * math.sin(beta))*1000

            angle1 = g.angle(camera.u)
            angle2 = g.angle(camera.r)
            
            #self.isInFront = True
            if (0 <= angle1 <= math.pi/2 and 0 <= angle2 <= math.pi/2): #I. kvadrant
                x = camera.x + x
                y = camera.y - y
            elif (0 <= angle1 <= math.pi/2 and angle2 >= math.pi/2): #II. kvadrant
                x = camera.x - x
                y = camera.y - y      
            elif (angle1 >= math.pi/2 and angle2 >= math.pi/2): #III. kvadrant
                x = camera.x - x
                y = camera.y + y
            elif (angle1 >= math.pi/2 and 0 <= angle2 <= math.pi/2): #IV. kvadran               
                x = camera.x + x
                y = camera.y + y
                
        else:
            x = 0
            y = 0
            
        x = int(x)
        y = int(y)
        return (x, y)

    #vrati bod, ve kterem se protina primka pohledu s rovinou promitani
    def findG(self, camera):
        c1 = self.Position.x
        c2 = self.Position.y
        c3 = self.Position.z
        
        u1 = camera.u.x
        u2 = camera.u.y
        u3 = camera.u.z

        r1 = camera.r.x
        r2 = camera.r.y
        r3 = camera.r.z
        
        s1 = camera.S.x
        s2 = camera.S.y
        s3 = camera.S.z

        if (self.isInFront):
            g1 = camera.Position.x - c1
            g2 = camera.Position.y - c2
            g3 = camera.Position.z - c3
        else:
            g1 = c1
            g2 = 0
            g3 = c3

        #miluju matlab
        try:
            t = (-(c1*r2*u3 - c1*r3*u2 - c2*r1*u3 + c2*r3*u1 + c3*r1*u2 - c3*r2*u1
                   + r1*s2*u3 - r1*s3*u2 - r2*s1*u3 + r2*s3*u1 + r3*s1*u2 - r3*s2*u1)/
                 (g1*r2*u3 - g1*r3*u2 - g2*r1*u3 + g2*r3*u1 + g3*r1*u2 - g3*r2*u1))
        except:
            t = 0

        #speak
        #print((c1 + t*g1, c2 + t*g2, c3 + t*g3))

        return Vector(c1 + t*g1,
                      c2 + t*g2,
                      c3 + t*g3)

    def isInFrontOfCamera(self, camera):
        a = self.Position.pointLen(camera.S)
        ac = self.Position.pointLen(camera.Position)
        if (a <= ac): return True

        return False

    #metoda vraci upravene souradnice vertexu, ktery je za kamerou
    def fromBack(self, side, bigger, lower):
        bigger *= 50
        lower *= 50
        l = math.sqrt(bigger*bigger + lower*lower)
        if (l > side):
            return math.sqrt(l*l - side*side), side
        else:
            return 0, 0

    
