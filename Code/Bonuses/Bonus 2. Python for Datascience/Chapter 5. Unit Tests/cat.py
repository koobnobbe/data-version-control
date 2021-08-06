class Cat(object):
    '''Class that abstracts cats'''
    def __init__(self, name, spicies, age):
        self.name = name
        self.spicies = spicies
        self.age = age

    def __str__(self):
        return f'Name: {self.name} | Spicies: {self.spicies} | Age: {self.age}'

    def speak(self):
        return f'{self.name} say meeeeeeooooow'
    
    def birthday(self):
        self.age += 1

    def jump(self):
        return f'{self.name} jumped {2/self.age} meters!'