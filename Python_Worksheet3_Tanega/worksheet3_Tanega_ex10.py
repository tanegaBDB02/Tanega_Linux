def division(n1,n2):
    try:
        result=n1/n2
        print(result)

    except ZeroDivisionError:
        print ("Error:Number can't be divided by zero")
    except ValueError:
        print ("Error:Invalid argument input")
    except Exception as Error:
        print (Error)

    finally:
        print("Operation completed")

def main():
    division(5,25)
    division(2,0)
    division("l",5)

if __name__=="__main__":
    main()


