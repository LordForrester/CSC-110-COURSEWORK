import unittest
import geometry

class TestMyStuff(unittest.TestCase):

    def test_cubeArea(self):
        self.assertEqual(150, geometry.cubeArea(5)) 

    


def main():
    # creates the suite from test cases above
   
    
    suite = unittest.TestLoader().loadTestsFromTestCase(TestMyStuff)
    # run that test suite, being somewhat wordy
    unittest.TestTestRunner(verbosity=2).run(suite)


main()




