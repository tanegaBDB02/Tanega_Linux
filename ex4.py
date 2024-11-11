def list_squares():
    numbers=[1,2,3,4,5,6,7,8,9,10]
    squares={s:s**2 for s in numbers if s%2==0}

    print(squares)

def main():
    list_squares()

if __name__=="__main__":
    main()
