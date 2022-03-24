import random
res = sum([random.randrange(1, 50, 1) for i in range(10)])
print("Random number summation list is : " + str(res))

def greet():
    ""
    Input: none
    #This function just prints "hello"
    ""
    print('Hello!')

greet()
print(help(greet))

def greet(name):
    ""
    Input:none
    #this function just prints "hello, <name>"
    ""
    print('Helo,', str(name). capitalize())

greet("james")

