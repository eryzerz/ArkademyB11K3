def is_prime(num):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                return False
        return True
    else:
        return False


def display_triangle(num):

    # Input Validation
    base_or_height = num
    assert 0 < base_or_height < 10

    ctr = 2
    for i in range(num + 1):
        for j in range(i):
            while is_prime(ctr) == False:
                ctr += 1
            print(ctr, end=" ")
            ctr += 1
        print()


def main():
    level = int(input())
    display_triangle(level)


if __name__ == "__main__":
    main()
