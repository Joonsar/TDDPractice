# Tehty 4.5.2023

from io import StringIO
import string
import unittest

def fizzbuzz():
    try:
        print("Enter the character, height, width, fill: ")
        print("'Example: 0 20 50 yes'")
        user_input = input(">>> ").split()

        character = user_input[0]
        height, width = int(user_input[1]), int(user_input[2])
       
       # Limit width and height to 50
        if height > 50:
            height = 20
        if width > 100:
            width = 50
    
        fill = user_input[3].lower() in ["yes", "y"]

        if fill:
            area = (character * width + "\n") * height
        else:
            area = character * width + "\n" + (character + " " * (width - 2) + character + "\n") * (height - 2) + character * width + "\n"

        if fill:
            for i in range(height):
                for j in range(width):
                    print(character, end="")
                print()
        else:
            for i in range(height):
                for j in range(width):
                    if i == 0 or i == height - 1 or j == 0 or j == width - 1:
                        print(character, end="")
                    else:
                        print(" ", end="")
                print()
        return area
    
    except (ValueError, IndexError):
        print("Invalid input. Please enter the correct format.")
        return fizzbuzz()
        
        
class TestFizzBuzz(unittest.TestCase):
    def setUp(self):
        self.user_input = "0 20 50 yes".split()
        self.marker = self.user_input[0]
        self.height, self.width = int(self.user_input[1]), int(self.user_input[2])
        self.fill = self.user_input[3].lower() in ["yes", "y"]
        
    def test_inputExists(self):
        self.assertIsNotNone(self.user_input)

    def test_inputType(self):
        self.assertIsInstance(self.marker, str)
        self.assertIsInstance(self.height, int)
        self.assertIsInstance(self.width, int)
        self.assertIsInstance(self.fill, bool)

    def test_character(self):
        """Test that the character input is a single character."""
        self.assertEqual(len(self.marker), 1)

    def test_heightWidth(self):
        """Test that the height and width inputs are positive ints."""
        self.assertGreater(self.height, 0)
        self.assertGreater(self.width, 0)
    
    def test_widthLimit(self):
        """Test that the width is not greater than 50."""
        self.assertLessEqual(self.width, 50)
    
    def test_heightLimit(self):
        """Test that the height is not greater than 50."""
        self.assertLessEqual(self.height, 20)
            
    def test_fillEdges(self):
        """Test that the fill edges input is a boolean value."""
        self.assertIsInstance(self.fill, bool)        
    fizzbuzz()
if __name__ == '__main__':
    unittest.main()
    


