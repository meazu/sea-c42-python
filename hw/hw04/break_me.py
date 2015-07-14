#Function when called throws a name exception.
def exhibit_name_error():
    a = 10   
    sum = a + b # 'b' is not defined and trying sum it with 'a'
    return sum

#Function when called throws a type exception.        
def exhibit_type_error():
    a = 10
    b = 'Apple'
    div = a // b # value of 'a' is int and 'b' is string type and 
                     # performing divions operation.
    return div
#Function when called throws an attribute exception.
def exhibit_attribute_error():
    a = [10, 20, 30]
    b = 'string'
    return (a.b)
