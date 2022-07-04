# -*-coding : utf-8 -*-

# StermanEngine

from .engine import Engine

class StermanEngine (Engine) :
    
    def __init__(self,warnigning_light_on=False):
        self._warning_light_on = warnigning_light_on
        
    def needs_service (self):
        if self._warning_light_on :
            return True
        else :
            return False 