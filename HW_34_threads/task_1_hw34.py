from threading import Thread


class Counter(Thread):
    counter = 0
    rounds = 100000

    def run(self):
        for i in range(self.rounds):
            Counter.counter += 1

t1 = Counter()
t2 = Counter()
t1.start()
t2.start()
t1.join()
t2.join()

print(Counter.counter)