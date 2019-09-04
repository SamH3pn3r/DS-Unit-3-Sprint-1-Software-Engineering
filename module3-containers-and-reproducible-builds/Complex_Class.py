"""
    A Class to help with complex numbers!
"""

class Complex:
    def __init__(self, realpart, imagpart): 
        self.r = realpart
        self.i = imagpart

    def add(self, real, imag):
        real = self.r + realpart
        imag = self.i + imagpart
        print(str(real) + " + " + str(imag) + "i")

    def mult(self, real, imag):
        real = self.r * real
        imag = self.i * imag
        print(str(real) + " + " + str(imag) + "i")

    def subtract(self, real, imag):
        real = self.r - real
        imag = self.i - imag
        print(str(real) + " + " + str(imag) + "i")

    def divide(self, real, imag):
        real = self.r / real
        imag = self.i / imag
        print(str(real) + " + " + str(imag) + "i")

# Testing
x = Complex(3.0, -4.5)
x.add(2, 3)
x.mult(1, -3)
x.divide(13, 45)
x.subtract(22, 34)
