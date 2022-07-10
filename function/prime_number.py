def is_prime_number(number):
  if number < 2:
    return False
  for i in range(2, number):
    if number % i == 0:
      return False
  return True

def prime_number_from(start, end):
  prime_number_list = []
  for i in range(start, end+1):
    if is_prime_number(i):
      prime_number_list.append(i)
  return prime_number_list


if __name__ == "__main__":
  number = int(input("수를 입력하세요 >> "))
  if is_prime_number(number):
    print(f"{number}는 소수입니다.")
  else:
    print(f"{number}는 소수가 아닙니다.")
  
  number =int(input("0부터 어디까지 소수를 찾으시겠습니까? >> "))
  prime_number_list = prime_number_from(0, number)
  print(prime_number_list)
