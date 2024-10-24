def matrix():
    mat1=[[20,45,1],[30,45,85],[10,25,19]]
    mat2=[[25,17,60],[37,28,42],[58,47,23]]
    diff_mat=[]
    for row1,row2 in zip(mat1,mat2):
        row_sum=[]
        for x,y in zip(row1,row2):
            row_sum.append(x-y)
        diff_mat.append(row_sum)
    print ("The sum of the matrices:",diff_mat)

def main():
    matrix()

if __name__=="__main__":
    main()
