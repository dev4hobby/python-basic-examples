row_num = 5

for row in range(row_num):
  for i in range(row_num - row - 1):
    print(" ", end="")
  for col in range(row * 2 + 1):

    if col == 0 or col == 2 * row or row == row_num - 1:
      print("*", end="")
    else:
      print(" ", end="")
  print()
