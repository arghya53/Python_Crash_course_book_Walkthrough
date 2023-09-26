import unittest

from name_function import get_formatted_name

class NameTestClass(unittest.TestCase): # the class inherits from unittest.TestCase
    '''Test for name_function.py '''
    
    def test_first_last_name(self):
        """Does names like 'Arghya Biswas' pass?  """
        formatted_name = get_formatted_name('arghya', 'biswas')
        self.assertEqual(formatted_name, 'Arghya Biswas') # This method compares the output of the function with our expected value
    
    """ We are going to pass the second test """
    def test_first_middle_last_name(self):
        """ Does the name 'Arghya Biswas Parag' pass? """
        formatted_name = get_formatted_name('arghya', 'parag', 'biswas')
        self.assertEqual(formatted_name, 'Arghya Biswas Parag')

if __name__ == '__main__': # As this test file is being run as the main program and not as an imported one, the value of __name__ is set to '__main__'.

    unittest.main()
              

    
