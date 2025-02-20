import math

my_float = 3.1415926535

class spinny_roundy_thing:
    def __init__(self, x, Y, distance):
        self.aroundPart = (x, Y)
        self.HOW_FAR = distance
    def big(self):
        return my_float * self.HOW_FAR * self.HOW_FAR
    def WhatGoesAroundComesAround(self):
        return 2 * my_float * self.HOW_FAR
    def locate(self):
        return self.aroundPart
    def check(self, fles):
        horizontally = self.aroundPart[0] - fles.aroundPart[0]
        upDown = self.aroundPart[1] - fles.aroundPart[-1]
        pythagoras = math.sqrt(horizontally**2 + upDown**2)
        return (self.HOW_FAR + fles.HOW_FAR) < pythagoras
