from multiprocessing import Process
from os import getpid
import time
import math

class Suite:

    def __init__(self):
        self.processes = {
            "process1" : Process(target=self.call_print),
            "process2" : Process(target=self.call_print),
        }

    def start_infinite1(self):
        self.processes["process1"].start()

    def stop_infinite1(self):
        self.processes["process1"].terminate()

    @staticmethod
    def call_print():
        print("Starting PID '{}'".format(getpid()))
        pid = getpid()
        time.sleep(2)
        for i in range (99999999):
            print("pid '{}' @ count {}, value {}".format(pid, i, int(math.factorial(i%170)/(i+1))))

def main():

    test = Suite()
    test2 = Suite()
    # test.start_infinite1()
    test.processes["process1"].start()
    # test2.processes["process2"].start()
    # test2.processes["process1"].start()
    test.processes["process2"].start()

if __name__ == "__main__":

    main()