import random

def insertion_sort(n):
    A=[]
    for i in range(n):
        A.append(random.randint(10, 50))
    print("The array with random numbers generated is:",A)
    l=len(A)
    print ("The unsorted array is:",A)
    for j in range(1,l):
        key=A[j]
        i=j-1
        while i>=0 and A[i]>key:
            A[i+1]=A[i]
            i=i-1
        A[i+1]=key
    print ("The sorted array is:",A)

def main():
    n=int(input("Enter the number of elements: "))
    insertion_sort(n)

if __name__=="__main__":
    main()



