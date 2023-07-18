from datetime import date
import unittest

class CarriganTire:
    def __init__(self, tire_wear):
        self.tire_wear = tire_wear

    def needs_service(self):
        return any(wear >= 0.9 for wear in self.tire_wear)
    
class CarFactory:
    @staticmethod
    def create_carrigan_tire(tire_wear):
        return CarriganTire(tire_wear)
    
if __name__ == "__main__":
    unittest.main()