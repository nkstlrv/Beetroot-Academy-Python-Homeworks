# Task 2
# Write a decorator that takes a list of stop words and replaces them with * inside the decorated function


from functools import wraps

def stop_words(words: list):
    @wraps(words)
    def function(func):
        def arguments(*args, **kwargs):
            a = func(*args, **kwargs)
            a = a.split()
            a = ['*' if item in words else item for item in a]
            return " ".join(a)
        return arguments
    return function


@stop_words(['Coca-Cola', 'Porsche'])
def create_slogan(name):
    s = f" {name} drinks Coca-Cola in his brand new Porsche !"
    return s

print(create_slogan(name='Python'))

