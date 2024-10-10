def replace_str (string,old_char,new_char):
    replace_char=string.replace(old_char,new_char)
    print(replace_char)

def main():
    string=input("Enter the string: ")
    old_char=input("Character to be replaced: ")
    new_char=input("Character to replace: ")
    replace_str(string,old_char,new_char)

if __name__=="__main__":
    main()




