def remove_duplicates(str):
    words=str.split()
    dup={}
    result=[]
    for word in words:
        if word.lower() not in dup:
            result.append(word)
            dup[word.lower()] = True
    return ' '.join(result)


def main():
    str=input("Enter the sentence: ")
    print (remove_duplicates(str))

if __name__=="__main__":
    main()

