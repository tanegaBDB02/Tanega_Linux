def concat_str(s1,s2):
    concat=s1+s2
    print (concat)

def main():
    s1=input("Enter the string: ")
    s2=input("Enter another string: ")
    print ("The concatenated string is")
    concat_str(s1, s2)

if __name__=="__main__":
    main()
