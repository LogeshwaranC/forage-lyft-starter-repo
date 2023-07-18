from datetime import date
import unittest


class OctoprimeTire:
    def __init__(self, tire_wear):
        self.tire_wear = tire_wear

    def needs_service(self):
        return sum(self.tire_wear) >= 3
    

class CarFactory:
    @staticmethod
    def create_carrigan_tire(tire_wear):
        return OctoprimeTire(tire_wear)
    

if __name__ == "__main__":
    unittest.main()