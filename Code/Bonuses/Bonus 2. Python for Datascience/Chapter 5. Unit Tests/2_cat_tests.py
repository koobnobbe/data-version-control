import unittest

class CatTest(unittest.TestCase):
    '''Unit Tests for the Cat class'''
    def initialized_properly(self):
        # Arrange & Act
        cat = Cat("name", "spicies", 5)

        # Assert
        self.assertEqual(cat.name, 'name')
        self.assertEqual(cat.spicies, 'spicies')
        self.assertEqual(cat.age, 5)

    def str_overridden(self):
        # Arrange
        cat = Cat("name", "spicies", 5)

        # Act
        info = cat.__str__()

        # Assert
        self.assertEqual(info, 'Name: name | Spicies: spicies | Age: 5')

    def speak_test(self):
        # Arrange
        cat = Cat("name", "spicies", 5)

        # Act
        spoken = cat.speak()

        # Assert
        self.assertEqual(spoken, 'name say meeeeeeooooow')

    def birthday_test(self):
        # Arrange
        cat = Cat("name", "spicies", 5)

        # Act
        cat.birthday()

        # Assert
        self.assertEqual(cat.age, 6)

    def jump_test(self):
        # Arrange
        cat = Cat("name", "spicies", 2)

        # Act
        info = cat.jump()

        # Assert
        self.assertEqual(info, 'name jumped 1 meters!')

if __name__ == '__main__':
    unittest.main()