import random

L=[]
n=int(input("Enter the number of elements you want: "))
for i in range (n):
    L.append(random.randint(10,50))
print ("The list with random numbers generated is",L)

def even_odd_num():
    length=len(L)
    even = [L[i] for i in range(length) if L[i]%2==0]
    print ("The even numbers in this list is:",even)
    odd = [L[i] for i in range(length) if L[i]%2!=0]
    print("The odd numbers in this list is:", odd)

def main():
    even_odd_num()

if __name__=="__main__":
    main()

