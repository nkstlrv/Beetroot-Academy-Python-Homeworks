class InRange:

    def __init__(self, start, end, step=1):
        self.value = start
        self.end = end
        self.step = step

    def __iter__(self):
        return self

    def __next__(self):
        if self.value >= self.end:
            raise StopIteration
        value = self.value
        self.value += self.step
        return value


for item in InRange(-5, 10, 5):
    print(item)

