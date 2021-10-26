'''
example:
vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
class Ball:
    pass
'''

class Ball:
    def __init__(self, color):
        if not isinstance(color, str):
            raise TypeError(f"{color} - incorrect type for color")
        self.color = color

    def __repr__(self):
        return f"Object of claas Ball with attributs {self.__dict__}"

    def __str__(self):
        return f"{self.color} ball"

b1 = Ball("Red")
b2 = Ball("Blue")

b1
b2
print(b1)
print(b2)

