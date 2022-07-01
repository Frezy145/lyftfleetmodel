# -*-coding : utf-8 -*-

# NubbinBattery class

from datetime import date

class NubbinBattery :
    
    def __init__(self, current_date, last_service_date):
        self._last_service_date = date(last_service_date)
        self._current_date = date(current_date)
        
    def needs_service() :
        duration = self._last_service_date - self._current_date.today()
        if duration.days >= 4*365 :
            return True
        else :
            return False