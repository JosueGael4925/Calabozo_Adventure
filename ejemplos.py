#COMPRENSIÓN DE LISTAS CON CONDICIÓN []

letras = ['a', 'b', 'c', 'd', 'e']
uppercase_letras = [letra.upper() for letra in letras if letra != 'c']
print(uppercase_letras)  # OUTPUT: ['A', 'B', 'D', 'E']


#DESEMPAQUETAMIENTO EXTENDIDO

first, *middle, last = [10, 20, 30, 40, 50]
print(first, middle, last)  # OUTPUT: 10 [20, 30, 40] 50


#ENUMERATE CON COMPRENSIÓN DE LISTAS

frutas = ['manzana', 'uva', 'mango']
indexed_frutas = [(index, fruta) for index, fruta in enumerate(frutas)]
print(indexed_frutas)  # OUTPUT: [(0, 'manzana'), (1, 'uva'), (2, 'mango')]



#HERENCIAS MULTIPLE

class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating.")

    def sleep(self):
        print(f"{self.name} is sleeping.")
class Flyable:
    def fly(self):
        print(f"{self.name} is flying.")
class Bird(Animal, Flyable):
    def __init__(self, name):
        super().__init__(name)
bird = Bird("Sparrow")
bird.eat()  # Output: Sparrow is eating.
bird.sleep()  # Output: Sparrow is sleeping.
bird.fly()  # Output: Sparrow is flying.



#METODOS ESTATICOS

class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b

result = MathUtils.add(5, 3)
print(result)  # Output: 8

#STREAM REPRESENTATION

data = [1, 2, 3, 4, 5]

for item in data:
    # Procesar cada elemento
    print(item)