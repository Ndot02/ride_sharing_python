from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __init__(self, driver_name, vehicle_type, rating):
        self.driver_name = driver_name
        self.vehicle_type = vehicle_type
        self.rating = rating

    @property
    def rating(self):
        return self.__rating

    @rating.setter
    def rating(self, value):
        if value < 1 or value > 5:
            raise ValueError("Rating must be between 1 and 5")

        self.__rating = value

    @abstractmethod
    def fare_calculation(self, distance):
        pass


class Bike(Vehicle):
    def fare_calculation(self, distance):
        return distance * 15


class Car(Vehicle):
    def fare_calculation(self, distance):
        return distance * 25