import unittest
# import prueba

class TestMyModule(unittest.TestCase):     
        def test_sum(self):
            self.assertEqual(prueba.sum(5, 7), 10)

if __name__ == "__main__":
    unittest.main()