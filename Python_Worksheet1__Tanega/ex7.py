def individual_num(num):
    for i in str (num): #extracting each number
        print(i, end=" ") #printing it in the same line

def main():
    num = int(input("Enter a number"))
    if (len(str(num))) > 1: #checking if it is a single digit or not
        individual_num(num) #calling the function
    else:
        print ("Invalid input: enter a number which has more than 1 digit")

if __name__=="__main__":
    main()