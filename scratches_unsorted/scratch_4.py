from Tkinter import *
from PIL import ImageTk, Image
import tkMessageBox, tkFileDialog
import datetime
import os.path
import re
import string
from tkUtility import tkUtility as tku

marco_filename = ""
filefullpath = ""

class GUI_Radar_IMU_Test(object):
    
    def __init__(self):
        
        self.window_base = Tk()  # Create window
        self.window_base.title("Radar Functional Test: Setup")
        # self.fields_main = TestParameters(self.window_base)
        self.init_fields_main()
        tku.init_statusbar(self.window_base)
        tku.configure_statusbar(self.window_base, "Welcome")
        self.buttons_main = InitButtons(self.window_base)
        self.window_base.mainloop()  # Run continuously

    def init_fields_main(self):
        self.window_base

    """
    Error check fields in Initial Window before Reading Radar Data
    """
    def validate_fields_main():

        global filefullpath
        global self.fields_main
        global self.statusbar_main

        # Check Directory Field
        if not os.path.isdir(self.fields_main.file_entry.get()):
            self.statusbar_main.configure_bar("Invalid Directory | Directory DNE","red")
            return False

        # Convert Test Name to Valid File Name
        filename = self.fields_main.test_entry.get()
        filename = str(filename).strip().replace(' ', '_')
        filename = re.sub(r'(?u)[^-\w.]', '', filename)
        filename.lstrip(string.digits)

        # Check if 'Test Name' Field is Blank
        if filename == "":
            self.statusbar_main.configure_bar("'Test Name' Cannot be Blank","red")
            return False

        filefullpath = self.fields_main.file_entry.get() + "\\" + filename + ".npy"

        # Check if File already Exists
        if os.path.isfile(filefullpath):
            self.statusbar_main.configure_bar("File {} already exists. Update 'Test Name' field.".format(filefullpath),"red")
            return False

        # Check if RCS is valid
        if not self.fields_main.RCS_entry.get().isdigit():
            self.statusbar_main.configure_bar("Invalid RCS {}".format(self.fields_main.RCS_entry.get()),"red")
            return False

        self.statusbar_main.configure_bar("Latest test results saved as: {}".format(filefullpath), "black")
        print("Saving as {}".format(filefullpath))
        return True

    # Initializes listening to port, parsing, saving, and displaying radar data
    def start_radar():

        self.fields_main.rcs = self.fields_main.RCS_entry.get()
        self.fields_main.filefullpath = filefullpath

        self.window_base.destroy()

class TestParameters(object):

    def reflector_renum(self):
        for count, reflector in enumerate(self.reflectors):
            reflector.id = count+1
            reflector.test_label.configure(text="Reflector '{}': '{}'".format(reflector.id, reflector.type))

    def receive_filedirectory(self):
        filedirectory = tkFileDialog.askdirectory(initialdir="/", title="Select Location")
        self.file_entry.delete(0, "end")
        self.file_entry.insert(0, filedirectory)

    def __init__(self, window):

        self.filetypes = [("Numpy Binary", "*.npy")]
        self.reflectors = []
        self.rcs = None
        self.filefullpath = None

        frame1 = Frame(window)
        frame1.pack(side=TOP, anchor=NW)
        self.test_date = Label(frame1, text=datetime.datetime.now().strftime("%A %B %d, %Y")).grid(sticky=NW)

        # Frame containing Saved File Name, AKA Test Name, Widgets
        frame2 = Frame(window)
        frame2.pack(side=TOP, anchor=NW, fill=X)
        test_label = Label(frame2, text="Test Name:")
        test_label.pack(side=LEFT)
        self.test_entry = Entry(frame2)
        self.test_entry.pack(side=LEFT, expand=True, fill=X)

        # Frame containing all reflector related information
        self.frame_targets = Frame(window)
        self.frame_targets.pack(side=TOP, anchor=NW, fill=X)
        self.frame_target_add = Frame(self.frame_targets)
        self.frame_target_add.pack(side=BOTTOM, anchor=SE, fill=X)
        self.file_button = Button(self.frame_target_add, text="+", command=lambda: ReflectorSettingsWindow(Reflector()))
        self.file_button.pack(side=RIGHT)
        self.test_label = Label(self.frame_target_add, text="Add Reflector")
        self.test_label.pack(side=RIGHT)

        # Frame containing RCS Information
        self.frame_RCS = Frame(window)
        self.frame_RCS.pack(side=TOP, anchor=NW, fill=X)
        self.RCS_label = Label(self.frame_RCS, text="Minimum RCS:")
        self.RCS_label.pack(side=LEFT)
        self.RCS_entry = Entry(self.frame_RCS)
        self.RCS_entry.pack(side=LEFT, expand=True, fill=X)

        # Frame containing Saved File Directory Widgets
        self.frame3 = Frame(window)
        self.frame3.pack(side=TOP, anchor=NW, fill=X)
        self.file_label = Label(self.frame3, text="Save Directory:")
        self.file_label.pack(side=LEFT)
        self.file_entry = Entry(self.frame3)
        self.file_entry.pack(side=LEFT, expand=True, fill=X)
        self.file_button = Button(self.frame3, text="...", command=self.receive_filedirectory)
        self.file_button.pack(side=LEFT)

