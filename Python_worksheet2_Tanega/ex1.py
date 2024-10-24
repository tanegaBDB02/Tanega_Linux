def sum_avg(n):
    L=[]
    print ("Enter the elements:")
    for i in range (0,n):
        element=int(input())
        L.append(element)
    print ("The list with the entered elements is:", L)
    sum=0
    for count in L:
        sum=sum+count
    avg=sum/n
    print ("The sum of the elements is:",sum)
    print ("The average is:",avg)

def main():
    n = int(input("Enter the number of elements: "))
    sum_avg(n)

if __name__=="__main__":
    main()