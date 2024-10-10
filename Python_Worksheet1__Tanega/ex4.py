def decimal(num):
    b=num[::-1]
    deci=0
    for i in range(0,len(b)):
        n=int(b[i])*(2**i)
        deci=deci+n
    return deci


def main():
    num = str(input("Enter a number: "))
    if num.isdigit():
        print (decimal(num))


if __name__=="__main__":
    main()



