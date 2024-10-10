def prime():
    num = int(input("Enter a number"))
    if (num<2): #checking if it is a unique number or not
        return False
    for i in range (2, num): #iterating till that number to check if it is prime
        if (num % i == 0):
            return False

    return True

def main():
    if prime(): #checking if it is true
        print ("It is a prime number")
    else:
        print ("It is not a prime number")

if __name__=="__main__":
    main()



