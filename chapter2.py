def get_all():
    lis = []
    for i in range(1, 10):
        for j in range(1, i + 1):
            lis.append(str(i) + "*" + str(j) + "=" + str(i * j))
    return lis


def print_tab(lis, boo):
    cp_lis = lis[:]
    if boo:
        cp_lis.reverse()
        for i in range(1, 10):
            while i > 0:
                print("%s \t" % cp_lis.pop())
                i = i - 1
            print()
    else:
        for i in range(1, 10):
            while 10 - i > 0:
                print("%s \t" % cp_lis.pop())
                i = i + 1
            print()


def cube(x):
    return x * x * x


if __name__ == "__main__":
    lis = get_all()
    print_tab(lis, True)
    print("\n" * 2)
    print_tab(lis, False)
    # c = 2 + 3j
    # print(c)
    # print(list(map(cube, range(1, 11))))
    # a = range(1, 11)
    # print(list(k * 5 for k in a))
    # print([k * 5 for k in range(1, 11)])
