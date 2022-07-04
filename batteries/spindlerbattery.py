# -*-coding : utf-8 -*-

from .battery import Battery

# SpindlerBattery class

class SpindlerBattery (Battery) :
    
    def __init__(self, last_service_date, current_date):
        self._last_service_date = last_service_date
        self._current_date = current_date
        
    def needs_service(self) :
        # assume dates are in datetime.date type
        # duration will be timedelta type
        duration = self._current_date.today() - self._last_service_date
        if duration.days >= 2*365 : #assume 1 year = 365 days
            return True
        else :
            return False