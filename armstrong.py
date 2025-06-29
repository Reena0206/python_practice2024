#Check Number is Armstrong or not

num = int(input("Enter a Number to check Armstrong or not: "))

#Get the sum of all number with power of length
str_num = str(num)
sum_num = 0
for i in str_num:
    sum_num += int(i)**len(str_num)
    # print(int(i)**len(str_num))

if num==sum_num:
    print(f"{num} is an Armstrong Number")
else:
    print(f"{num} is not an Armstrong Number")