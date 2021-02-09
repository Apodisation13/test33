def mul(iter):
    result = iter[0]
    for i in range(1, len(iter)):
        result *= iter[i]
    return result


if __name__ == "__main__":
    a = [10, 3]
    b = (2, 3, 2**2)
    c = [1, 2, 3, 4]
    print(mul(a))
    print(mul(b))
    print(mul(c))
    print(mul(a) - 1)
