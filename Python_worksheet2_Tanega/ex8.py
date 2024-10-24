def extract_chr(k):
    L=["Apple","Banana","Orange","Kiwi","Watermelon","Apricot"]
    occur = lambda x: x[0].upper()==k.upper()
    occur_list= list(filter(occur,L))

    if occur_list==[]:
        print ("No word starts with",k)
    else:
        print ("The words which has",k,"as the first character are:",occur_list)

def main():
    k=input("Enter the letter you want to check: ")
    extract_chr(k)

if __name__=="__main__":
    main()
