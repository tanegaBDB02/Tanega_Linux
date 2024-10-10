def binary(num):
    bin=""
    while(num>=1):
        q=num//2
        r=num%2
        bin=bin+str(r)
        num=q
    print(int(bin[::-1]))


def main():
    num = int(input("Enter a number"))
    print ("The binary conversion of the number is")
    binary(num)


if __name__=="__main__":
    main()






