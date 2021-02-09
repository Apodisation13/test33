def div(iter):
    result = iter[0]
    for i in range(1, len(iter)):
        result /= iter[i]
    return result


if __name__ == "__main__":
    a = [6, 3]
    b = (8, 2, 2)
    c = [30, 3, 5, 2, -1]
    for each in [a, b, c]:
        print(div(each))
