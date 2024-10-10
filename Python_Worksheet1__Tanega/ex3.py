def count_one(num):
    bin=""
    while(num>=1):
        q=num//2
        r=num%2
        bin=bin+str(r)
        num=q

    count=0
    for i in bin:
        if (int(i)==1):
            count = count +1

    print (count)

def main():
    num = int(input("Enter a number"))
    print ("The number of ones in the binary equivalent are")
    count_one(num)


if __name__=="__main__":
    main()




