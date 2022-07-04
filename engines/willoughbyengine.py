# -*-coding : utf-8 -*-

# WilloughbyEngine

from .engine import Engine

class WilloughbyEngine (Engine) :
    
    def __init__(self, last_service_mileage, current_mileage):
        self.last_service_mileage = last_service_mileage
        self.current_milleage = current_mileage
        
    def needs_service (self):
        if self.current_milleage - self.last_service_mileage >= 60000 :
            return True
        else :
            return False 