class ReflectorSettingsWindow:

    def statusbar_update(self, message, color):
        self.statusBar.configure(fg=color, text=message)

    def on_close(self):
        if not self.saved:
            tkMessageBox.showinfo("Quit", "Reflector unsaved.")
            self.reflector_window.destroy()
            del self
        else:
            self.reflector_window.destroy()
            del self

    def type_displayoptions(self):

        #Reflector Type 1
        if self.type_variation.get() == "Dihedral Corner Reflector":
            if self.type == "Dihedral Corner Reflector":
                return
            self.type = "Dihedral Corner Reflector"
            if hasattr(self.details, 'frame_params'):
                self.details.frame_params.destroy()
            self.details = ReflectorDihedral(self)
        #Reflector Type 2
        if self.type_variation.get() == "Trihedral Corner Reflector (Triangle)":
            if self.type == "Trihedral Corner Reflector (Triangle)":
                return
            self.type = "Trihedral Corner Reflector (Triangle)"
            if hasattr(self.details, 'frame_params'):
                self.details.frame_params.destroy()
            self.details = ReflectorTrihedralTriangle(self)
        #Reflector Type 3
        if self.type_variation.get() == "Trihedral Corner Reflector (Square)":
            if self.type == "Trihedral Corner Reflector (Square)":
                return
            self.type = "Trihedral Corner Reflector (Square)"
            if hasattr(self.details, 'frame_params'):
                self.details.frame_params.destroy()
            self.details = ReflectorTrihedralSquare(self)
        #Reflector Type 4
        if self.type_variation.get() == "Flat Plate":
            if self.type == "Flat Plate":
                return
            self.type = "Flat Plate"
            if hasattr(self.details, 'frame_params'):
                self.details.frame_params.destroy()
            self.details = ReflectorFlatPlate(self)

    def __init__(self, parent):

        self.edit = False
        if type(parent) is not type(Reflector()):
            self.edit = True

        self.typeList = {
            "Dihedral Corner Reflector",
            "Trihedral Corner Reflector (Triangle)",
            "Trihedral Corner Reflector (Square)",
            "Flat Plate"
        }
        
        global self.fields_main
        global self.statusbar_main
        global self.window_base

        self.saved = False
        self.type = parent.type

        self.reflector_window = Toplevel(self.window_base)
        self.reflector_window.title("Reflector {}".format(len(self.fields_main.reflectors)+1))
        # Select Reflector type
        self.frame1 = Frame(self.reflector_window)
        self.frame1.pack(side=TOP,anchor=NW, fill=X)
        self.type_label = Label(self.frame1, text="Select Reflector Type:")
        self.type_label.pack(side=LEFT)
        self.type_variation = StringVar(self.reflector_window)
        self.type_selection = OptionMenu(self.frame1, self.type_variation, *sorted(self.typeList))
        self.type_selection.pack(side=LEFT)

        self.details = ""

        # Status Bar
        self.statusbar = InitStatusBar(self.reflector_window)

        # Window-related Functions
        self.type_variation.trace("w", lambda q, x, c: self.type_displayoptions())
        self.reflector_window.protocol("WM_DELETE_WINDOW", lambda: self.on_close())

        # If editing existing reflector, pre-set the
        if self.edit:
            self.type_variation.set(parent.type)
            parent.create_frames(self)
            parent.populate_frames()


