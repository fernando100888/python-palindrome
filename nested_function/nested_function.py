#nested functions are functions that are created within another function
#1st example
def main():
    a = 1
    def nested():
        print(a)
    nested()
main() # 1
'''I define the function main that contains a value a=1 and it also contains another function called 
nested that prints the value of a and displays it. When calling the main function, it will give us 1,
 which is the value of a that was printed by the nested function inside the main function.'''





#2nd example
def main():
    a=1
    def nested():
        print(a)
    return nested
my_function = main()
my_function() # 1
'''in this example instead of executing nested, return nested. By doing this we can create variables,
 such as my_function, to which we assign the result of executing the main function. When this 
 happens, the variable a=1 is created, the nested function is created, which will print the value of 
 a, and nested is returned, so my_function will contain a function of type nested that will contain 
 everything what the function contains nested inside the main function, in this case 1. Since 
 my_function contains an object of type function, we can execute it using the parentheses of a 
 function. This technique in which values that are in higher scopes are remembered is called closures.'''





# 3rd example
def main():
    a = 1
    def nested():
        print(a)
    return nested
my_function = main()
my_function()
del(main)
my_function() #1
              #1
'''It's the same code, first it prints 1. But then we remove main with the python "del" keyword, with
 this we should also remove a=1, but this doesn't happen. Why? Because the nested function is 
 remembering the variable a from a higher scope, this, as we said, is a closure.'''
