import tkinter as tk
from tkinter import ttk
import settingsUtil as su

class InfoFrame(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        # self.grid(row=0, column=0, sticky="nsew")
        self.create_widgets()

    def create_widgets(self):
        self.name_label = ttk.Label(self, text="Name")
        self.name_entry = ttk.Entry(self)
        self.tempo_label = ttk.Label(self, text="Tempo")
        self.tempo_spinbox = ttk.Spinbox(self, from_=40, to=300, increment=0.1)
        
        # position them on the grid
        self.name_label.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)
        self.name_entry.grid(row=0, column=1, sticky="nsew", padx=5, pady=5)
        self.tempo_label.grid(row=1, column=0, sticky="nsew", padx=5, pady=5)
        self.tempo_spinbox.grid(row=1, column=1, sticky="nsew", padx=5, pady=5)

        # Add components to class property
        self.components = {}
        self.components['name'] = self.name_entry
        self.components['tempo'] = self.tempo_spinbox

    def load_from_settings_dict(self, settings_dict):
        self.name_entry.delete(0, tk.END)
        self.name_entry.insert(0, su.uni2Str(settings_dict['database']['mem']['NAME']))
        self.tempo_spinbox.delete(0, tk.END)
        tempo = int(settings_dict['database']['mem']['MASTER']['A'])/10
        self.tempo_spinbox.insert(0, tempo)

    def export_as_settings_dict(self, settings_dict):
        # TODO: Implement this method
        settings_dict['database']['mem']['NAME'] = su.str2Uni(self.name_entry.get())
        settings_dict['database']['mem']['MASTER']['A'] = int(float(self.tempo_spinbox.get())*10)
        return settings_dict

if __name__ == "__main__":
    root = tk.Tk()
    frame = InfoFrame(root)
    frame.pack(expand=True, fill="both")
    root.mainloop()