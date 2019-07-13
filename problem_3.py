def get_amount(string, phrase):

    # Input validation
    phrase_length = len(phrase)
    string_length = len(string)
    assert 1 < phrase_length < string_length

    array = []

    for i in range(len(string) - len(phrase) + 1):
        temp = string[i]
        for j in range(1, len(phrase)):
            temp += string[i + j]
        array.append(temp)
        array.append(temp[::-1])

    return array.count(phrase)


def main():
    string = input()
    phrase = input()
    print("Ditemukan {} kali".format(get_amount(string, phrase)))


if __name__ == "__main__":
    main()
