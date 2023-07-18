from battery.battery import Battery
from datetime import datetime
today = datetime.today().date()


class SpindlerBattery(Battery):
    def __init__(self, current_date, last_service_date):
        self.current_date = current_date
        self.last_service_date = last_service_date

    def needs_service(self):
        date_which_battery_should_be_serviced_by = today.replace(year=today.year)(self.last_service_date, 3)
        if date_which_battery_should_be_serviced_by < self.current_date:
            return True
        else:
            return False