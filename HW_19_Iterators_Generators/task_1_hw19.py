def with_index(iterable, start=0):
    start_index = start
    iter_object = iter(iterable)
    while True:
        try:
            yield start_index, next(iter_object)
            start_index += 1
        except StopIteration:
            break


my_enumerate = with_index([1, None, 3, True, 5, 'a', 'hello there', (33, 88, 0)])

for item in my_enumerate:
    print(item)


