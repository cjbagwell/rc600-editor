import json
import tkinter as tk
import tkinter.ttk as ttk


class LoopFrame(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        # self.grid(row=0, column=0, sticky="nsew")
        self.notebook = ttk.Notebook(self)
        self.create_widgets()
        self.add_frames_to_notebook()
        self.notebook.pack(expand=True, fill="both")

    def create_widgets(self):
        self.tracks_frame = LoopTracksFrame(self.parent)
        self.record_frame = LoopRecordFrame(self.parent)
        self.play_frame = LoopPlayFrame(self.parent)
        self.rhythm_frame = LoopRhythmFrame(self.parent)

    def add_frames_to_notebook(self):
        # Add frames to notebook
        self.notebook.add(self.tracks_frame, text="Tracks")
        self.notebook.add(self.record_frame, text="Record")
        self.notebook.add(self.play_frame, text="Play")
        self.notebook.add(self.rhythm_frame, text="Rhythm")
        # Set grid locations
        self.notebook.grid(row=0, column=0, sticky="nsew")

class LoopTracksFrame(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.grid(row=0, column=0, sticky="nsew")
        self.create_widgets()

    def create_widgets(self):
        with open('data/trackOptions.json', 'r') as file:
            track_options = json.load(file)
        # Create 7 labels, 1 for the setting and 6 for the tracks
        for i in range(0, 7):
            if i == 0:
                setting_label = ttk.Label(self, text="Setting")
                setting_label.grid(row=0, column=0)
            else:
                track_label = ttk.Label(self, text=f"Track {i}")
                track_label.grid(row=0, column=i)
        # Create rows for each of the settings
        self.track_components = []
        for track_num in range(0, 6):
            row = 1
            cur_dict = {}
            for label, values in track_options.items():
                if track_num == 0:
                    lab = ttk.Label(self, text=label + ":")
                    lab.grid(row=row, column=0, padx=10, pady=5, sticky="w")
                cbx = ttk.Combobox(self, values=values, state="readonly")
                cbx.grid(row=row, column=track_num+1,
                         padx=10, pady=5, sticky="w")
                cbx.current(0)
                cur_dict[label] = cbx
                row += 1
            self.track_components.append(cur_dict)

class LoopRecordFrame(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.grid(row=0, column=0, sticky="nsew")
        self.create_widgets()

    def create_widgets(self):
        # Add the record tab with specified labels and dropdowns
        with open('data/recordOptions.json','r') as f:
            record_options = json.load(f)
        self.components = {}
        row = 0
        for label, values in record_options.items():
            lbl = ttk.Label(self, text=label + ":")
            lbl.grid(row=row, column=0, padx=10, pady=5, sticky="w")
            cmbx = ttk.Combobox(self, values=values, state="readonly")
            cmbx.grid(row=row, column=1, padx=10, pady=5, sticky="w")
            cmbx.current(0)
            row += 1
            self.components[label] = cmbx

class LoopPlayFrame(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.grid(row=0, column=0, sticky="nsew")
        self.create_widgets()
    
    def create_widgets(self):
        with open('data/playOptions.json', 'r') as f:
            play_options = json.load(f)
        self.components = {}
        row = 0
        for label, values in play_options.items():
            lbl = ttk.Label(self, text=label + ":")
            lbl.grid(row=row, column=0, padx=10, pady=5, sticky="w")
            cmbx = ttk.Combobox(self, values=values, state="readonly")
            cmbx.grid(row=row, column=1, padx=10, pady=5, sticky="w")
            cmbx.current(0)
            self.components[label] = cmbx
            row += 1
        
class LoopRhythmFrame(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.grid(row=0, column=0, sticky="nsew")
        self.create_widgets()
    
    def create_widgets(self):
        with open('data/rhythmOptions.json', 'r') as f:
            rhythm_options = json.load(f)
        self.components = {}
        row = 0
        for label, values in rhythm_options.items():
            lbl = ttk.Label(self, text=label + ":")
            lbl.grid(row=row, column=0, padx=10, pady=5, sticky="w")
            cmbx = ttk.Combobox(self, values=values, state="readonly")
            cmbx.grid(row=row, column=1, padx=10, pady=5, sticky="w")
            cmbx.current(0)
            self.components[label] = cmbx
            row += 1

