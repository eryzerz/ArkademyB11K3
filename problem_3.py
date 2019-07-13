

def get_amount(string, phrase):
    array = []
    count = 0

    for i in range(len(string) - len(phrase) + 1):
        temp_1 = ""
        temp_2 = ""
        for j in range(1, len(phrase)):
            temp_1 += string[i + j]
        temp_2 = string[i] + temp_1
        array.append(temp_2)
        array.append(temp_2[::-1])

    return array.count(phrase)


def main():
    string = input()
    phrase = input()
    print("Ditemukan {} kali".format(get_amount(string, phrase)))


if __name__ == "__main__":
    main()
