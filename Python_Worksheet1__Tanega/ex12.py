def highest_frequency_character(S):
    S = S.lower()
    frequency = {}
    for char in S:
        if char.isalpha():
            if char in frequency:
                frequency[char] += 1
            else:
                frequency[char] = 1

    highest_char = None
    highest_count = 0

    for char, count in frequency.items():
        if count > highest_count:
            highest_count = count
            highest_char = char

    print("The character with the highest frequency is: ",highest_char)
    print("The frequency of the character is: ", highest_count)


def main():
    S=input("Enter the string: ")
    result = highest_frequency_character(S)
    print(result)


if __name__=="__main__":
    main()


