import random

for i in range(3):
    print(random.random())
    print(random.randint(10, 20))


names = ["John", "Bob", "Mosh", "Mary"]
leader = random.choice(names)
print(leader)