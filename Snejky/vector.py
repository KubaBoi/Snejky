

class Vector:

    @staticmethod
    def add(vector1: tuple, vector2: tuple):
        v = []
        for v1, v2 in zip(vector1, vector2):
            v.append(v1 + v2)
        return tuple(v)

    @staticmethod
    def sub(vector1: tuple, vector2: tuple):
        v = []
        for v1, v2 in zip(vector1, vector2):
            v.append(v1 - v2)
        return tuple(v)

    @staticmethod
    def scale(vector: tuple, scalar: float):
        for i in vector:
            vector[i] *= scalar
        return vector

    @staticmethod
    def reverse(vector: tuple):
        return Vector.scale(vector, -1)

    @staticmethod
    def product(vector1: tuple, vector2: tuple):
        return (
            vector1[1] * vector2[2] - vector2[1] * vector1[2],
            vector1[2] * vector2[0] - vector2[2] * vector1[0],
            vector1[0] * vector2[1] - vector2[0] * vector1[1]
        )