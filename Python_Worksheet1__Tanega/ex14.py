def whitespace (string):
    l=len(string)
    for i in range(0, l-1):
        if(string[i]==" "):
            trimmed_str=string.replace(" ","")
    print(trimmed_str)

def main():
    string=input("Enter the string: ")
    whitespace(string)

if __name__=="__main__":
    main()



