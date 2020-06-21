#!/usr/bin/python
# -*- coding: utf-8 -*-


import sys
import math

# Functions to apply basic arithmetic
# operations on 2 numbers 
# Each func, takes 2 numbers as input

add = lambda a, b: a + b 
subtract = lambda a, b: a - b 
multiply = lambda a, b: a * b 
divide = lambda a, b: a / b 
modulus = lambda a, b: a % b 


sine = lambda a: math.sin(a)
cosine = lambda a: math.cos(a)
tangent = lambda a: math.tan(a)

faren = lambda a: ((a - 32) * (5 / 9))
celcius = lambda a: (a * (9 / 5) + 32)
dollar = lambda a: (a * (0.89))  ##current conversion rate at time of writing this program
euro = lambda a: (a / (0.89))    ##current conversion rate at time of writing this program
pound = lambda a: (a / (2.205))
kilo = lambda a: (a * (2.205))





# CLI
# Testing/Playing Interface
i = 0
while True:
    selection = input("\n\n[{}] Exit(press e), Calculate(press cal) or Convert(press con): ".format(i))
    if selection == "cal":
        op = input("\nAdd(press a), \nSubtract(press s), \nMultiply(press m),\nDivide(press d), \nModulus(press mo), \nSine(press sin), \nCosine(press cos), \nTangent(press tan): ").strip().lower()
        if op == "a":
            print("  Sum: " + str(add(float(input("\nN1: ")), float(input("N2: ")))))
        elif op == "s":
            print("  Subtracted: " + str(subtract(float(input("\nN1: ")), float(input("N2: ")))))
        elif op == "m":
            print("  Multiplied: " + str(multiply(float(input("\nN1: ")), float(input("N2: ")))))
        elif op == "d":
            print("  Divided: " + str(divide(float(input("\nN1: ")), float(input("N2: ")))))
        elif op == "mo":
            print("  Modulus: " + str(modulus(float(input("\nN1: ")), float(input("N2: ")))))
        elif op == "sin":
            print("  Sine: " + str(sine(float(input("\nNumber: ")))))
        elif op == "cos":
            print("  Cosine: " + str(cosine(float(input("\nNumber: ")))))
        elif op == "tan":
            print("  Tangent: " + str(tangent(float(input("\nNumber: ")))))
            
        i += 1
    elif selection == "con":
        convert = input("\nFarenheight to Celcius(press f), \nCelcius to Farenheight(press c), \nDollar to Euro(press $), \nEuro to dollar(press euro), \nPounds to Kilograms(press lb), \nKilograms to pounds(press kilo): ").strip().lower()
        if convert == "f":
            print("  Farenheight to Celcius: " + str(faren(float(input("\nEnter Degrees: ")))))
        if convert == "c":
            print("  Celcius to Farenheight: " + str(celcius(float(input("\nEnter Degrees: ")))))
        if convert == "$":
            print("  Dollar to Euro: " + str(dollar(float(input("\nEnter Dollars: ")))))
        if convert == "euro":
            print("  Euro to Dollar: " + str(euro(float(input("\nEnter Euros: ")))))
        if convert == "lb":
            print("  Pounds to Kilograms: " + str(pound(float(input("\nEnter Pounds: ")))))
        if convert == "kilo":
            print("  Kilograms to Pounds: " + str(kilo(float(input("\nEnter Kilograms: ")))))
            
         
    else:
        print("\nHope you enjoyed!")
        sys.exit()