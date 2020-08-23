class Person:
    def __init__(self, name):
        self.name = 'aaa'
        self.q = 1

    # def __str__(self):
    #     if self.q:
    #         return f'{self.name}ich'
    #     return self.name

p = Person('Ivan')

print_str = p.name if p.q else f'{p.name}'
