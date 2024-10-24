def print_items():
    random_dict={'run':'correr','eat':'comer','sleep':'dormir','write':'escribir','speak':'hablar'}
    print ("The keys and values of this dictionary is printed as follows:")
    for x,y in random_dict.items():
     print ("Key:",x,"-","Value:",y)

def main():
    print_items()

if __name__=="__main__":
    main()