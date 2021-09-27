num=input("Enter the first Num")
num1=input("Enter the Second Num")
num2=input("Enter the Third Num")
max= num if num>num1 and num>num2 else num1 if num1>num2 else num2
print(max)