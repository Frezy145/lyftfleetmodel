# -*-coding : utf-8 -*-

from .battery import Battery

# NubbinBattery class

class NubbinBattery(Battery) :
    
    def __init__(self, last_service_date, current_date):
        self._last_service_date = last_service_date
        self._current_date = current_date
        
    def needs_service(self) :
        # assume dates are in datetime.date type
        duration = self._current_date.today() - self._last_service_date
        if duration.days >= 4*365 :
            return True
        else :
            return False