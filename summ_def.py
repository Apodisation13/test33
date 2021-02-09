def summ(*args):
    return sum(args)


if __name__ == "__main__":
    a = (1, 2, 7, 3)
    b = [1, 2, 3, 4, 5]
    print(summ(*a))
    print(summ(*b))
