# -*- coding : utf-8 -*-

# CarFactory class

from car import Car
from batteries.spindlerbattery import SpindlerBattery
from batteries.nubbinbattery import NubbinBattery
from engines.capuletengine import CapuletEngine
from engines.willoughbyengine import WilloughbyEngine
from engines.stermanengine import StermanEngine

# car factory class 
class CarFactory :
    
    # calliope method 
    def create_calliope (self, current_date, last_service_date, current_mileage, last_service_mileage):
        engine = CapuletEngine(last_service_mileage, current_mileage)
        battery = SpindlerBattery(current_date, last_service_date)
        return Car(engine,battery)
    
    # glissade method 
    def create_glissade(self, current_date, last_service_date, current_mileage, last_service_mileage):
        engine = WilloughbyEngine(last_service_mileage, current_mileage)
        battery = SpindlerBattery(current_date, last_service_date)
        return Car(engine, battery)
    
    # palindrome method
    def create_palindrome(self, current_date, last_service_date, warning_light_on):
        engine = StermanEngine(warning_light_on)
        battery = SpindlerBattery(current_date, last_service_date)
        return Car(engine, battery)
        
    # rorschach method 
    def create_rorschach(self, current_date, last_service_date, current_mileage, last_service_mileage):
        engine = WilloughbyEngine(last_service_mileage, current_mileage)
        battery = NubbinBattery(current_date, last_service_date)
        return Car(engine, battery)
    
    # thovex method   
    def create_thovex(self, current_date, last_service_date, current_mileage, last_service_mileage):
        engine = CapuletEngine(last_service_mileage, current_mileage)
        battery = NubbinBattery(current_date, last_service_date)
        return Car(engine, battery)