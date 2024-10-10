def occur(string,char):
    string=string.lower()
    char=char.lower()
    index = string.find(char)
    if index != -1:
        print(index)
    else:
        print(f"'{char}' is not found in the string.")
    return "done"


def main():
    string=input("Enter the string: ")
    char = input("Enter the character you want to find the first occurence of")
    print(occur(string,char))


if __name__=="__main__":
    main()

