# -*- coding : utf-8 -*-

from unittest import TestCase, main
from datetime import date

from engines.capuletengine import CapuletEngine
from engines.willoughbyengine import WilloughbyEngine
from engines.stermanengine import StermanEngine

from batteries.spindlerbattery import SpindlerBattery
from batteries.nubbinbattery import NubbinBattery

# Capulet engine class test
class CapuletEngineTest(TestCase):
    
    def setUp(self):
        self.first_capulet = CapuletEngine(5000, 20000)
        self.second_capulet = CapuletEngine(3000, 34000)
    
    def test_needs_service (self):
        self.assertFalse(self.first_capulet.needs_service())
        self.assertTrue(self.second_capulet.needs_service())

class WilloughbyEngineTest(TestCase):
    
    def setUp(self):
        self.first_willoughby = WilloughbyEngine(5000, 45000)
        self.second_willoughby = WilloughbyEngine(5000, 66000)
        
    def test_needs_service(self):
        self.assertFalse(self.first_willoughby.needs_service())
        self.assertTrue(self.second_willoughby.needs_service())

class StermanEngineTest(TestCase):
    
    def setUp(self):
        self.first_sterman = StermanEngine()
        self.second_sterman = StermanEngine(True)
    
    def test_needs_service (self):
        self.assertFalse(self.first_sterman.needs_service())
        self.assertTrue(self.second_sterman.needs_service())

class SpindlerBatteryTest(TestCase):
    
    def setUp(self):
        self.first_spindler = SpindlerBattery(date(2020, 10, 4), date(2022, 7, 4))
        self.second_spindler = SpindlerBattery(date(2019, 7, 4), date(2022, 7, 4))
    
    def test_needs_service (self):
        self.assertFalse(self.first_spindler.needs_service())
        self.assertTrue(self.second_spindler.needs_service())
        

class NubbinBatteryTest(TestCase):
    
    def setUp(self):
        self.first_nubbin = SpindlerBattery(date(2021, 7, 4), date(2022, 7, 4))
        self.second_nubbin = SpindlerBattery(date(2017, 7, 4), date(2022, 7, 4))
        
    def test_needs_service (self):
        self.assertFalse(self.first_nubbin.needs_service())
        self.assertTrue(self.second_nubbin.needs_service())

if __name__ == '__main__':
    main()
