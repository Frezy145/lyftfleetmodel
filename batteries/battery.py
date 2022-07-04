# -*- coding : utf-8 -*-

from abc import ABC

# battery class

class Battery (ABC):
    
    def needs_service (self):
        return bool()
    
    