def max_min():
    marks_dict={"Physics":80,"Chemistry":78,"Biology":90,"History":88,"Geography":92}
    max=0
    for i in marks_dict.values():
        if i>max:
            max=i
    print("The maximum value of the dictionary is:",max)
    list_dict=list(marks_dict.values())
    min=list_dict[0]
    for i in marks_dict.values():
        if i<min:
            min=i
    print("The maximum value of the dictionary is:",min)

def main():
    max_min()

if __name__=="__main__":
    main()