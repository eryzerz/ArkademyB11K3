def get_series(operation, n, k):
    num = ""

    for i in range(1, n + 1):
        num += str(i)

    if operation.lower() == "sum":
        total = 0
        for i in k:
            total += int(num[i - 1])
        return total
    if operation.lower() == "mul":
        total = 1
        for i in k:
            total *= int(num[i - 1])
        return total
    if operation.lower() == "sub":
        total = 0
        for i in k:
            if i == k[0]:
                total += int(num[i - 1])
            else:
                total -= int(num[i - 1])
        return total
    if operation.lower() == "div":
        total = 0
        for i in k:
            if i == k[0]:
                total += int(num[i - 1])
            else:
                total //= int(num[i - 1])
        return total


def main():
    print(get_series("sum", 20, [11, 13, 15]))
    print(get_series("mul", 20, [12, 15, 17]))
    print(get_series("sub", 20, [2, 4, 8]))
    print(get_series("div", 20, [8, 19, 15]))


if __name__ == "__main__":
    main()
