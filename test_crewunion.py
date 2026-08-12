# test_crewunion.py
"""
Tests for CrewUnion module.
"""

import unittest
from crewunion import CrewUnion

class TestCrewUnion(unittest.TestCase):
    """Test cases for CrewUnion class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = CrewUnion()
        self.assertIsInstance(instance, CrewUnion)
        
    def test_run_method(self):
        """Test the run method."""
        instance = CrewUnion()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
