'''Basic Calculator Program

Create a simple Python program that asks the user to input two numbers and a mathematical operation (addition, subtraction, multiplication, or division).
Perform the operation based on the user's input and print the result.
Example: If a user inputs 10, 5, and +, your program should display 10 + 5 = 15.

Note: Upload the code to GitHub and submit the GitHub link'''


a = int(input("what is your first number: "))
b = input ("choose a sign +,-,*,/: " )
c = int(input("What is your second number: "))

def calc(a,c):
    if b =='+' :
        print (a+c)
    elif b =='-':
        print (a-c)
    elif b =='*':
        print(a*b)
    elif b =='/':
        print(a/b)
    elif b!= '+' or '-' or '*' or '/':
        print  ("include the correct sign, start again") 
    else:
        print('i cant work with strings')

calc(a,c)



    


