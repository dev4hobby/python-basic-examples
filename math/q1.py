from math import tan, cos, sin
import matplotlib.pyplot as plt

a = 0.1
k = 0.5

x_pos = []
y_pos = []

def function_a(x, t):
  y = round(tan(x+a) * sin(x+k) - cos(x+k), 2)
  x_pos.append(x)
  y_pos.append(y)
  if y >= 400.00 and y <= 400.05:
    print(f"[cross] X: {x}, Y: {y}")

if __name__ == "__main__":
  limit = 1.4725
  pos = 1.4675
  t = 400.00
  while pos < limit:
    function_a(pos, t)      
    pos += 0.000001

  plt.plot(x_pos, y_pos, label="line 1")
  plt.plot(x_pos, [t]*len(y_pos), label="line 2")
  plt.legend()
  plt.show()