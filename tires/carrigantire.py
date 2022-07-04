# -*- coding : utf-8 -*-

from .tire import Tire

# Carrigan tire class

class CarriganTire(Tire):
    
    def __init__(self, *array):
        self._array = array
        
    def needs_service(self):
        
        for elt in self._array:
            if elt >= 0.9 :
                return True
                
        return False