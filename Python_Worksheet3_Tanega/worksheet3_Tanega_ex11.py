class FormulaError(Exception):
    pass

def calculator(str):
    split_formula=str.split()
    try:
        if len(split_formula)!=3:
            raise FormulaError("Formula must consist 3 elements")

        n1=float(split_formula[0])
        op=split_formula[1]
        n2=float(split_formula[2])

        if op not in ["+","-"]:
            raise FormulaError("Operator should be at least +/-")

        if op=="+":
            print(n1+n2)
        elif op=="-":
            print(n1-n2)

    except FormulaError as err:
            print(err)
    except ValueError:
        print ("Enter valid integers")


def main():
    while True:
        str=input("Enter a formula (e.g. 1 + 2), which are separated by whitespaces or enter quit to exit: ")
        if str.lower()=="quit":
            break
        calculator(str)

if __name__=="__main__":
    main()









