class Transport:
    def __init__(self,brand,max_speed,kind=None):
        self.brand = brand
        self.max_speed = max_speed
        self.kind = kind

    def __str__(self):
        return f"Тип транспорта {self.kind} марки {self.brand} может развивать скорость {self.max_speed} км/ч"


class Car(Transport):
    def __init__(self,brand,max_speed,mileage,gasoline_residue):
        super().__init__(brand,max_speed,kind=Car)
        self.__gasoline_residue = gasoline_residue
        self.mileage = mileage

    @property
    def gasoline(self):
        return f"Осталось бензина на {self.__gasoline_residue} км"

    @gasoline.setter
    def gasoline(self,value):
        if type(value) == int:
            self.__gasoline_residue += value
            print(f"Объем топлива увеличен на {value} л и составляет {self.__gasoline_residue} л")
        else:
            print(f"Ошибка заправки автомобиля")
