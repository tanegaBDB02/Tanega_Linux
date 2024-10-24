import random

L=[]
n=int(input("Enter the number of elements you want: "))
for i in range (n):
    L.append(random.randint(10,50))
print ("The list with random numbers generated is",L)

def dup_elem():
    length=len(L)
    duplicates=set()
    for i in range(0,length):
        count=0
        for j in range(0,length):
            if L[i]==L[j]:
                count+=1
                if count>1:
                    duplicates.add(L[i])
    print ("The element(s) which have duplicates is/are:",set(L).intersection(duplicates))

def main():
    dup_elem()

if __name__=="__main__":
    main()
