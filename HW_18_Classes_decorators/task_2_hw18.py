
class Boss:

    def __init__(self, b_id: int, name: str, company: str):
        self.b_id = b_id
        self.name = name
        self.company = company
        self._workers = []

    def __str__(self):
        return f"{self.name} -- {self.company}"

    @property
    def workers(self):
        return f"Here are all workers of this Boss:\n {self._workers}"
    
    def new_worker(self, new_id, new_name):
        for worker in self._workers:
            if worker.name == new_name:
                raise ValueError("This worker already exists")
        new_worker = Worker(new_id, new_name, self.company, self)
        self._workers.append(new_worker)
        print(f"New worker added: {new_worker} added")

                

    

class Worker:

    def __init__(self, w_id, name, company, boss):
        self.w_id = w_id
        self.name = name
        self.company = company

        # Checks if attribute is instance of the Boss class before assigning
        if isinstance(boss, Boss) == False:
            raise ValueError("Boss atribute should be an instance of the Boss class")
        self._boss = boss

    def __str__(self):
        return f"Worker {self.name} -- {self.company}"
    
    def __repr__(self):
        return f"ID - {self.w_id}, Name - {self.name}, Company - {self.company}, {self.boss}"
        
        
    @property
    def boss(self):
        return f"This workers boss is {self._boss}"
    
    @boss.setter
    def boss(self, new_boss: Boss):

        # Checks if attribute is instance of the Boss class before assigning
        if isinstance(new_boss, Boss) == False:
            raise ValueError("Boss atribute should be an instance of the Boss class")
        
        self._boss = new_boss
        print(f"{self.name}'s new boss is {self._boss}")

            
            
            
b_1 =Boss(7, "James Bond", "MI6")
print(b_1)

print("*" * 20)

w_1 = Worker(321, "Emma", "MI6", b_1)
print(w_1)

w_1.boss = Boss(900, "Elon Mask", "SpaceX")

print("*" * 20)

b_1.new_worker(3, "Sam")
b_1.new_worker(5667, "Tom")
print(b_1.workers)
