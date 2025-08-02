# test_quantumpulse.py
"""
Tests for QuantumPulse module.
"""

import unittest
from quantumpulse import QuantumPulse

class TestQuantumPulse(unittest.TestCase):
    """Test cases for QuantumPulse class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = QuantumPulse()
        self.assertIsInstance(instance, QuantumPulse)
        
    def test_run_method(self):
        """Test the run method."""
        instance = QuantumPulse()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
