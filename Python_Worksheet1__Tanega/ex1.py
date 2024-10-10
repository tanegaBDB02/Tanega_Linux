def sum_of_squares():
    sum = 0 #initializing it to zero
    n = int(input("Enter the range"))
    for i in range (0, n):
        square = n ** 2 #performing the square
        sum = sum+square
    return sum

def main():
    result = sum_of_squares() #calling the function
    print ("The sum of squares of the numbers is", result)

if __name__=="__main__":
    main()