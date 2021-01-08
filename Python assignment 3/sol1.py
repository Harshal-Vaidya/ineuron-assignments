def myreduce(function, iterable, initializer=None):
    it = iter(iterable)
    if initializer is None:
        value = next(it)
    else:
        value = initializer
    for element in it:
        value = function(value, element)
    return value


def myfilter(function, iterable):
    list_result=[]
    for element in iterable:
        if function(element) == True:
            list_result.append(element)
    return list_result


# def sum(n1,n2):
#     return(n1+n2)

# def even(n):
#     if n%2==0:
#         return True
#     else:
#         return False        
    
