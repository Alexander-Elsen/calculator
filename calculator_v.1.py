import time 
import string

def main():
   print('Welcome to calculator v.1!')
   while True:
   
       
       number_1 = float(input('What is your first number?'))
       calculation = input('Wich calculation do you want to do(+, -, * or /)?')
       number_2 = float(input('What is your second number?'))
       if calculation == '+':
           calculationa = number_1 + number_2
           print(calculationa)
       elif calculation == '-':
           calculationb = number_1 - number_2
           print(calculationb)
       elif calculation == '*':
           calculationc = number_1 * number_2
           print(calculationc)
       elif calculation == '/':
           calculationd = number_1 / number_2
           print(calculationd)
     
if __name__ == "__main__":
    main()