from Tkinter import *

window_base = Tk()

choices_persistent = [
    ("True", True),
    ("False", False),
]

choice_pers = BooleanVar()
choice_pers.set(True)

# Frame containing persistency check radio buttons
frame_persistent = Frame(window_base)
frame_persistent.pack(side=TOP, anchor=NW, fill=X)
for label, value in choices_persistent:
    Radiobutton(frame_persistent, text=label, variable=choice_pers, value=value, indicatoron=0).pack(side=LEFT, expand=True, fill=X)

window_base.mainloop()