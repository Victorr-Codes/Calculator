try:
    while (1):
        print("\nWELCOME TO SHIVANG's CALCULATOR")
        print("ENTER YOUR FIRST NUMBER")
        var1 = int(input())
        print("WHAT DO YOU WANT TO DO")
        print("+" ,"-" ,"/" , "*")
        var3 = input()
        print("ENTER YOUR SECOND NUMBER")
        var2 = int(input())

        if var3=="+":
            print("Your ans is" , var1 + var2)

        elif var3=="-":
            print("Your ans is" , var1-var2)

        elif var3=="/":
            print("Your ans is" , var1 / var2)

        else:
            print("Your ans is" ,var1 * var2)

except Exception as e:
    print("Please write correctly")
