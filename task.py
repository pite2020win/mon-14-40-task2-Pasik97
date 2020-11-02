#
#Flight simulator. 
#Write a code in python that simulates the tilt correction of the plane (angle between plane wings and earth). 
#The program should print out current orientation, and applied tilt correction.
# (Tilt is "Roll" in this diagram https://www.novatel.com/assets/Web-Phase-2-2012/Solution-Pages/AttitudePlane.png)
#The program should run in infinite loop, until user breaks the loop. 
#Assume that plane orientation in every new simulation step is changing with random angle with gaussian distribution (the planes is experiencing "turbuence"). 
# Hint: "random.gauss(0, 2*rate_of_correction)"
#With every simulation step the orentation should be corrected, correction should be applied and printed out.
#Try to expand your implementation as best as you can. 
#Think of as many features as you can, and try implementing them.
#
#Try to expand your implementation as best as you can. 
#Think of as many features as you can, and try implementing them.
#Make intelligent use of pythons syntactic sugar (overloading, iterators, generators, etc)
#Most of all: CREATE GOOD, RELIABLE, READABLE CODE.
#The goal of this task is for you to SHOW YOUR BEST python programming skills.
#Impress everyone with your skills, show off with your code.
#
#Your program must be runnable with command "python task.py".
#Show some usecases of your library in the code (print some things)
#Delete these comments before commit!
#
#Good luck.

import random

class Plane:
  def __init__(self):
    self.roll = 0;
    self.correction = 0;

  def find_correction(self):
    randomCorrection = random.randint(0, 10)

    while self.roll - random.gauss(0, 2*randomCorrection) < 0.0001: 
      randomCorrection = random.randint(0, 10)

    self.correction = randomCorrection

  def roll_with_correction(self):
    return self.roll - random.gauss(0, 2*self.correction)


if __name__ == '__main__':
  start = 1;
  plane = Plane();
  while start:
    plane.roll += random.gauss(0, 2*random.randint(0, 10))
    print("Plane roll: {}".format(plane.roll))
    plane.find_correction()
    print(plane.roll_with_correction())