class Reflector(object):

    def quit(self, window):
        if not self.saved:
            tkMessageBox.showinfo("Quit", "Reflector unsaved.")
            window.destroy()
        else:
            window.destroy()

    def __init__(self):
        self.parameters = {}
        self.id = 0
        self.type = "None"
        self.saved = False


class ReflectorDihedral(Reflector):
	
    global self.fields_main
    global self.statusbar_main

    # to delete existing reflector
    def delete(self):
        self.fields_main.reflectors.pop(self.id-1)
        self.fields_main.reflector_renum()
        self.statusbar_main.configure_bar("Deleted Reflector".format(self.id), "black")
        self.frame_mainmenu.destroy()

    # To edit existing reflector
    def edit(self):
        self.saved = False
        x = ReflectorSettingsWindow(self)
        del x

    # Attempt to save reflector
    def save(self, settings):

        # Error checking reflector parameters
        if not str.isdigit(self.width_entry.get()):
            settings.statusbar.configure_bar("Invalid width entry, non-numerical", "red")
            return
        if float(self.width_entry.get()) <= 0:
            settings.statusbar.configure_bar("Invalid width entry, non-positive", "red")
            return
        if not str.isdigit(self.length_entry.get()):
            settings.statusbar.configure_bar("Invalid length entry, non-numerical", "red")
            return
        if float(self.length_entry.get()) <= 0:
            settings.statusbar.configure_bar("Invalid length entry, non-positive", "red")
            return
        if not str.isdigit(self.posx_entry.get()):
            settings.statusbar.configure_bar("Invalid PosX entry, non-numerical", "red")
            return
        if not str.isdigit(self.posy_entry.get()):
            settings.statusbar.configure_bar("Invalid PosY entry, non-numerical", "red")
            return
        if float(self.posy_entry.get()) <= 0:
            settings.statusbar.configure_bar("Invalid PosY entry, non-positive", "red")
            return

         # Save reflector
        self.parameters["width"] = self.width_entry.get()
        self.parameters["length"] = self.length_entry.get()
        self.parameters["posx"] = self.posx_entry.get()
        self.parameters["posy"] = self.posy_entry.get()
        self.type = "Dihedral Corner Reflector"
        self.saved = True

        # Update main menu with reflector details
        try:
            self.test_label.configure(text="Reflector '{}': '{}'".format(self.id, self.type))
            self.statusbar_main.configure_bar("Edited Reflector {}".format(self.id), "black")
        except:
            print "Created new"
            self.frame_mainmenu = Frame(self.fields_main.frame_targets)
            self.frame_mainmenu.pack(side=TOP, anchor=NW, fill=X)
            self.fields_main.reflectors.append(self)
            self.id = len(self.fields_main.reflectors)
            self.test_label = Label(self.frame_mainmenu, text="Reflector '{}': '{}', RCS= ".format(self.id, self.type))
            self.test_label.pack(side=LEFT)
            # Edit and Delete Buttons
            self.delete_button = Button(self.frame_mainmenu, text="Delete", command=lambda: self.delete())
            self.delete_button.pack(side=RIGHT, anchor=SE)
            self.edit_button = Button(self.frame_mainmenu, text="Edit", command=lambda: self.edit())
            self.edit_button.pack(side=RIGHT, anchor=SE)
            self.statusbar_main.configure_bar("Created new Reflector {}".format(self.id), "black")
        # Close reflector properties window
        settings.reflector_window.destroy()

    # Populate fields in reflector properties window with saved properties
    def populate_frames(self):
        self.width_entry.insert(0, str(self.parameters["width"]))
        self.length_entry.insert(0, str(self.parameters["length"]))
        self.posx_entry.insert(0, str(self.parameters["posx"]))
        self.posy_entry.insert(0, str(self.parameters["posy"]))

    # Generate reflector specific fields in reflector properties window
    def create_frames(self, settings):
        #Outer Frame
        self.frame_params = Frame(settings.reflector_window)
        self.frame_params.pack(side=TOP,anchor=NW, fill=X)
        #ID Frame
        #Width Frame
        self.frame_width = Frame(self.frame_params)
        self.frame_width.pack(side=TOP, anchor=NW, fill=X)
        self.width_label = Label(self.frame_width, text="Width (cm)")
        self.width_label.pack(side=LEFT)
        self.width_entry = Entry(self.frame_width)
        self.width_entry.pack(side=LEFT, expand=True, fill=X)
        #length Frame
        self.frame_length = Frame(self.frame_params)
        self.frame_length.pack(side=TOP, anchor=NW, fill=X)
        self.length_label = Label(self.frame_length, text="Height (cm)")
        self.length_label.pack(side=LEFT)
        self.length_entry = Entry(self.frame_length)
        self.length_entry.pack(side=LEFT, expand=True, fill=X)
        #PosX Frame
        self.frame_posx = Frame(self.frame_params)
        self.frame_posx.pack(side=TOP, anchor=NW, fill=X)
        self.posx_label = Label(self.frame_posx, text="PosX (cm)")
        self.posx_label.pack(side=LEFT)
        self.posx_entry = Entry(self.frame_posx)
        self.posx_entry.pack(side=LEFT, expand=True, fill=X)
        #PosY Frame
        self.frame_posy = Frame(self.frame_params)
        self.frame_posy.pack(side=TOP, anchor=NW, fill=X)
        self.posy_label = Label(self.frame_posy, text="PosY (cm)")
        self.posy_label.pack(side=LEFT)
        self.posy_entry = Entry(self.frame_posy)
        self.posy_entry.pack(side=LEFT, expand=True, fill=X)
        #Photo Reference Frame
        self.frame_photo = Frame(self.frame_params)
        self.frame_photo.pack(side=TOP, anchor=N, fill=X)
        self.img = ImageTk.PhotoImage(Image.open(os.path.join(os.path.dirname(__file__), 'media/DihedralCornerReflector.png')))
        self.img_label = Label(self.frame_photo, image=self.img)
        self.img_label.pack(side=TOP, anchor=N)
        # Save & Quit Buttons
        self.frame_end = Frame(self.frame_params)
        self.frame_end.pack(side=TOP, anchor=N, fill=X)
        self.quit_button = Button(self.frame_end, text="Quit", command=lambda: self.quit(settings.reflector_window))
        self.quit_button.pack(side=RIGHT, anchor=SE)
        self.save_button = Button(self.frame_end, text="Save", command=lambda: self.save(settings))
        self.save_button.pack(side=RIGHT, anchor=SE)

    def __init__(self, settings):
        Reflector.__init__(self)

        self.parameters = {
            "width": 0,
            "length": 0,
            "posx": 0,
            "posy": 0
        }

        self.create_frames(settings)


