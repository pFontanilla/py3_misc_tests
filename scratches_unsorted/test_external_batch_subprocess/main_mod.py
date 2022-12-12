import subprocess
import os
import time
from multiprocessing import Process

# Testing execution and stopping of external batch.
# subprocess for external while Process/fork for internal python code

# Test 1
# Below behaviour is that the batch gets terminated, but the python which the batch calls will still run.
# This makes sense because the python is a separate process from the batch

def test1():

    command = "infinite.bat"

    p = subprocess.Popen(command, shell=True, cwd=os.getcwd(), capture_output=True)
    # p = subprocess.Popen("infinite.bat", cwd=os.getcwd())

    time.sleep(1)
    print("************ done sleep *******************")

    p.kill()
    print("killed process")
    print(p.poll())

    while True:
        continue


if __name__ == "__main__":

    test1()
