import pickle

my_dict = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6, "G": 7, "H": 8, "I": 9, "J": 10, "K": 11, "L": 12, "M": 13, "N": 14, "O": 15, "P": 16, "Q": 17, "R": 18, "S": 19, "T": 20, "U": 21, "V": 22, "W": 23, "X": 24, "Y": 25, "Z": 26}

# Save the dictionary to a file
with open("my_dict.pickle", "wb") as f:
  pickle.dump(my_dict, f)

# Load the dictionary from the file
with open("my_dict.pickle", "rb") as f:
  my_dict_from_pickle = pickle.load(f)

# Print the dictionary
print(my_dict_from_pickle)
print(str(my_dict_from_pickle))



# Save the dictionary as txt file
with open("my_dict.txt", "w") as f:
  f.write(str(my_dict))

# Load the dictionary from the txt file
with open("my_dict.txt", "r") as f:
  my_dict_from_txt = eval(f.read())

print(my_dict_from_txt)
