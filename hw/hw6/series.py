# Homework 6 : Mathematical series : Fibonacci Series and Lucas Numbers

# This program generates the nth number of the Fibonacci series and Lucas Numbers.

###########################################################################
###Funcation definition for the fibonacci series. This function has one paramneter 'n' and returns a value which is the nth value in the series.
###########################################################################
###

def fibonacci(n):
    # Variables to hold intermediate results. The first two values of the series are assigned by default.
    f1 = 0
    f2 = 1
    # The first value of the series is f1 , second value is f2 by default and next subsequent value is calulated and assigned to f3

    for i in range(2, n):        
        f3 = f1 + f2
        f1 = f2
        f2 = f3
        i = i + 1

    if n == 1:
        nth_value = f1
    elif n == 2:
        nth_value = f2
    else:
        nth_value = f3

    return nth_value
###########################################################################
###Funcation definition for the Lucas Number. This function has three paramneters, first paramneter is the nth value of the series to be calculated. Second and third parameters are the first and second values of the series.
###########################################################################
###

def lucas(larg1, larg2, larg3):
    # First and second values of the series are assigned to variables.
    f1 = larg2
    f2 = larg3
    #loop is executed if the input nth value of the series is more than 2.
    for i in range(2, larg1):
        f3 = f1 + f2
        f1 = f2
        f2 = f3
        i = i + 1
    # The variable nth_value holds the result.
    if larg1 == 1:
        nth_value = f1
    elif larg1 == 2:
        nth_value = f2
    else:
        nth_value = f3

    return nth_value


###########################################################################
### Function called sum_series, with one required parameter and two optional parameters. The required parameter will determine the nth value of the series to be calculated. The two optional parameters will have default values of 0 and 1 and will determine the fibonacci series or the lucas number.
###########################################################################
### 
def sum_series(arg1, arg2 = 0, arg3 = 1):
    if arg2 == 0 and arg3 == 1:
        # res variable holds ibonacci series of the nth value  
        res = fibonacci(arg1)
    else:
        res = lucas(arg1, arg2, arg3)
    return res
########################################################################
#### This block of code has assert statements to ensure the program works correctly.
#######################################################################


if __name__ == "__main__":
    # It has one argument and hence the fibonacci series function is called. The "1"st  value of the series is 0, assert returns True.  
    assert sum_series(1) == 0
    # It has one argument and hence the fibonacci series function is called. The "2"st  value of the series is 1, assert returns True.  
    assert sum_series(2) == 1
    # It has one argument and hence the fibonacci series function is called. The "6"st  value of the series is 5, assert returns True.  
    assert sum_series(6) == 5
    # It has three arguments. The second argument is 0 and third argument is 1, hence the fibonacci series function is called. The "8"st  value of the series is 13, assert returns True.  
    assert sum_series(8, 0, 1) == 13
        # It has three arguments. The second argument is 2 and third argument is 1, hence the lucas numbers function is called. The "1"st  value of the series is 2, assert returns True.  
    assert sum_series(1, 2, 1) == 2
        # It has three arguments. The second argument is 2 and third argument is 1, hence the lucas numbers function is called. The "3"st  value of the series is 3, assert returns True.  
    assert sum_series(3, 2, 1) == 3
        # It has three arguments. The second argument is 4 and third argument is 2, hence the lucas number function is called. The "3"st  value of the series is 6, assert returns True.  
    assert sum_series(3, 4, 2) == 6





