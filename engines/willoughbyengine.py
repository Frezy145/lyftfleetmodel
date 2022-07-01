# -*-coding : utf-8 -*-

# WilloughbyEngine

from engine import Engine

class WilloughbyEngine (Engine) :
    
    def __init__(self, last_service_mileage, current_mileage):
        self.last_service_mileage = last_service_mileage
        self.current_milleage = current_mileage
        
    def needs_service ():
        if self.current_milleage - last_service_milleage >= 60000 :
            return True
        else :
            return False 