class Mammal:
    def walk(self):
        print("I am walking")
    

class Dog(Mammal):
    def bark(self):
        print("Bark")


class Cat(Mammal):
    def be_annoying(self):
        print("Annoying!")


GermanShepherd = Dog()
GermanShepherd.walk()
GermanShepherd.bark()


Persian = Cat()
Persian.walk()
Persian.be_annoying()