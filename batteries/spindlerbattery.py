# -*-coding : utf-8 -*-

# SpindlerBattery class

from datetime import date

class SpindlerBattery :
    
    def __init__(self, current_date, last_service_date):
        self._last_service_date = date(last_service_date)
        self._current_date = date(current_date)
        
    def needs_service() :
        duration = self._last_service_date - self._current_date.today()
        if duration.days >= 2*365 :
            return True
        else :
            return False