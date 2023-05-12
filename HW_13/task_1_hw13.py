
def our_func(something, *args, **kwargs):

    a = "first local var"
    b = "second local var"
    c = "third local var"
    
    return None

# The only way I've found 
print("\n Number of local vars is -->", our_func.__code__.co_nlocals)