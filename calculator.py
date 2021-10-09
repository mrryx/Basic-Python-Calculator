#I spent wayyyy too long on this lol

calcType = input("Type \"a\" for addition, type \"s\" for subtraction, type \"m\" for multiplication, or type \"d\" for division: ")

#Addition
if calcType == "a":
    addNum1 = input("First number: ")
    addNum2 = input("Second number: ")
    sum = int(addNum1) + int(addNum2)
    print("The sum of number one and number two is " + str(sum) + ".")

#Subtraction
if calcType == "s":
    subNum1 = input("First number: ")
    subNum2 = input("Second number: ")
    difference = int(subNum1) - int(subNum2)
    print("The difference of number one and number two is " + str(difference) + ".")

#Multiplication
if calcType == "m":
    mulNum1 = input("First number: ")
    mulNum2 = input("Second number: ")
    product = int(mulNum1) * int(mulNum2)
    print("The product of number one and number two is " + str(product) + ".")

#Division
if calcType == "d":
    divNum1 = input("First number: ")
    divNum2 = input("Second number: ")
    quotient = int(divNum1) / int(divNum2)
    print("The quotient of number one and number two is " + str(quotient) + ".")

input()
