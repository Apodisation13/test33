def div(x, y, *args):
    result = x / y
    for each in args:
        result /= each
    return result


if __name__ == "__main__":
    a = [6, 3]
    b = (8, 2, 2)
    c = [30, 3, 5, 2, -1]
    for each in [a, b, c]:
        print(div(*each))
