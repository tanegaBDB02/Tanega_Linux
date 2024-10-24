def sum_values():
    marks_dict={"Physics":80,"Chemistry":78,"Biology":90,"History":88,"Geography":92}
    sum=0
    for x in marks_dict.values():
        sum=sum+x
    print ("The sum of the values of the dictionary is:",sum)

def main():
    sum_values()

if __name__=="__main__":
    main()