class ReflectorTrihedralTriangle(Reflector):

    global self.fields_main
    global self.statusbar_main


    # to delete existing reflector
    def delete(self):
        self.fields_main.reflectors.pop(self.id-1)
        self.fields_main.reflector_renum()
        self.statusbar_main.configure_bar("Deleted Reflector".format(self.id), "black")
        self.frame_mainmenu.destroy()

    # To edit existing reflector
    def edit(self):
        self.saved = False
        x = ReflectorSettingsWindow(self)
        del x

    # Attempt to save reflector
    def save(self, settings):

        # Error checking reflector parameters
        if not str.isdigit(self.height_entry.get()):
            settings.statusbar.configure_bar("Invalid height entry, non-numerical", "red")
            return
        if float(self.height_entry.get()) <= 0:
            settings.statusbar.configure_bar("Invalid height entry, non-positive", "red")
            return
        if not str.isdigit(self.posx_entry.get()):
            settings.statusbar.configure_bar("Invalid PosX entry, non-numerical", "red")
            return
        if not str.isdigit(self.posy_entry.get()):
            settings.statusbar.configure_bar("Invalid PosY entry, non-numerical", "red")
            return
        if float(self.posy_entry.get()) <= 0:
            settings.statusbar.configure_bar("Invalid PosY entry, non-positive", "red")
            return

         # Save reflector
        self.parameters["height"] = self.height_entry.get()
        self.parameters["posx"] = self.posx_entry.get()
        self.parameters["posy"] = self.posy_entry.get()
        self.type = "Trihedral Corner Reflector (Triangle)"
        self.saved = True

        # Update main menu with reflector details
        try:
            self.test_label.configure(text="Reflector '{}': '{}'".format(self.id, self.type))
            self.statusbar_main.configure_bar("Edited Reflector {}".format(self.id), "black")
        except:
            print "Created new"
            self.frame_mainmenu = Frame(self.fields_main.frame_targets)
            self.frame_mainmenu.pack(side=TOP, anchor=NW, fill=X)
            self.fields_main.reflectors.append(self)
            self.id = len(self.fields_main.reflectors)
            self.test_label = Label(self.frame_mainmenu, text="Reflector '{}': '{}', RCS= ".format(self.id, self.type))
            self.test_label.pack(side=LEFT)
            # Edit and Delete Buttons
            self.delete_button = Button(self.frame_mainmenu, text="Delete", command=lambda: self.delete())
            self.delete_button.pack(side=RIGHT, anchor=SE)
            self.edit_button = Button(self.frame_mainmenu, text="Edit", command=lambda: self.edit())
            self.edit_button.pack(side=RIGHT, anchor=SE)
            self.statusbar_main.configure_bar("Created new Reflector {}".format(self.id), "black")
        # Close reflector properties window
        settings.reflector_window.destroy()

    # Populate fields in reflector properties window with saved properties
    def populate_frames(self):
        self.height_entry.insert(0, str(self.parameters["height"]))
        self.posx_entry.insert(0, str(self.parameters["posx"]))
        self.posy_entry.insert(0, str(self.parameters["posy"]))

    # Generate reflector specific fields in reflector properties window
    def create_frames(self, settings):
        #Outer Frame
        self.frame_params = Frame(settings.reflector_window)
        self.frame_params.pack(side=TOP,anchor=NW, fill=X)
        #ID Frame
        #Height Frame
        self.frame_height = Frame(self.frame_params)
        self.frame_height.pack(side=TOP, anchor=NW, fill=X)
        self.height_label = Label(self.frame_height, text="Height (cm)")
        self.height_label.pack(side=LEFT)
        self.height_entry = Entry(self.frame_height)
        self.height_entry.pack(side=LEFT, expand=True, fill=X)
        #PosX Frame
        self.frame_posx = Frame(self.frame_params)
        self.frame_posx.pack(side=TOP, anchor=NW, fill=X)
        self.posx_label = Label(self.frame_posx, text="PosX (cm)")
        self.posx_label.pack(side=LEFT)
        self.posx_entry = Entry(self.frame_posx)
        self.posx_entry.pack(side=LEFT, expand=True, fill=X)
        #PosY Frame
        self.frame_posy = Frame(self.frame_params)
        self.frame_posy.pack(side=TOP, anchor=NW, fill=X)
        self.posy_label = Label(self.frame_posy, text="PosY (cm)")
        self.posy_label.pack(side=LEFT)
        self.posy_entry = Entry(self.frame_posy)
        self.posy_entry.pack(side=LEFT, expand=True, fill=X)
        #Photo Reference Frame
        self.frame_photo = Frame(self.frame_params)
        self.frame_photo.pack(side=TOP, anchor=N, fill=X)
        self.img = ImageTk.PhotoImage(Image.open(os.path.join(os.path.dirname(__file__), 'media/TrihedralCornerReflectorTriangle.png')))
        self.img_label = Label(self.frame_photo, image=self.img)
        self.img_label.pack(side=TOP, anchor=N)
        # Save & Quit Buttons
        self.frame_end = Frame(self.frame_params)
        self.frame_end.pack(side=TOP, anchor=N, fill=X)
        self.quit_button = Button(self.frame_end, text="Quit", command=lambda: self.quit(settings.reflector_window))
        self.quit_button.pack(side=RIGHT, anchor=SE)
        self.save_button = Button(self.frame_end, text="Save", command=lambda: self.save(settings))
        self.save_button.pack(side=RIGHT, anchor=SE)

    def __init__(self, settings):
        Reflector.__init__(self)

        self.parameters = {
            "height": 0,
            "posx": 0,
            "posy": 0
        }

        self.create_frames(settings)


