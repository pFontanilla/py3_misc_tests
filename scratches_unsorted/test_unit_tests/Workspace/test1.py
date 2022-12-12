import unittest
import assertTestValues
from assertTestValues import assertResultsEqual

# Test function
class TestPeripheryCommunication1(unittest.TestCase):

    # Startup
    def setUp(self):
        print("csmTest running")

    # This function will be called after the test function execution
    def tearDown(self):
        print("test done")

    def test_PeripheryCom3(self):
        # self.assertEqual("hi", "hi")
        assertResultsEqual("hi", "bye")

    def test_PeripheryCom4(self):
        # self.assertEqual("hi", "hi")
        assertResultsEqual("hi", "hi")


# Step 1. Clean the fault buffer
ReadFaults()

# Step 2. Make Mcu unavailable, by blocking Mcu telegarms
blockCsmMessage(str(subRack), str(slot), "0")

# Step 3. Keep some delay (1 cycle only, which should not give enough time to raise a fault)
trackSleepCycle(oteParms["cycleTime"] * 2, 1)

# Step 4. Loop through the fault buffer 100 times to check if there is a fault, and if the fault is the expected fault
# In this situation, a fault should not be raised.
fault = FwFault.FW_FAULT_PAMREPLICA_COMM_LOST.value
faultRaised = assertMcuFault(test_steps, mcuId, fault, "FW_FAULT_PAMREPLICA_COMM_LOST")
assertResultsEqual(test_steps, "MCU fault reported", str(cardName), "NA", faultRaised, False)


if __name__ == '__main__':
    unittest.main()
