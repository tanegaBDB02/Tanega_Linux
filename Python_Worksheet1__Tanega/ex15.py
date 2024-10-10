def replace_word (string,old_word,new_word):
    new_sentence=string.replace(old_word,new_word)
    print(new_sentence)

def main():
    string=input("Enter the sentence: ")
    old_word=input("Word to be replaced: ")
    new_word=input("Word to replace: ")
    replace_word(string,old_word,new_word)

if __name__=="__main__":
    main()
