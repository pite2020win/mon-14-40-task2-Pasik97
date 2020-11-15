import random
from abc import ABC, abstractmethod

class Event(ABC):
  @abstractmethod
  def create_angle(self, newAngle):
    pass

class Turbulence(Event):
  def create_angle(self):
    return random.gauss(0, 2*random.randint(0, 10))

class Correction(Event):
  def create_angle(self, newAngle):
    return -newAngle

class Plane:
  def __init__(self):
    self.roll = 0
    self.correction = Correction()

  def detect_turbulence(self, new_angle):
    self.roll = new_angle
    print('Plane roll after turbulance: {}'.format(self.roll))
    self.apply_correction(new_angle)

  def apply_correction(self, angle):
    self.roll += self.correction.create_angle(angle)
    print('Plane roll after correction: {}'.format(self.roll))

class Environment:
  def __init__(self):
    self.turbulence = Turbulence()
    self.plane = Plane()

  def apply_turbulence(self):
    self.plane.detect_turbulence(self.turbulence.create_angle())

def run_program(environment):
  while True:
    environment.apply_turbulence()

if __name__ == '__main__':
  environment = Environment()
  next(run_program(environment))