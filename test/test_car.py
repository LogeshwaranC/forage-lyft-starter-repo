import unittest
from datetime import datetime

from engine.model.calliope import Calliope
from engine.model.glissade import Glissade
from engine.model.palindrome import Palindrome
from engine.model.rorschach import Rorschach
from engine.model.thovex import Thovex


class CarTestCase(unittest.TestCase):
    def setUp(self):
        today = datetime.today().date()
        self.today = today
        self.one_year_ago = today.replace(year=today.year - 1)
        self.three_years_ago = today.replace(year=today.year - 3)
        self.five_years_ago = today.replace(year=today.year - 5)
        self.zero_mileage = 0
        self.mileage_30k = 30000
        self.mileage_60k = 60000

class TestCalliope(CarTestCase):
    def test_battery_should_be_serviced(self):
        car = Calliope(self.three_years_ago, self.zero_mileage, self.zero_mileage)
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        car = Calliope(self.one_year_ago, self.zero_mileage, self.zero_mileage)
        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        car = Calliope(self.today, 30001, self.zero_mileage)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        car = Calliope(self.today, 30000, self.zero_mileage)
        self.assertFalse(car.needs_service())

class TestGlissade(CarTestCase):
    def test_battery_should_be_serviced(self):
        car = Glissade(self.three_years_ago, self.zero_mileage, self.zero_mileage)
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        car = Glissade(self.one_year_ago, self.zero_mileage, self.zero_mileage)
        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        car = Glissade(self.today, 60001, self.zero_mileage)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        car = Glissade(self.today, 60000, self.zero_mileage)
        self.assertFalse(car.needs_service())

class TestPalindrome(CarTestCase):
    def test_battery_should_be_serviced(self):
        car = Palindrome(self.five_years_ago, False)
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        car = Palindrome(self.three_years_ago, False)
        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        car = Palindrome(self.today, True)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        car = Palindrome(self.today, False)
        self.assertFalse(car.needs_service())

class TestRorschach(CarTestCase):
    def test_battery_should_be_serviced(self):
        car = Rorschach(self.five_years_ago, self.zero_mileage, self.zero_mileage)
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        car = Rorschach(self.three_years_ago, self.zero_mileage, self.zero_mileage)
        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        car = Rorschach(self.today, 60001, self.zero_mileage)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        car = Rorschach(self.today, 60000, self.zero_mileage)
        self.assertFalse(car.needs_service())

class TestThovex(CarTestCase):
    def test_battery_should_be_serviced(self):
        car = Thovex(self.five_years_ago, self.zero_mileage, self.zero_mileage)
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        car = Thovex(self.three_years_ago, self.zero_mileage, self.zero_mileage)
        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        car = Thovex(self.today, 30001, self.zero_mileage)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        car = Thovex(self.today, 30000, self.zero_mileage)
        self.assertFalse(car.needs_service())

if __name__ == '__main__':
    unittest.main()