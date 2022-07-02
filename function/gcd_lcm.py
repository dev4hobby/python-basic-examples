# 최대공약수
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


# 최소공배수
def lcm(a, b):
    return a * b // gcd(a, b)


func_list = [gcd, lcm]

print(func_list[0](72, 90))  # 최대공약수
print(func_list[1](8, 10))  # 최소공배수
