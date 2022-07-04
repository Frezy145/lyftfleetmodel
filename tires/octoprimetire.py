# -*- coding : utf-8 -*-

from .tire import Tire

# Octoprime Tire class

class OctoprimeTire(Tire):
    
    def __init__(self, *array):
        self._array = array
        
    def needs_service(self):
        
        if sum(self._array) >= 3:
            return True
        
        return False