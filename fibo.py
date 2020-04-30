# Program to display the Fibonacci sequence up to n-th number

# variable is gotten from the word 'vary'

#getFibonacci - function name
#nterms - parameters
#functions are dependent on their parameter

# Ambiguity One
def getFibonacciSequence(nterms):
    
    # first two numbers
    n1, n2 = 0, 1
    count = 0
    
    # check if the number entered is positive
    if nterms <= 0:
       print("Please enter a positive number")
    # check if the number entered is 1
    elif nterms == 1:
       print(n1)
    else:
    #   print("Fibonacci sequence:")
       while count < nterms:
           print(n1) #0, 1
           nth = n1 + n2 # 1 + 1 = 2
           # update values
           n1 = n2 # 1
           n2 = nth # 2
           count += 1  # 1 + 1 = 2
 


number = int(input("Enter A Number: "))
print (type(number)) 
getFibonacciSequence(number)


# function declaration to add two numbers
def add(num1, num2):
    print(num1 + num2)
    
#function declaration to say a name
def sayMyName(name):
    print("my name is " + name)

#function call
# add(5, 7)
# add(20, 100)
# sayMyName("Tunde")
# sayMyName("Dami")

# getFibonacciSequence(15)

# Ambiguity Two
def getFibonacciSequenceUpTo(number):
    n1, n2 = 0, 1
    nth = 0
    while nth < number:
      print(nth)
      nth = n1 + n2
      # update values
      n1 = n2
      n2 = nth
          
# getFibonacciSequenceUpTo(15)
