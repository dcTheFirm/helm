import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from app.main import VERSION

class AppTests(unittest.TestCase):
    def test_version(self):
        self.assertEqual(VERSION, "1.0.0")

if __name__ == "__main__":
    unittest.main()
