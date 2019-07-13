def is_prime(num):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                return False
        return True
    else:
        return False


def buy_egg(date, money):
    assert 1 <= date <= 31
    price = 2000
    amount = money // price
    if date % 2 == 1:
        bonus = (amount // 20) * 3
        if is_prime(date):
            bonus += (amount // 12)
            if date % 5 == 0:
                if bonus % 2 == 0:
                    bonus *= 10
                else:
                    bonus *= 5
                amount += bonus
        else:
            if date % 5 == 0:
                if bonus % 2 == 0:
                    bonus *= 10
                else:
                    bonus *= 5
                amount += bonus
        return amount
    else:
        if is_prime(date):
            bonus += (amount // 12)
            amount += bonus
        return amount


def main():
    print(buy_egg(25, 50000))
    print(buy_egg(5, 100000))


if __name__ == "__main__":
    main()
