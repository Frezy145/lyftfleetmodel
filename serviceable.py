# -*-coding : utf-8 -*-

from abc import ABC

# Servicable class

class Serviceable (ABC) :
    
    def need_service(self):
        
        return True
    