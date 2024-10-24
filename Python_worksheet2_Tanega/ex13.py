def unique_value():
    test_dict = {"Gfg": [5,7,7,7,7], "is": [6,7,7,7], "Best": [9,9,6,5,5]}
    unique=0
    max_keys=""
    for key,value in test_dict.items():
        count=len(set(value))
        if count>unique:
            unique=count
            max_keys=key
    print("Key which has the maximum values:",max_keys)

def main():
    unique_value()

if __name__=="__main__":
    main()

