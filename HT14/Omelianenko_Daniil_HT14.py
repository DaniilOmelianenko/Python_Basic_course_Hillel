class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.friends = []

    def know(self, other_person):
        if other_person in self.friends:
            #print('You already know this person')
            return
        self.friends.append(other_person)
        other_person.know(self)
        #print(f'Now you know {other_person}')

    def is_known(self, other_person):
        if other_person in self.friends:
            return True
        return False


Danil = Person('Daniil', 29)
Alina = Person('Alina', 27)
print(Danil.friends)
print(Danil.is_known(Alina))
print(Danil.friends)
Danil.know(Alina)
print(Danil.friends)
#print(Danil.is_known(Alina))
