def rem_occ(L,element):
    elem=[x for x in L if x!=element]
    return elem


def main():
    L=[12,90,45,7,34,34,56,90,34]
    element=int(input("Enter the element you want to remove: "))
    print (rem_occ(L,element))

if __name__=="__main__":
    main()