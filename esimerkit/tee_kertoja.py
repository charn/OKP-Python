def tee_kertoja(n):
    return lambda x: x * n

f = tee_kertoja(5)
print(f(3)) # 15
print(f(5)) # 25
