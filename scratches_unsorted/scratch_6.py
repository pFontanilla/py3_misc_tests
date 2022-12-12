
from Tkinter import *
import threading
from time import sleep

threadX = None
threadY = None

lockX = threading.Lock()
lockY = threading.Lock()

# def printbar(bar):
#
#     global x, y
#
#     if bar == statusBarx:
#         while True:
#             bar.configure(text="{}".format(x))
#     else:
#         while True:
#             bar.configure(text="{}".format(y))

class counting(object):

    def __init__(self):
        self.x = 0
        self.y = 0
        self.lockX = threading.Lock()
        self.lockY = threading.Lock()

        # self.__threadPY = threading.Thread(target=self.__printbarY, args=[statusBary])
        # self.__threadPY.setDaemon(True)
        # self.__threadPX = threading.Thread(target=self.__printbarX, args=[statusBarx])
        # self.__threadPX.setDaemon(True)

    # def startprintbarX(self):
    #     self.__threadPX.start()
    # def startprintbarY(self):
    #     self.__threadPY.start()
    # def __printbarX(self, bar):
    #     while True:
    #         sleep(0.01)
    #         with self.lockX:
    #             bar.configure(text="{}".format(self.x))
    # def __printbarY(self, bar):
    #     while True:
    #         sleep(0.01)
    #         with self.lockY:
    #             bar.configure(text="{}".format(self.y))
    def incrementbarY(self):
        print("Adding to 'y'")
        thread = threading.Thread(target=self.addY)
        thread.setDaemon(True)
        thread.start()
    def addY(self):
        while True:
            sleep(0.01)
            self.lockY.acquire()
            self.y = self.y + 1
            if(self.y > 10000):
                self.y = 0
            statusBary.configure(text="{}".format(self.y))
            self.lockY.release()
            # 'with' causing errors with tk configure
            # with self.lockY:
            #     self.y = self.y + 1
            #     if(self.y > 10000):
            #         self.y = 0
            #     statusBary.configure(text="{}".format(self.y))
    def incrementbarX(self):
        print("Adding to 'x'")
        thread = threading.Thread(target=self.addX)
        thread.setDaemon(True)
        thread.start()
    def addX(self):
        while True:
            sleep(0.01)
            self.lockX.acquire()
            self.x = self.x + 1
            if(self.x > 10000):
                self.x = 0
            statusBarx.configure(text="{}".format(self.x))
            self.lockX.release()
            # 'with' causing errors with tk configure
            # with self.lockX:
            #     self.x = self.x + 1
            #     if(self.x > 10000):
            #         self.x = 0
            #     statusBarx.configure(text="{}".format(self.x))
    def decrementbarY(self):
        print("Subbing to 'y'")
        thread = threading.Thread(target=self.subY)
        thread.setDaemon(True)
        thread.start()
    def subY(self):
        while True:
            sleep(0.01)
            self.lockY.acquire()
            self.y = self.y - 1
            if (self.y < 0):
                self.y = 10000
            statusBary.configure(text="{}".format(self.y))
            self.lockY.release()
            # 'with' causing errors with tk configure
            # with self.lockY:
            #     self.y = self.y - 1
            #     if (self.y < 0):
            #         self.y = 10000
            #     statusBary.configure(text="{}".format(self.y))
    def decrementbarX(self):
        print("Subbing to 'x'")
        thread = threading.Thread(target=self.subX)
        thread.setDaemon(True)
        thread.start()
    def subX(self):
        while True:
            sleep(0.01)
            self.lockX.acquire()
            self.x = self.x - 1
            if (self.x < 0):
                self.x = 10000
            statusBarx.configure(text="{}".format(self.x))
            self.lockX.release()
            # 'with' causing errors with tk configure
            # with self.lockX:
            #     self.x = self.x - 1
            #     if (self.x < 0):
            #         self.x = 10000
            #     statusBarx.configure(text="{}".format(self.x))

window_base = Tk()
window_base.title("ROH MS Determination via HERS MS")
window_base.geometry("800x120")

# Status Bar X Frame
frame_statusx = Frame(window_base)
frame_statusx.pack(side=BOTTOM, anchor=SW, fill=X)
statusBarx = Label(frame_statusx, text="0", bd=1, relief=SUNKEN, anchor=SW)
statusBarx.pack(side=BOTTOM, anchor=SW, fill=X)

# Status Bar Y Frame
frame_statusy = Frame(window_base)
frame_statusy.pack(side=BOTTOM, anchor=SW, fill=X)
statusBary = Label(frame_statusy, text="0", bd=1, relief=SUNKEN, anchor=SW)
statusBary.pack(side=BOTTOM, anchor=SW, fill=X)

# Buttons Frame
frame_mainbuttons = Frame(window_base)
frame_mainbuttons.pack(side=BOTTOM, anchor=SE)
# Quit Button
button_quit = Button(frame_mainbuttons, text="Quit", command=lambda: window_base.destroy())
button_quit.pack(side=RIGHT, anchor=SE)

counter = counting()

# Execute Button
button_executeXinc = Button(frame_mainbuttons, text="Increment 'X'", command=lambda: counter.incrementbarX())
button_executeXinc.pack(side=RIGHT, anchor=SE)
# Execute Button
button_executeYinc = Button(frame_mainbuttons, text="Increment 'Y+'", command=lambda: counter.incrementbarY())
button_executeYinc.pack(side=RIGHT, anchor=SE)
# Execute Button
button_executeXdec = Button(frame_mainbuttons, text="Decrement 'X'", command=lambda: counter.decrementbarX())
button_executeXdec.pack(side=RIGHT, anchor=SE)
# Execute Button
button_executeYdec = Button(frame_mainbuttons, text="Decrement 'Y'", command=lambda: counter.decrementbarY())
button_executeYdec.pack(side=RIGHT, anchor=SE)

# counter.startprintbarX()
# counter.startprintbarY()

# threadPX = threading.Thread(target=printbar, args=[statusBarx])
# threadPX.setDaemon(True)
# threadPX.start()
# threadPY = threading.Thread(target=printbar, args=[statusBary])
# threadPY.setDaemon(True)
# threadPY.start()

# threadPX.start()
# threadPX.join()
# threadPY.start()
print("printing now")
# print("{}".format(button_executeYdec._name))
window_base.mainloop()