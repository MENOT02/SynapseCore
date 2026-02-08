# test_synapsecore.py
"""
Tests for SynapseCore module.
"""

import unittest
from synapsecore import SynapseCore

class TestSynapseCore(unittest.TestCase):
    """Test cases for SynapseCore class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = SynapseCore()
        self.assertIsInstance(instance, SynapseCore)
        
    def test_run_method(self):
        """Test the run method."""
        instance = SynapseCore()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
