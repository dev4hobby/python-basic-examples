import math
from math import pow, ceil
from matplotlib import pyplot as plt

GRAVITY = 9.81
INTERVAL = 0.001

def time_array(start, end, step):
  times = []
  while start < end:
    times.append(start)
    start += step
  return times

def draw_parabola(x_velocity, y_velocity):
  fly_time = 2 * y_velocity / GRAVITY
  fly_distance = x_velocity * fly_time
  intervals = time_array(0, fly_time, INTERVAL)
  x = []
  y = []

  for t in intervals:
    x.append(x_velocity * t)
    y.append(y_velocity * t - 0.5 * GRAVITY * t * t)
  
  plt.xlabel(f"x vector velocity is {x_velocity} m/s")
  plt.ylabel(f"y vector velocity is {y_velocity} m/s")
  plt.title(f"Fly time is {math.ceil(fly_time)} 's. Distance is {math.ceil(fly_distance)}")
  plt.plot(x, y)
  plt.show()

if __name__=="__main__":
  try:
    x_velocity = float(input("Enter x velocity: "))
    y_velocity = float(input("Enter y velocity: "))
    draw_parabola(x_velocity, y_velocity)
  except ValueError:
    print("Invalid input.")