class ReflectorTrihedralSquare(Reflector):

    global self.fields_main
    global self.statusbar_main

    # to delete existing reflector
    def delete(self):
        self.fields_main.reflectors.pop(self.id-1)
        self.fields_main.reflector_renum()
        self.statusbar_main.configure_bar("Deleted Reflector".format(self.id), "black")
        self.frame_mainmenu.destroy()

    # To edit existing reflector
    def edit(self):
        self.saved = False
        x = ReflectorSettingsWindow(self)
        del x

    # Attempt to save reflector
    def save(self, settings):

        # Error checking reflector parameters
        if not str.isdigit(self.height_entry.get()):
            settings.statusbar.configure_bar("Invalid height entry, non-numerical", "red")
            return
        if float(self.height_entry.get()) <= 0:
            settings.statusbar.configure_bar("Invalid height entry, non-positive", "red")
            return
        if not str.isdigit(self.posx_entry.get()):
            settings.statusbar.configure_bar("Invalid PosX entry, non-numerical", "red")
            return
        if not str.isdigit(self.posy_entry.get()):
            settings.statusbar.configure_bar("Invalid PosY entry, non-numerical", "red")
            return
        if float(self.posy_entry.get()) <= 0:
            settings.statusbar.configure_bar("Invalid PosY entry, non-positive", "red")
            return

         # Save reflector
        self.parameters["height"] = self.height_entry.get()
        self.parameters["posx"] = self.posx_entry.get()
        self.parameters["posy"] = self.posy_entry.get()
        self.type = "Trihedral Corner Reflector (Square)"
        self.saved = True

        # Update main menu with reflector details
        try:
            self.test_label.configure(text="Reflector '{}': '{}'".format(self.id, self.type))
            self.statusbar_main.configure_bar("Edited Reflector {}".format(self.id), "black")
        except:
            print "Created new"
            self.frame_mainmenu = Frame(self.fields_main.frame_targets)
            self.frame_mainmenu.pack(side=TOP, anchor=NW, fill=X)
            self.fields_main.reflectors.append(self)
            self.id = len(self.fields_main.reflectors)
            self.test_label = Label(self.frame_mainmenu, text="Reflector '{}': '{}', RCS= ".format(self.id, self.type))
            self.test_label.pack(side=LEFT)
            # Edit and Delete Buttons
            self.delete_button = Button(self.frame_mainmenu, text="Delete", command=lambda: self.delete())
            self.delete_button.pack(side=RIGHT, anchor=SE)
            self.edit_button = Button(self.frame_mainmenu, text="Edit", command=lambda: self.edit())
            self.edit_button.pack(side=RIGHT, anchor=SE)
            self.statusbar_main.configure_bar("Created new Reflector {}".format(self.id), "black")
        # Close reflector properties window
        settings.reflector_window.destroy()

    # Populate fields in reflector properties window with saved properties
    def populate_frames(self):
        self.height_entry.insert(0, str(self.parameters["height"]))
        self.posx_entry.insert(0, str(self.parameters["posx"]))
        self.posy_entry.insert(0, str(self.parameters["posy"]))

    # Generate reflector specific fields in reflector properties window
    def create_frames(self, settings):
        #Outer Frame
        self.frame_params = Frame(settings.reflector_window)
        self.frame_params.pack(side=TOP,anchor=NW, fill=X)
        #ID Frame
        #Height Frame
        self.frame_height = Frame(self.frame_params)
        self.frame_height.pack(side=TOP, anchor=NW, fill=X)
        self.height_label = Label(self.frame_height, text="Height (cm)")
        self.height_label.pack(side=LEFT)
        self.height_entry = Entry(self.frame_height)
        self.height_entry.pack(side=LEFT, expand=True, fill=X)
        #PosX Frame
        self.frame_posx = Frame(self.frame_params)
        self.frame_posx.pack(side=TOP, anchor=NW, fill=X)
        self.posx_label = Label(self.frame_posx, text="PosX (cm)")
        self.posx_label.pack(side=LEFT)
        self.posx_entry = Entry(self.frame_posx)
        self.posx_entry.pack(side=LEFT, expand=True, fill=X)
        #PosY Frame
        self.frame_posy = Frame(self.frame_params)
        self.frame_posy.pack(side=TOP, anchor=NW, fill=X)
        self.posy_label = Label(self.frame_posy, text="PosY (cm)")
        self.posy_label.pack(side=LEFT)
        self.posy_entry = Entry(self.frame_posy)
        self.posy_entry.pack(side=LEFT, expand=True, fill=X)
        #Photo Reference Frame
        self.frame_photo = Frame(self.frame_params)
        self.frame_photo.pack(side=TOP, anchor=N, fill=X)
        self.img = ImageTk.PhotoImage(Image.open(os.path.join(os.path.dirname(__file__), 'media/TrihedralCornerReflectorSquare.png')))
        self.img_label = Label(self.frame_photo, image=self.img)
        self.img_label.pack(side=TOP, anchor=N)
        # Save & Quit Buttons
        self.frame_end = Frame(self.frame_params)
        self.frame_end.pack(side=TOP, anchor=N, fill=X)
        self.quit_button = Button(self.frame_end, text="Quit", command=lambda: self.quit(settings.reflector_window))
        self.quit_button.pack(side=RIGHT, anchor=SE)
        self.save_button = Button(self.frame_end, text="Save", command=lambda: self.save(settings))
        self.save_button.pack(side=RIGHT, anchor=SE)

    def __init__(self, settings):
        Reflector.__init__(self)

        self.parameters = {
            "height": 0,
            "posx": 0,
            "posy": 0
        }

        self.create_frames(settings)


