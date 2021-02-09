def mul(iter):
    result = iter[0]
    for i in range(1, len(iter)):
        result *= iter[i]
    return result


a = [10, 3]
b = (10, 3, 3)
c = [1, 2, 3, 4]
print(mul(a))
print(mul(b))
print(mul(c))
print(mul(a) - 1)
