import csv
import tkinter as tk
from tkinter import ttk


class ControlFunctionFrame(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.grid(row=0, column=0, sticky="nsew")
        self.create_widgets()

    def read_control_functions(self):
        csv_file = 'data/controlFunctions.csv'
        dropdown_options = []
        labels_dict = {}
        with open(csv_file, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                index = int(row['CtlPedalIndex'])
                name = row['Name']
                push = row['Push']
                hold = row['Hold']
                click = row['Click']
                labels_dict[name] = (push, hold, click)
                dropdown_options.append(name)
        return dropdown_options, labels_dict

    def update_labels(self, event, labels, labels_dict):
        selected_value = event.widget.get()
        values = labels_dict[selected_value]
        labels[0].config(text=f"Push: {values[0]}")
        labels[1].config(text=f"Hold: {values[1]}")
        labels[2].config(text=f"Click: {values[2]}")
    
    def create_widgets(self):
        dropdown_options, labels_dict = self.read_control_functions()
        ctlFunComponents = []
        for row in range(14):
            if row == 0:
                l1 = ttk.Label(self, text="Button")
                l2 = ttk.Label(self, text="Mode 1")
                l3 = ttk.Label(self, text="Mode 2")
                l4 = ttk.Label(self, text="Mode 3")
                l1.grid(row=row, column=0, padx=10, pady=5, sticky="w")
                l2.grid(row=row, column=1, padx=10, pady=5, sticky="w")
                l3.grid(row=row, column=2, padx=10, pady=5, sticky="w")
                l4.grid(row=row, column=3, padx=10, pady=5, sticky="w")
            else:
                ttk.Label(self, text=f"Button {row}").grid(
                    row=row, column=0, padx=10, pady=5, sticky="w")
                for col in range(1, 4):
                    frame = ttk.Frame(self)
                    frame.grid(row=row, column=col,padx=10,pady=5,sticky="w")
                    cbx = ttk.Combobox(frame, values=dropdown_options)
                    cbx.grid(row=0, column=0, columnspan=3,padx=5,pady=5,sticky="w")
                    cbx.current(0)
                    labels = [
                        ttk.Label(frame, text=f"Push: {labels_dict[cbx.get()][0]}"),
                        ttk.Label(frame, text=f"Hold: {labels_dict[cbx.get()][1]}"),
                        ttk.Label(frame, text=f"Click: {labels_dict[cbx.get()][2]}")
                    ]
                    for i, lbl in enumerate(labels):
                        lbl.grid(row=1, column=i, padx=5, pady=2, sticky="w")
                    cbx.bind("<<ComboboxSelected>>", lambda e,
                             labs=labels: self.update_labels(e, labs, labels_dict))
        # Set fixed width for each column
        for col in range(1, 4):
            self.grid_columnconfigure(col, minsize=400)
