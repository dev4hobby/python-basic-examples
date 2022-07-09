from playsound import playsound
from random import randint

if __name__ == "__main__":
  number = randint(1, 100)
  print(f"number is .. {number}")
  if number > 50:
    print("Play CantinaBand3.wav")
    playsound("./CantinaBand3.wav")
  else:
    print("Play StarWars3.wav")
    playsound("./StarWars3.wav")