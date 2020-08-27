import math

class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def speak(self, st):
        print(st + str((self.x, self.y, self.z, self.length())))

    #vector - vrati velikost
    def length(self):
        return math.sqrt(self.x*self.x + self.y*self.y + self.z*self.z)

    #bod - pricte k bodu vektor 
    def addVector(self, vector):
        self.x += vector.x
        self.y += vector.y
        self.z += vector.z

    #posune bod a vrati novy bod
    def addVectorReturn(self, vector):
        return Vector(self.x + vector.x,
                      self.y + vector.y,
                      self.z + vector.z)

    #obrati vektor
    def reverseVector(self):
        return Vector(self.x * -1,
                      self.y * -1,
                      self.z * -1)

    #nastavi delku vektoru
    def setVectorLeng(self, m):
        norm = self.norm()
        return Vector(norm.x * m,
                      norm.y * m,
                      norm.z * m)
    #vynasobi vektor
    def multipleVector(self, m):
        return Vector(self.x * m,
                      self.y * m,
                      self.z * m)

    #bod - vrati vzdalenost k jinemu bodu
    def pointLen(self, point):
        return (math.sqrt((self.x - point.x)*(self.x - point.x) +
                          (self.y - point.y)*(self.y - point.y) +
                          (self.z - point.z)*(self.z - point.z)))
    
    #vector - vrati normalizovany vektor
    def norm(self):
        if (self.length() != 0):
            return Vector(self.x / self.length(),
                          self.y / self.length(),
                          self.z / self.length())
        else: return Vector(0, 0, 0)

    #bod - vytvori novy vektor k bodu
    def newVector(self, point):
        return Vector(self.x - point.x,
                      self.y - point.y,
                      self.z - point.z)

    #vektor - vrati uhel mezi vektory
    def angle(self, vector):
        if (self.length() * vector.length() == 0):
            return 0
        try:
            return (math.acos(self.scalar(vector) /
                          (self.length() * vector.length())))
        except: return 0

    #vektor - vrati skalarni soucin vektoru
    def scalar(self, vector):
        return (self.x * vector.x +
                self.y * vector.y +
                self.z * vector.z)

    #vektor - zjisti jestli jsou vektory rovnobezne(muzou byt i opacne)
    def parallelVector(self, vector):
        if (abs(self.norm().x) == abs(vector.norm().x) and
            abs(self.norm().y) == abs(vector.norm().y) and
            abs(self.norm().z) == abs(vector.norm().z)):
            return True
        return False
    
    #vrati stejny vektor, ale zkopirovany
    def copy(self):
        return Vector(self.x, self.y, self.z)

    #vrati true pokud jsou si vektory rovny
    def equals(self, vector):
        return (self.x == vector.x and
                self.y == vector.y and
                self.z == vector.z)

    #vrati true pokud vektory miri stejnym smerem
    def directionEquals(self, vector):
        a = self.norm()
        b = vector.norm()
        return a.equals(b)
