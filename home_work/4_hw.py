class Rectangle:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height

    def S(self):
        if self.width > 0 and self.height > 0:
            return self.width * self.height
        else:
            return "введите корректные значения"

    def P(self):
        if self.width > 0 and self.height > 0:
            return 2 * self.width + 2 * self.height
        else:
            return "введите корректные значения"


X1 = Rectangle(5, 5)
print("плащадь примоугольника1 - ", X1.S())
print("периметр примоугольника1 - ", X1.P())

X2 = Rectangle(0, -2)
print("плащадь примоугольника2 - ", X2.S())
print("периметр примоугольника2 - ", X2.P())

X3 = Rectangle(0, 2)
print("плащадь примоугольника3 - ", X3.S())
print("периметр примоугольника3 - ", X3.P())


# 2
class Math:
    def __init__(self, a: int, b: int):
        self.a = a
        self.b = b

    def addition(self):
        return self.a + self.b

    def multiplication(self):
        return self.a * self.b

    def division(self):
        if self.b != 0:
            return self.a / self.b

    def subtraction(self):
        return self.a - self.b


Y1 = Math(2, 0)
print(Y1.addition())
print(Y1.division())
print(Y1.multiplication())
print(Y1.subtraction())


#3