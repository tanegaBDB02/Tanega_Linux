def arrange():
    L=[2,-8,4,-2,3,-7,5,6,-9]
    L.sort(key=lambda x:x>=0)
    print(L)

def main():
    arrange()

if __name__=="__main__":
    main()