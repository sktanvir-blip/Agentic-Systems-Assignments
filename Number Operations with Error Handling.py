try:
    num1=int(input())
    num2=int(input())
    print("sum is:-",num1+num2)

    if num2==0:
        print("Cannot Divide By Zero")
    else:
        print("Division Result:-",num1/num2)

except ValueError:
    print("Invalid Input")
    