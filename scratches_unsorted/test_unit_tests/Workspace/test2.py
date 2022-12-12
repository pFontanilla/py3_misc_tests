import unittest
import assertTestValues
from assertTestValues import assertResultsEqual

# Test function
class TestPeripheryCommunication2(unittest.TestCase):

    # Startup
    def setUp(self):
        print("csmTest running")

    # This function will be called after the test function execution
    def tearDown(self):
        print("test done")

    def test_PeripheryCom1(self):
        # self.assertEqual("hi", "hi")
        assertResultsEqual("hi", "bye")

    def test_PeripheryCom2(self):
        # self.assertEqual("hi", "hi")
        fake_list = [1]
        if fake_list[3] == 7:
            print("how")
        assertResultsEqual("hi", "hi")


if __name__ == '__main__':
    unittest.main()
