# -*-coding : utf-8 -*-

from abc import ABC

# engines

class Engine (ABC) :
    
    def needs_service(self) :
        
        return bool()