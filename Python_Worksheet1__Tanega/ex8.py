def half_str(string):
    l= len(string)
    half=int(float(l/2)) #integer value of decimal
    #half=int(l//2) (alternate way)
    print (string[0:half]) #printing the string till half of it

def main():
    string=input("Enter the string: ")
    print ("The first half of the string is")
    half_str(string)


if __name__=="__main__":
    main()