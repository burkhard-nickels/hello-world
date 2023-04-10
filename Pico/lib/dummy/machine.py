
from enum import Enum

# Pin = Enum('Pin', ['ON', 'OFF'])

def reset():
    print("Dummy machine Reset")

def soft_reset():
    print("Dummy machine Soft Reset")

def idle():
    print("Dummy machine Idle")

class ADC():

    def __init__(self,pin):
      self.pin = pin

    def read_u16(self):
        return 27.6432

class Pin():
    IN = 0
    OUT = 1

    def __init__(self,pin,enum):
      self.source = pin
      self.enum = enum

    def on(self):
        print("Dummy LED on!")

    def off(self):
        print("Dummy LED off!")

    def value(self):
        return 1

