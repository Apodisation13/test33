def minus(iter):
    result = iter[0]
    for i in range(1, len(iter)):
        result -= iter[i]
    return result


a = [10, 3]
c = [10, 3, 4, 6]
print(minus(a))
print(minus(c))
