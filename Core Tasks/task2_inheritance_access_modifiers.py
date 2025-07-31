class Vehicle:
    def __init__(self, brand, model):
        self._brand = brand
        self.__model = model

    def show_details(self):
        return f"Brand: {self._brand}, Model: {self.__model}"

class Car(Vehicle):
    def __init__(self, brand, model, fuel_type):
        super().__init__(brand, model)
        self.fuel_type = fuel_type

    def show_car_details(self):
        return f"{self._brand} runs on {self.fuel_type}"

car1 = Car("Toyota", "Innova", "Diesel")
print(car1.show_car_details())