def anagram(s1,s2):
    l1=len(s1)
    l2=len(s2)
    s1 = s1.lower()
    s2 = s2.lower()
    sorted_str1=sorted(s1)
    sorted_str2=sorted(s2)

    if (l1!=l2):
        print("Enter strings that are equal in length")
    elif (sorted_str1==sorted_str2):
        print (s1,"and",s2,"are anagrams")
    else:
        print (s1,"and",s2,"are not anagrams")

def main():
    s1=input("Enter a string: ")
    s2=input("Enter another string: ")
    anagram(s1,s2)

if __name__=="__main__":
    main()

