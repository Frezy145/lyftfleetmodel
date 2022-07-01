# -*-coding : utf-8 -*-

# StermanEngine

from engine import Engine

class StermanEngine (Engine) :
    
    def __init__(self,warnigning_light_on=False):
        self.warning_light_on = bool()
        
    def needs_service ():
        if self.warning_light_on :
            return True
        else :
            return False 