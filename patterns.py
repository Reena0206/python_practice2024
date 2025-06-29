row = 5

# 1.
#     *****
#     *****
#     *****
#     *****
#     *****
for i in range(row):
    for j in range(row):
        print("*",end="")
    print()
print('='*30)

# 2.
#    *****
#    *   *
#    *   *
#    *   *
#    *****
for i in range(row):
    for j in range(row):
        if i==0 or i==4 or j==0 or j==4:
            print("*",end="")
        else:
            print(" ",end="")
    print()
print('='*30)

# 3.
#   *
#   **
#   ***
#   ****
#   *****
for i in range(1,row+1):
    for j in range(1,i+1):
        print("*",end="")
    print()
print('='*30)

# 4.
#  *****
#  ****
#  ***
#  **
#  *
for i in range(row,0,-1):
    for j in range(i):
        print("*",end="")
    print()
print('='*30)    

# 5.
#  1
#  22
#  333
#  4444
#  55555
for i in range(1,row+1):
    for j in range(1,i+1):
        print(i,end="")
    print()
print('='*30)

# 6.
#  55555
#  4444
#  333
#  22
#  1
for i in range(row,0,-1):
    for j in range(i):
        print(i,end="")
    print()
print('='*30) 

# 7.
#  1
#  12
#  123
#  1234
#  12345
for i in range(1,row+1):
    for j in range(1,i+1):
        print(j,end="")
    print()
print('='*30)

# 8.
#  54321
#  4321
#  321
#  21
#  1
for i in range(row,0,-1):
    for j in range(i,0,-1):
        print(j,end="")
    print()
print('='*30) 

# 9.
#     *
#    ***
#   *****
#  *******
for i in range(1,row):
    for j in range(row-i):
        print(" ",end="")
    for j in range(1,2*i):
        print("*",end="")
    print()
print('='*30)

# 10.
#  *********
#   *******
#    *****
#     ***
#      *
for i in range(row,0,-1):
    for j in range(row-i):
        print(" ",end="")
    for j in range(1,2*i):
        print("*",end="")
    print()
print('='*30)

# 11.
#       *
#      ***
#     *****
#    *******
#   *********
#    *******
#     *****
#      ***
#       *
for i in range(1,row):
    for j in range(row-i):
        print(" ",end="")
    for j in range(1,2*i):
        print("*",end="")
    print()
for i in range(row,0,-1):
    for j in range(row-i):
        print(" ",end="")
    for j in range(1,2*i):
        print("*",end="")
    print()
print('='*30)

# 12.
#    *
#    **
#    * *
#    *  *
#    *****
for i in range(1,row+1):
    for j in range(1,i+1):
        if j==1 or i==row or i==j:
            print("*",end="")
        else:
            print(" ",end="")
    print()
print('='*30)

# 13.
#    *****
#    *  *
#    * *
#    **
#    *
for i in range(row,0,-1):
    for j in range(1,i+1):
        if j==1 or i==row or i==j:
            print("*",end="")
        else:
            print(" ",end="")
    print()
print('='*30)

# 14.
#        *
#       * *
#      *   *
#     *     *
#    *********
for i in range(1,row+1):
    for j in range(row-i):
        print(" ",end="")
    for k in range(1,2*i):
        if k==1 or k==(2*i)-1 or i==row:
            print("*",end="")
        else:
            print(" ",end="")
    print()
print('='*30)

# 15.
#    *********
#     *     *
#      *   *
#       * *
#        *
for i in range(row,0,-1):
    for j in range(row-i):
        print(" ",end="")
    for k in range(1,2*i):
        if k==1 or k==(2*i)-1 or i==row:
            print("*",end="")
        else:
            print(" ",end="")
    print()
print('='*30)

# 16.
#        *
#       * *
#      *   *
#     *     *
#    *       *
#     *     *
#      *   *
#       * *
#        *
for i in range(1,row):
    for j in range(row-i):
        print(" ",end=" ")
    for k in range(1,2*i):
        if k==1 or k==(2*i)-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
for i in range(row,0,-1):
    for j in range(row-i):
        print(" ",end=" ")
    for k in range(1,2*i):
        if k==1 or k==(2*i)-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
print('='*30)

# 17.
#           1
#         1 2 1
#       1 2 3 2 1
#     1 2 3 4 3 2 1
#   1 2 3 4 5 4 3 2 1
for i in range(1,row+1):
    for j in range(row-i):
        print(" ",end=" ")
    for k in range(1,i+1):
        print(k,end=" ")
    for l in range(i-1,0,-1):
        print(l,end=" ")
    print()

# 18.
#           A
#         A B A
#       A B C B A
#     A B C D C B A
#   A B C D E D C B A
for i in range(1,row+1):
    for j in range(row-i):
        print(" ",end=" ")
    for k in range(1,i+1):
        print(chr(64+k),end=" ")
    for l in range(i-1,0,-1):
        print(chr(64+l),end=" ")
    print()

# 19.
#    *                 *
#    * *             * *
#    * * *         * * *
#    * * * *     * * * *
#    * * * * * * * * * *
#    * * * * * * * * * *
#    * * * *     * * * *
#    * * *         * * *
#    * *             * *
#    *                 *
for i in range(1,row+1):
    for j in range(1,i+1):
        print("*",end=" ")
    for k in range(2*(row-i)):
        print(" ",end=" ")
    for j in range(1,i+1):
        print("*",end=" ")
    print()
for i in range(row,0,-1):
    for j in range(1,i+1):
        print("*",end=" ")
    for k in range(2*(row-i)):
        print(" ",end=" ")
    for j in range(1,i+1):
        print("*",end=" ")
    print()