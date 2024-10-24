def dup_elem(L,k):
    dup=[]
    for element in L:
        count=L.count(element)
        if count>k:
            dup.append(element)
    print("The element(s) occuring more tham",k,"times:",set(dup))


def main():
    L=[12,34,32,87,12,45,12]
    k=int(input("Enter k value: "))
    dup_elem(L,k)

if __name__=="__main__":
    main()