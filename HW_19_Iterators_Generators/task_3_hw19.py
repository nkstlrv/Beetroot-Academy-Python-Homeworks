class MyIterable:
    def __init__(self, my_object):
        self._my_object = my_object
        self.iterable_object = iter(self.get_item)

    def __iter__(self):
        return self

    def __next__(self):
        try:
            return next(self.iterable_object)
        except StopIteration:
            raise StopIteration

    @property
    def get_item(self):
        return self._my_object


object_1 = MyIterable(['Monday', 'Tuesday', 33, [1, 2, 3]])

for item in object_1:
    print(item)

print('-' * 100)

print(object_1.get_item[0])
print(object_1.get_item[3])
print(object_1.get_item[33])



