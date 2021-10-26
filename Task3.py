'''
example:
vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv

class Fraction:
    pass

if __name__ == "__main__":
    x = Fraction(1, 2)
    y = Fraction(1, 4)
    x + y == Fraction(3, 4)

'''

class Fraction:
    def __init__(self, x, y):
        if not isinstance(x, (int, float)) or not isinstance(x, (int, float)):
            raise TypeError("Значення недопустимого типу")
        if y == 0:
            raise ZeroDivisionError
        self.x = x
        self.y = y

    def __add__(self, other):
        return (Fraction(self.x * other.y + self.y * other.x, self.y * other.y))

    def __sub__(self, other):
        return (Fraction(self.x * other.y - self.y * other.x, self.y * other.y))

    def __mul__(self, other):
        return (Fraction(self.x * other.x, self.y * other.y))

    def __truediv__(self, other):
        if other.x == 0:
            raise ZeroDivisionError
        return (Fraction(self.x * other.y, self.y * other.x))

    def __str__(self):
        return f"{self.x}/{self.y}"

    def __eq__(self, other):
        return self.x/self.y == other.x/other.y
#        return self.x == other.x and self.y == other.y


x = Fraction(3, 0)
y = Fraction(1, 4)
print(f"{x} + {y} = {x + y}")
print(f"{x} - {y} = {x - y}")
print(f"{x} / {y} = {x / y}")
print(f"{x} * {y} = {x * y}")
print(x + y == Fraction(5, 8))

