from datetime import date
import unittest
from servicing_criteria.carrigan_tires import CarriganTire
from servicing_criteria.octoprime_tires import OctoprimeTire


class CarFactory:
    @staticmethod
    def create_carrigan_tire(tire_wear):
        return CarriganTire(tire_wear)

    @staticmethod
    def create_octoprime_tire(tire_wear):
        return OctoprimeTire(tire_wear)

