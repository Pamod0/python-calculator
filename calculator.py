import math

# functions for basic arithmetic operations


def add(a, b):
    return a+b


def subtract(a, b):
    return a-b


def multiply(a, b):
    return a*b


def divide(a, b):
    #  handles exceptions using a try-except block
    try:
        return a/b
    except Exception as e:
        print(e)


def power(a, b):
    return a**b


def remainder(a, b):
    return a % b


def square_root(a):
    return math.sqrt(a)

# functions for trignometric operations


def sine(a):
    answer = math.sin(math.radians(a))
    # round answer to two decimal places due to long answers
    return round(answer, 2)


def cosine(a):
    answer = math.cos(math.radians(a))
    return round(answer, 2)


def tangent(a):
    answer = math.tan(math.radians(a))
    return round(answer, 2)


# list for store calculator history
calc_history = []
# this string holds current calculation data
last_calculation = ""

# function for print calculator history


def history():
    if calc_history == []:
        print("No past calculations to show")
    else:
        for i in calc_history:
            print(i)


# function for take valid user input


def get_operand(text):
    while True:
        try:
            num = float(input(text))
            break
        except:
            print("Not a valid number, please enter again")
            continue
    return num

# main functionality of the calcultor


def calculator():
    # store basic calculator functions in a dictionary
    calc_functions = {
        '+': add,
        '-': subtract,
        '*': multiply,
        '/': divide,
        '^': power,
        '%': remainder,
        '$': square_root,
    }
    # store trignometric functions in a dictionary
    calc_functions_trignometric = {
        'sin': sine,
        'cos': cosine,
        'tan': tangent
    }

    while True:
        print("Select operation.")
        print("1.Add      : + ")
        print("2.Subtract : - ")
        print("3.Multiply : * ")
        print("4.Divide   : / ")
        print("5.Power    : ^ ")
        print("6.Remainder: % ")
        print("7.Square Root: $ ")
        print("8.Sine: sin ")
        print("9.Cosine: cos ")
        print("10.Tangent: tan ")
        print("11.Calculation History")

        operation = input("Operation: ")
        # check whether user entered operator is valid and
        # call get_operand() function to collect user input
        if operation in calc_functions:
            operand1 = get_operand("Enter first number: ")
            operand2 = get_operand("Enter second number: ")
            # call user selected selected calc function with arguments
            answer = calc_functions[operation](operand1, operand2)
            print("Answer is ", answer)
            # store current calculation's data to last_calculation string
            # and append that data to calc_history list
            last_calculation = "{0} {1} {2} = {3}".format(
                operand1, operation, operand2, answer)
            calc_history.append(last_calculation)
            break

        # this block's functionality is same as previous block
        # but for trignometric calculations
        elif operation in calc_functions_trignometric:
            angle = float(input("Enter an angle in degrees: "))
            if operation == 'sin':
                answer = sine(angle)
            elif operation == 'cos':
                answer = cosine(angle)
            elif operation == 'tan':
                answer = tangent(angle)
            print("Answer is ", answer)
            last_calculation = "{0} {1}  = {2}".format(
                operation, angle, answer)
            calc_history.append(last_calculation)
            break

        # call history() function to print calculator history
        elif operation == 'h':
            history()

        else:
            print("Enter a valid operation")

    # terminate the program or do another calculation
    while True:
        final_response = input(
            "Do you want to perform another calculation? (yes/no)")
        if final_response.lower() == "no":
            print("Program ended")
            exit()
        else:
            calculator()


# calling the calculator function to start calculator
calculator()
