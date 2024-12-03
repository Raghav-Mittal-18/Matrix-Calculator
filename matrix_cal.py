print("                                            ---># WELCOME TO MATRIXES CALCULATOR #")
print("You Can Perform Here Any Operation Between Two Matrixes")
row=int(input("enter the no. of rows in 1st matrix"))
col=int(input("enter the no. of columns in 1st matrix"))
row1=int(input("enter the no. of rows in 2nd matrix"))
col1=int(input("enter the no. of columns in 2nd matrix"))
oper=int(input("press 1 for multiplication \npress 2 subtraction \npress 3 addition ::"))

if col!=row1: #CHECKING WHETHER THE MATRIXES ARE ABLE OR NOT FOR OPERATIONS
    print("error, you cannot perform any calculation bet these matrixes")

elif col==row1: 
    mat=[]
    for i in range(row):
        mat.append([])
        # PROGRAM FOR TAKING ELEMENTS FROM USER 
        # FOR 1ST MATRIX
        
    for i in range(1,row+1):
        for a in range(1,col+1):
            n=int(input( f"enter the element 1st matrix of at position :{i}{a}: "))
            mat[i-1].insert(a-1,n)
    for i in mat:
        print(i)
    
    # For 2nd matrix
    
    mat1=[]
    for i in range(row1):
        mat1.append([])
    for i in range(1,row1+1):
        for a in range(1,col1+1):
            n=int(input( f"enter the element of 2nd matrix at position :{i}{a}: "))
            mat1[i-1].insert(a-1,n)
    for i in mat1:
        print(i)
    
    if oper==1:
        print(len(mat1))
        new=[]
        for i in range(len(mat)):
            new.append([])
        for i in range(len(mat)):
            for a in range(len(mat1[0])):
                sum=0
                for j in range(len(mat[0])):
                    sum+=(mat[i])[j]*(mat1[j])[a]
                new[i].insert(a,sum)
        print("The multiplication of these two Matrixes is::")
        for i in new:
            print(i)
    elif oper==2 and col==col1 and row==row1:
        subt=[]
        for i in range(row):
            subt.append([])
        if row==row1 and col==col1:
            for i in range(row):
                for a in range(col):
                    sub=(mat[i])[a]-(mat1[i])[a]
                    subt[i].insert(a,sub)
            print("The Subtraction of these two Matrixes is::")
            for i in subt:
                print(i)
    elif oper==3 and col==col1 and row==row1:
        add=[]
        for i in range(row):
            add.append([])
        if row==row1 and col==col1:
            for i in range(row):
                for a in range(col):
                    adds=(mat[i])[a]+(mat1[i])[a]
                    add[i].insert(a,adds)
            print("The Addition of these two Matrixes is::")
            for i in add:
                print(i)
    else:
        print("order is not same so addition and multiplication does not takes place")