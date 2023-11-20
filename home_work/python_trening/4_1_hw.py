from home_work.check import Checks


class Car(Checks):
    def __init__(self, color: str = "green", type: str = "BMW", year: int = 1900):
        super().__init__()
        self.color = color
        self.type = type
        self.year = year

    def run(self):
        super().check_text("Автомобиль заведен")
        return "Автомобиль заведен"

    def stop(self):
        super().check_text("Автомобиль заглушен")
        return "Автомобиль заглушен"

    def years(self, year: int):
        self.year = year
        super().check_text(f'год автомобиля = {self.year} ')
        print("год автомобиля = ", self.year)

    def types(self, type: str):
        self.type = type
        super().check_text(f'тип автомобиля = {self.type} ')
        print("тип автомобиля = ", self.type)

    def colors(self, color: str):
        self.color = color
        super().check_text(f'цвет автомобиля = {self.color} ')
        print("цвет автомобиля = ", self.color)


auto = Car()
print(auto.run())
print(auto.stop())
print(auto.years(1968))
print(auto.types("Volvo"))
print(auto.colors("black"))
