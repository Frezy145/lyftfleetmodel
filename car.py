# -*-coding : utf-8 -*-

# Car class

from serviceable import Serviceable

class Car (Serviceable) :
    
    def __init_ (self, engine, battery):
        self._engine = engine
        self._battery = battery
        
    def needs_service():
        self._engine.needs_service()
        self._battery.needs_service()