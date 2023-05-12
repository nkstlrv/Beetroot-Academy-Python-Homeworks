class Fraction:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"{__class__.__name__}({self.x}, {self.y})"

    def __add__(self, other):
        if self.y == 0 or other.y == 0:
            raise ZeroDivisionError("Denominator can't be equal to zero")
        else:
            a = self.x * other.y + other.x * self.y
            b = self.y * other.y
            return Fraction(a, b)

    def __sub__(self, other):
        if self.y == 0 or other.y == 0:
            raise ZeroDivisionError("Denominator can't be equal to zero")
        else:
            a = self.x * other.y - other.x * self.y
            b = self.y * other.y
            return Fraction(a, b)

    def __mul__(self, other):
        if self.y == 0 or other.y == 0:
            raise ZeroDivisionError("Denominator can't be equal to zero")
        else:
            a = self.x * other.x
            b = self.y * other.y
            return Fraction(a, b)

    def __truediv__(self, other):
        if other.x == 0:
            a = self.x
            b = self.y
            return Fraction(a, b)
        elif self.y == 0 or other.y == 0:
            raise ZeroDivisionError("Denominator can't be equal to zero")
        else:
            a = self.x * other.y
            b = self.y * other.x
            return Fraction(a, b)


if __name__ == "__main__":

    x = Fraction(1, 3)
    y = Fraction(2, 5)

    print(x + y)
    print(x - y)
    print(x * y)
    print(x / y)