class ReflectorFlatPlate(Reflector):

    global self.fields_main
    global self.statusbar_main

    # to delete existing reflector
    def delete(self):
        self.fields_main.reflectors.pop(self.id-1)
        self.fields_main.reflector_renum()
        self.statusbar_main.configure_bar("Deleted Reflector".format(self.id), "black")
        self.frame_mainmenu.destroy()

    # To edit existing reflector
    def edit(self):
        self.saved = False
        x = ReflectorSettingsWindow(self)
        del x

    # Attempt to save reflector
    def save(self, settings):

        # Error checking reflector parameters
        if not str.isdigit(self.width_entry.get()):
            settings.statusbar.configure_bar("Invalid width entry, non-numerical", "red")
            return
        if float(self.width_entry.get()) <= 0:
            settings.statusbar.configure_bar("Invalid width entry, non-positive", "red")
            return
        if not str.isdigit(self.height_entry.get()):
            settings.statusbar.configure_bar("Invalid height entry, non-numerical", "red")
            return
        if float(self.height_entry.get()) <= 0:
            settings.statusbar.configure_bar("Invalid height entry, non-positive", "red")
            return
        if not str.isdigit(self.posx_entry.get()):
            settings.statusbar.configure_bar("Invalid PosX entry, non-numerical", "red")
            return
        if not str.isdigit(self.posy_entry.get()):
            settings.statusbar.configure_bar("Invalid PosY entry, non-numerical", "red")
            return
        if float(self.posy_entry.get()) <= 0:
            settings.statusbar.configure_bar("Invalid PosY entry, non-positive", "red")
            return

         # Save reflector
        self.parameters["width"] = self.width_entry.get()
        self.parameters["height"] = self.height_entry.get()
        self.parameters["posx"] = self.posx_entry.get()
        self.parameters["posy"] = self.posy_entry.get()
        self.type = "Flat Plate"
        self.saved = True

        # Update main menu with reflector details
        try:
            self.test_label.configure(text="Reflector '{}': '{}'".format(self.id, self.type))
            self.statusbar_main.configure_bar("Edited Reflector {}".format(self.id), "black")
        except:
            print "Created new"
            self.frame_mainmenu = Frame(self.fields_main.frame_targets)
            self.frame_mainmenu.pack(side=TOP, anchor=NW, fill=X)
            self.fields_main.reflectors.append(self)
            self.id = len(self.fields_main.reflectors)
            self.test_label = Label(self.frame_mainmenu, text="Reflector '{}': '{}', RCS= ".format(self.id, self.type))
            self.test_label.pack(side=LEFT)
            # Edit and Delete Buttons
            self.delete_button = Button(self.frame_mainmenu, text="Delete", command=lambda: self.delete())
            self.delete_button.pack(side=RIGHT, anchor=SE)
            self.edit_button = Button(self.frame_mainmenu, text="Edit", command=lambda: self.edit())
            self.edit_button.pack(side=RIGHT, anchor=SE)
            self.statusbar_main.configure_bar("Created new Reflector {}".format(self.id), "black")
        # Close reflector properties window
        settings.reflector_window.destroy()

    # Populate fields in reflector properties window with saved properties
    def populate_frames(self):
        self.width_entry.insert(0, str(self.parameters["width"]))
        self.height_entry.insert(0, str(self.parameters["height"]))
        self.posx_entry.insert(0, str(self.parameters["posx"]))
        self.posy_entry.insert(0, str(self.parameters["posy"]))

    # Generate reflector specific fields in reflector properties window
    def create_frames(self, settings):
        #Outer Frame
        self.frame_params = Frame(settings.reflector_window)
        self.frame_params.pack(side=TOP,anchor=NW, fill=X)
        #ID Frame
        #Width Frame
        self.frame_width = Frame(self.frame_params)
        self.frame_width.pack(side=TOP, anchor=NW, fill=X)
        self.width_label = Label(self.frame_width, text="Width (cm)")
        self.width_label.pack(side=LEFT)
        self.width_entry = Entry(self.frame_width)
        self.width_entry.pack(side=LEFT, expand=True, fill=X)
        #Height Frame
        self.frame_height = Frame(self.frame_params)
        self.frame_height.pack(side=TOP, anchor=NW, fill=X)
        self.height_label = Label(self.frame_height, text="Height (cm)")
        self.height_label.pack(side=LEFT)
        self.height_entry = Entry(self.frame_height)
        self.height_entry.pack(side=LEFT, expand=True, fill=X)
        #PosX Frame
        self.frame_posx = Frame(self.frame_params)
        self.frame_posx.pack(side=TOP, anchor=NW, fill=X)
        self.posx_label = Label(self.frame_posx, text="PosX (cm)")
        self.posx_label.pack(side=LEFT)
        self.posx_entry = Entry(self.frame_posx)
        self.posx_entry.pack(side=LEFT, expand=True, fill=X)
        #PosY Frame
        self.frame_posy = Frame(self.frame_params)
        self.frame_posy.pack(side=TOP, anchor=NW, fill=X)
        self.posy_label = Label(self.frame_posy, text="PosY (cm)")
        self.posy_label.pack(side=LEFT)
        self.posy_entry = Entry(self.frame_posy)
        self.posy_entry.pack(side=LEFT, expand=True, fill=X)
        #Photo Reference Frame
        self.frame_photo = Frame(self.frame_params)
        self.frame_photo.pack(side=TOP, anchor=N, fill=X)
        self.img = ImageTk.PhotoImage(Image.open(os.path.join(os.path.dirname(__file__), 'media/FlatPlate.png')))
        self.img_label = Label(self.frame_photo, image=self.img)
        self.img_label.pack(side=TOP, anchor=N)
        # Save & Quit Buttons
        self.frame_end = Frame(self.frame_params)
        self.frame_end.pack(side=TOP, anchor=N, fill=X)
        self.quit_button = Button(self.frame_end, text="Quit", command=lambda: self.quit(settings.reflector_window))
        self.quit_button.pack(side=RIGHT, anchor=SE)
        self.save_button = Button(self.frame_end, text="Save", command=lambda: self.save(settings))
        self.save_button.pack(side=RIGHT, anchor=SE)

    def __init__(self, settings):
        Reflector.__init__(self)

        self.parameters = {
            "width": 0,
            "height": 0,
            "posx": 0,
            "posy": 0
        }

        self.create_frames(settings)


class InitButtons:

    def __init__(self, window):

        bottom_frame = Frame(window)
        bottom_frame.pack(side=BOTTOM, anchor=SE, fill=X)

        self.quit_button = Button(bottom_frame, text="Quit", command=lambda: exit())
        self.quit_button.pack(side=RIGHT, anchor=SE)
        self.enter_button = Button(bottom_frame, text="Enter", command=lambda: start_radar() if validate_fields_main() else None)
        self.enter_button.pack(side=RIGHT, anchor=SE)





def RUN_GUI():

    gui = GUI_Radar_IMU_Test()



if __name__ == "__main__":

    RUN_GUI()

