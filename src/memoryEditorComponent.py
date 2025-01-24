import tkinter as tk
from tkinter import ttk
from InfoFrame import InfoFrame
from LoopFrame import LoopFrame
from AssignsFrame import AssignsFrame
from ControlFunctionsFrame import ControlFunctionFrame
import settingsUtil as su
import json


class MemoryEditorComponent(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        # self.grid(row=0, column=0, sticky="nsew")
        self.notebook = ttk.Notebook(parent)
        self.create_frames()
        self.add_frames_to_notebook()
        self.notebook.pack(expand=True, fill="both")

    def create_frames(self):
        self.info_frame = InfoFrame(self.notebook)
        self.loop_frame = LoopFrame(self.notebook)
        self.ctl_func_frame = ControlFunctionFrame(self.notebook)
        self.assigns_frame = AssignsFrame(self.notebook)
        # self.input_frame = ttk.Frame(self.notebook)
        # self.output_frame = ttk.Frame(self.notebook)
        # self.mixer_frame = ttk.Frame(self.notebook)
        # self.ifx_frame = ttk.Frame(self.notebook)
        # self.tfx_frame = ttk.Frame(self.notebook)

    def add_frames_to_notebook(self):
        # Add frames to notebook
        self.notebook.add(self.info_frame, text="Info")
        self.notebook.add(self.loop_frame, text="Loop")
        self.notebook.add(self.ctl_func_frame, text="Control Functions")
        self.notebook.add(self.assigns_frame, text="Assigns")
        # self.notebook.add(self.input_frame, text="Input")
        # self.notebook.add(self.output_frame, text="Output")
        # self.notebook.add(self.mixer_frame, text="Mixer")
        # self.notebook.add(self.ifx_frame, text="IFX")
        # self.notebook.add(self.tfx_frame, text="TFX")
        # Set grid locations

    def load_settings_file(self, file):
        settings_dict = su.read_settings_file(file)
        self.info_frame.load_from_settings_dict(settings_dict)
        self.loop_frame.load_from_settings_dict(settings_dict)
        # self.ctl_func_frame.load_from_settings_dict(settings_dict)
        self.assigns_frame.load_from_settings_dict(settings_dict)
        # mem_dict = settings_dict['database']['mem']
        # print(settings_dict)

    def export_as_settings_file(self, file):
        print("Exporting as settings file not implemented yet")

root = tk.Tk()
root.title("Memory Editor")
tmp = MemoryEditorComponent(root)


file_base = r'exampleData\ROLAND\DATA\MEMORY062'# Sweethome
# file_base = r'exampleData\ROLAND\DATA\MEMORY066'# Johnny B Goode


tmp.notebook.pack(expand=True, fill="both")
tmp.load_settings_file(file_base + 'A.RC0')
tmp.mainloop()
# root = tk.Tk()
# root.title("Memory Editor")
# tmp = MemoryEditorComponent(root)
# tmp.load_settings_file(file_base + 'B.RC0')
# tmp.mainloop()