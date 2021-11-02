print('Calculator is starting... ')
print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")



while True:
    choice = input("Enter choice(1/2/3/4): ")

    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        sum = float(num1) + float(num2)
        sub = float(num1) - float(num2)
        mul = float(num1) * float(num2)
        div = float(num1) / float(num2) 


        if choice == '1':
            print('Add:',sum)
        elif choice == '2':
            print('Subtract:',sub)

        elif choice == '3':
            print('Multiply:',mul )

        elif choice == '4':
            print('Divide:',div)
        
        nxt = input("Let's do next calculation? (yes/no): ")
        if nxt == "no":
          break
    
    else:
        print("Invalid Input")
