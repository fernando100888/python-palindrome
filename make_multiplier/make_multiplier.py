def make_multiplier(x):

    def multiplier(n):
        return x * n

    return multiplier

times10 = make_multiplier(10)
times4 = make_multiplier(4)

print(times10(3))
print(times4(5))
print(times10(times4(2))) 

# return 30, 20, 80

''' we have a make_multiplier function that receives a parameter x, and within this function we have
 another nested function, called multiplier that has a parameter n, this function remembers a value
  of a higher scope (x), finally multiplier is returned.


With this we can create custom functions like times10 and times4, which will be the result of 
executing the make_multiplier function with the value 10 and 4 respectively, 10 and 4 will be the 
values of x, but we don't have the values of n yet. So we can write times10(3), times4(5), and times10
(times4(2))), so that 3, 5, 2 and times4(2) are the respective parameters n of the multiplier function found
 inside the make_multiplier function, and then we can print these results'''
