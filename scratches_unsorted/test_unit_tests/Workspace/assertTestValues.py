
# Import supporting libraries
import time
import unittest

# from ote import oteGlobal
# from ote.oteGlobal import runLog, printResults
# from ote.oteSpawn import doTest, activateFW, getFwResp

class AssertFromUnit(unittest.TestCase):
    pass

def assertResultsEqual(actualValue, expected):
    if(actualValue == expected):
        result = 1
    else:
        result = 0
    # print(test_steps, testName, device, cycle, actualValue, expected,result)
    # printResults(test_steps, testName, {"device" : device},{"cycle" : str(cycle), "actual": str(actualValue), "result": str(expected)}, {"actual": str(actualValue), "result": str(expected)}, result)
    unit_asserts = AssertFromUnit()
    unit_asserts.assertEqual(actualValue, expected)
    #runLog("test PermanentDataRequest running")

def assertResultsEqual1(test_steps, testName, device, cycle, actualValue, expected):
    if(actualValue == expected):
        result = 1
    else:
        result = 0
    print(test_steps, testName, device, cycle, actualValue, expected,result)
    printResults(test_steps, testName, {"device" : device},{"cycle" : str(cycle), "actual": str(actualValue), "result": str(expected)}, {"actual": str(actualValue), "result": str(expected)}, result)
    unit_asserts = AssertFromUnit()
    unit_asserts.assertEqual(actualValue, expected)
    #runLog("test PermanentDataRequest running")


def assertFault(test_steps, exp_fault, faultName):
    activateFW({"name": 'getFaultLog_ProcessFwFault'})
    doc=getFwResp()
    ele = doc[0]
    is_faultcode =False
    cycle = "0"
    try:
        num_faults = ele.__dict__["_attributes"]["numFaults"]
        for i in range(0,int(num_faults)):
            activateFW({"name": 'getFaultLog_ProcessFwFault'})
            doc1=getFwResp()
            ele_1 = doc1[0]
            num_faults1=ele_1.__dict__["_attributes"]["numFaults"]
            num_faults=num_faults1
            cycle= ele_1.__dict__["_attributes"]["cycle"]
            fault=ele_1.__dict__["_attributes"]["fault"]
            if fault == str(exp_fault):
                printResults(test_steps,faultName,{},{"cycle":cycle,"FaultCode":fault},{"FaultCode":fault},True)
                runLog("{}{}".format("expected ",fault))
                is_faultcode=True
                break
            else:
                is_faultcode=False
        if not is_faultcode:
            printResults(test_steps,faultName,{},{"cycle":cycle,"FaultCode":"FaultCode not generated"},{"FaultCode":"FaultCode is not generated"},False)
            runLog("FaultCode is not generated")
    except AttributeError:
        pass
    unit_asserts = AssertFromUnit()
    unit_asserts.assertEqual(fault, str(exp_fault))
    return  is_faultcode
    #printResults(test_steps, testName, {"device" : device},{"cycle" : str(cycle), "actual": str(actualValue), "result": str(expected)}, {"actual": str(actualValue), "result": str(expected)}, result)
    #runLog("test PermanentDataRequest running")


def assertMcuFault(test_steps, exp_mcuId, exp_fault, faultName):
    activateFW({"name": 'getFaultLog_ProcessFwFault'})
    doc=getFwResp()
    ele = doc[0]
    is_faultcode =False
    cycle = "0"
    try:
        num_faults = ele.__dict__["_attributes"]["numFaults"]
        for i in range(0,int(num_faults)):
            activateFW({"name": 'getFaultLog_ProcessFwFault'})
            doc1=getFwResp()
            ele_1 = doc1[0]
            num_faults1=ele_1.__dict__["_attributes"]["numFaults"]
            num_faults=num_faults1
            cycle= ele_1.__dict__["_attributes"]["cycle"]
            fault=ele_1.__dict__["_attributes"]["fault"]
            mcuId=ele_1.__dict__["_attributes"]["p1"]
            if fault == str(exp_fault) and mcuId == str(exp_mcuId):
                printResults(test_steps,faultName,{},{"cycle":cycle,"FaultCode":fault},{"FaultCode":fault},True)
                runLog("{}{}".format("expected ",fault))
                runLog("FaultCode generated")
                is_faultcode=True
                break
            else:
                is_faultcode=False
        if not is_faultcode:
            printResults(test_steps,faultName,{},{"cycle":cycle,"FaultCode":"FaultCode not generated"},{"FaultCode":"FaultCode is not generated"},False)
            runLog("FaultCode not generated")
    except AttributeError:
        pass
    unit_asserts = AssertFromUnit()
    unit_asserts.assertEqual(fault, str(exp_fault))
    unit_asserts.assertEqual(mcuId, str(exp_mcuId))
    return  is_faultcode
    #printResults(test_steps, testName, {"device" : device},{"cycle" : str(cycle), "actual": str(actualValue), "result": str(expected)}, {"actual": str(actualValue), "result": str(expected)}, result)
    #runLog("test PermanentDataRequest running")


 

