# Import the TestCase class from unittest
from unittest import TestCase

# Create TryTesting, a subclass of TestCase
class TryTesting(TestCase):
    # Write a method in TryTesting for each test
    def test_always_passes(self):
        # Use one of the self.assert* methods from unittest.TestCase to make assertions
        self.assertTrue(True)
        
    def test_always_fail(self):
        self.assertTrue(False)
        
        
# Run by python -m unittest "filename"
# run by pytest