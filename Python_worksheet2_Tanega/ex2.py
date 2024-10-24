
n=int(input("Enter the number of elements you want: "))
L=[]
print ("Enter the elements:")
for i in range (0,n):
    element=int(input())
    L.append(element)
print ("The list with the entered elements is:", L)


def max_elem():
    max=L[0]
    for i in range(n):
        if L[i]>max:
            max = L[i]
    print ("The maximum element of the list is:",max)


def min_elem():
    min=L[0]
    for i in range(n):
        if L[i] < min:
            min=L[i]
    print("The minimum element of the list is:", min)


def main():
    max_elem()
    min_elem()

if __name__=="__main__":
    main()






