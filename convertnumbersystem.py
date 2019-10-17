"""    """

print("-"*40,"\n" "1 - Integer To Binary, Octal, Hexadecimal","\n",
      "-"*40,"\n" "2 - Binary Arithmetic","\n",
      "-"*40,"\n" "3 - Octal Arithmetic","\n",
      "-"*40,"\n" "4 - Hexadecimal Arithmetic","\n",
      )

while True:
    giris = input("Make your choice. >   Press 'q' to exit")
    if giris == "q":
        break
    elif giris == "1":
        number1 = int(input("Enter the number to convert. >   "))
        print("-"*60,"\n" """[Integer: {:d}] - [Octal: {:o}] - [Hexadecimal: {:x}] - [Binary: {:b}]"""
              .format(number1, number1, number1, number1))
    elif giris == "2":
        try:
            number22 = input("Enter to binary number >   ")
            opert = input("Enter to operator (+,-,*,/) >   ")
            if opert not in "+-*/":
                print("Please enter to operators (+,-,*,/)")
            number33= input("Enter to binary number >   ")
            number2= int(number22, 2)
            number3= int(number33, 2)
            for op in opert:
                if op == "+":
                    print("{} {} {} = {:b}".format(number22,opert,number33,number2+number3))
                elif op == "-":
                    print("{} {} {} = {:b}".format(number22, opert, number33, number2 - number3))
                elif op == "*":
                    print("{} {} {} = {:b}".format(number22, opert, number33, number2 * number3))
                elif op == "/":
                    print("{} {} {} = {:b}".format(number22, opert, number33, number2 / number3))
                else:
                    pass
        except ValueError:
            print("Please enter to binary numbers and true operators.")
    elif giris == "3":
        try:
            number44 = input("Enter to octal number >   ")
            opert2 = input("Enter to operator (+,-,*,/) >   ")
            if opert2 not in "+-*/":
                print("Please enter to operators (+,-,*,/)")
            number55 = input("Enter to octal number >   ")
            number4 = int(number44, 8)
            number5 = int(number55, 8)
            for op in opert2:
                if op == "+":
                    print("{} {} {} = {:o}".format(number44, opert2, number55, number4 + number5))
                elif op == "-":
                    print("{} {} {} = {:o}".format(number44, opert2, number55, number4 - number5))
                elif op == "*":
                    print("{} {} {} = {:o}".format(number44, opert2, number55, number4 * number5))
                elif op == "/":
                    print("{} {} {} = {:o}".format(number44, opert2, number55, number4 / number5))
                else:
                    pass
        except ValueError:
            print("Please enter to octal numbers and true operators.")
    elif giris == "4":
        try:
            number66 = input("Enter to hexadecimal number >   ")
            opert3 = input("Enter to operator (+,-,*,/) >   ")
            if opert3 not in "+-*/":
                print("Please enter to operators (+,-,*,/)")
            number77 = input("Enter to hexadecimal number >   ")
            number6 = int(number66, 16)
            number7 = int(number77, 16)
            for op in opert3:
                if op == "+":
                    print("{} {} {} = {:x}".format(number66, opert3, number77, number6 + number7))
                elif op == "-":
                    print("{} {} {} = {:x}".format(number66, opert3, number77, number6 - number7))
                elif op == "*":
                    print("{} {} {} = {:x}".format(number66, opert3, number77, number6 * number7))
                elif op == "/":
                    print("{} {} {} = {:x}".format(number66, opert3, number77, number6 / number7))
                else:
                    pass
        except ValueError:
            print("Please enter to hexadecimal numbers and true operators.")