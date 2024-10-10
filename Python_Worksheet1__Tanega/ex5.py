def power(b,n):
    compute= b**n
    print ("The result of",b,"base to the power",n,"is",compute)

def main():
    b = int(input("Enter the base"))
    n = int(input("Enter the power"))
    power(b,n)

if __name__=="__main__":
    main()
