def alt_str(string):
    l=len(string)
    alt=string[0:l:2]
    print (alt)

def main():
    string=input("Enter the string: ")
    print ("The alternate characters of the string is", alt_str(string))


if __name__=="__main__":
    main()


