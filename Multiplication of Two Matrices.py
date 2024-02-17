rows_of_a = int(input("Enter number of rows of a: "))
columns_of_a = int(input("Enter number of columns of a: "))
rows_of_b = int(input("Enter number of rows of b: "))
columns_of_b = int(input("Enter number of columns of b: "))
A = []
R = []
B = []
# [s, r, k, c,] = [0,0,0,0]

if columns_of_a == rows_of_b:
    for i in range(rows_of_a):
        R = []
        for j in range(columns_of_a):
            n = int(input("Enter elements of matrix a: "))
            R.append(n)
        A.append(R)
        
    for i in range(rows_of_b):
        R = []
        for j in range(columns_of_b):
            n = int(input("Enter elements of matrix b: "))
            R.append(n) 
        B.append(R)   
            
D = [[0]*len(B[0]) for _ in range(len(A))]

if columns_of_a == rows_of_b:
    for r in range(rows_of_a):    
        for c in range(rows_of_b ):
            s = 0
            for k in range(columns_of_a):
                x = A[r][k] * B[k][c]
                s = s + x
                D[r][c] = s
        #     c = c + 1 
        # c = 0
        # s = 0
        # r = r + 1
    print(f"{A} * {B} = {D}")   
else:
    print("Number of column of 'a'should be equal to number of rows of 'b' ")