import tkinter as tk
from tkinter import ttk
import csv
import numpy as np


def read_csv_options(csv_file, colName):
    options = []
    with open(csv_file, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            options.append(row[colName])
    return options


class AssignsFrame(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        # self.grid(row=0, column=0, sticky="nsew")
        self.create_widgets()

    def read_target_options(self):
        csv_file = 'data/AssignTargets.csv'
        targets = []
        minMaxOptions = []
        with open(csv_file, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                targets.append(row['target'])
                cur_opts = row['minMaxOptions'].strip()
                if cur_opts.find(',') != -1:
                    cur_opts = cur_opts.split(',')
                elif cur_opts.find(':') != -1:
                    parts = cur_opts.split(':')
                    if len(parts) == 3:
                        start, step, end = map(float, parts)
                        cur_opts = list(map(str, np.arange(start, end + step, step)))
                    else:
                        raise ValueError("Invalid range string format")
                minMaxOptions.append(cur_opts)

        return targets, minMaxOptions



    def create_widgets(self):
        # Read options from CSV files
        source_options = read_csv_options('data/AssignSources.csv', 'source')
        target_options, minMaxOptions = self.read_target_options()
        mode_options = ['Moment', 'Toggle']

        # Create validation commands for the ACT.LO and ACT.HI spinboxes
        def validate_numeric_range(P, minval, maxval):
            if P.isdigit() or P == "":
                if P == "":
                    return True
                value = int(P)
                return minval <= value <= maxval
            return False
        def create_vcmd_lo(act_hi_var):
            def vcmd_lo(P):
                try:
                    hi = int(act_hi_var.get())
                    return validate_numeric_range(P, 0, hi - 1)
                except ValueError:
                    return validate_numeric_range(P, 0, 126)
            return vcmd_lo
        def create_vcmd_hi(act_lo_var):
            def vcmd_hi(P):
                try:
                    lo = int(act_lo_var.get())
                    return validate_numeric_range(P, lo + 1, 127)
                except ValueError:
                    return validate_numeric_range(P, 1, 127)
            return vcmd_hi
        def update_act_hi_range(lo_var, hi_spinbox):
            lo_val = int(lo_var.get())
            hi_spinbox.config(from_=max(1, lo_val), to=127)
        def update_act_lo_range(hi_var, lo_spinbox):
            hi_val = int(hi_var.get())
            lo_spinbox.config(from_=0, to=min(126, hi_val))

        # Create a function to update the min and max comboboxes based on the target combobox
        def update_min_max(event, min_cmbx, max_cmbx):
            target = event.widget.get()
            idx = target_options.index(target)
            current_min = min_cmbx.get()
            current_max = max_cmbx.get()
            min_cmbx.config(values=minMaxOptions[idx])
            max_cmbx.config(values=minMaxOptions[idx])
            if current_min not in minMaxOptions[idx]:
                min_cmbx.set(minMaxOptions[idx][0])
            if current_max not in minMaxOptions[idx]:
                max_cmbx.set(minMaxOptions[idx][-1])

        # prepare a list for the 16 assign elements
        self.components = []
        # Create the 4x4 grid layout
        for row in range(4):
            for col in range(4):
                # Create a frame for each assign
                frame = ttk.Frame(self, borderwidth=2, relief="groove")
                frame.grid(row=row, column=col, padx=10, pady=10, sticky="nsew")

                # Create the variables behind each component
                enable_var = tk.BooleanVar(value=False)
                act_lo_var = tk.StringVar()
                act_hi_var = tk.StringVar()
                min_var = tk.StringVar(value=minMaxOptions[0][0])
                max_var = tk.StringVar(value=minMaxOptions[0][-1])
                mode_var = tk.StringVar(value="Moment")
                target_var = tk.StringVar(value=target_options[0])
                source_var = tk.StringVar(value=source_options[0])

                # Create the validation commands for the ACT.LO and ACT.HI spinboxes
                vcmd_lo = (self.register(create_vcmd_lo(act_hi_var)), '%P')
                vcmd_hi = (self.register(create_vcmd_hi(act_lo_var)), '%P')

                # Create the labels
                assign_label = ttk.Label(frame, text=f"Assign {row * 4 + col + 1}", font=("bold"))
                src_label = ttk.Label(frame, text="Source:")
                mode_label = ttk.Label(frame, text="Mode:")
                act_lo_label = ttk.Label(frame, text="ACT.LO:")
                act_hi_label = ttk.Label(frame, text="ACT.HI:")
                target_label = ttk.Label(frame, text="Target:")
                min_label = ttk.Label(frame, text="Min:")
                max_label = ttk.Label(frame, text="Max:")

                # Create the components
                enable_checkbox = ttk.Checkbutton(frame, text="Enable", variable=enable_var)
                min_combobox = ttk.Combobox(frame, textvariable=min_var, values=minMaxOptions[0], state="readonly")
                max_combobox = ttk.Combobox(frame, textvariable=max_var, values=minMaxOptions[0], state="readonly")
                source_combobox = ttk.Combobox(frame, textvariable=source_var, values=source_options, state="readonly")
                target_combobox = ttk.Combobox(frame, textvariable=target_var, values=target_options, state="readonly")
                mode_combobox = ttk.Combobox(frame, textvariable=mode_var, values=mode_options, state="readonly")
                act_lo_spinbox = ttk.Spinbox(frame, from_=0, to=126, textvariable=act_lo_var, validate="key", validatecommand=vcmd_lo)
                act_hi_spinbox = ttk.Spinbox(frame, from_=1, to=127, textvariable=act_hi_var, validate="key", validatecommand=vcmd_hi)

                # Bind the min and max comboboxes to the minMaxOptions list
                target_combobox.bind("<<ComboboxSelected>>", lambda event, min_cmbx=min_combobox, max_cmbx=max_combobox: update_min_max(event, min_cmbx, max_cmbx))
                target_var.set(target_options[0])
                target_combobox.event_generate("<<ComboboxSelected>>")

                # Set the default values
                source_combobox.set(source_options[0])
                mode_combobox.set(mode_options[0])
                min_var.set(minMaxOptions[0][0])
                max_var.set(minMaxOptions[0][-1])
                act_lo_var.set("0")
                act_hi_var.set("127")

                # Create the trace commands
                act_lo_var.trace_add("write", lambda name, index, mode, lo_var=act_lo_var, hi_spinbox=act_hi_spinbox: update_act_hi_range(lo_var, hi_spinbox))
                act_hi_var.trace_add("write", lambda name, index, mode, hi_var=act_hi_var, lo_spinbox=act_lo_spinbox: update_act_lo_range(hi_var, lo_spinbox))

                # Place the labels and components in the grid
                assign_label.grid(   row=0, column=0, columnspan=1, padx=5, pady=5, sticky="w")
                enable_checkbox.grid(row=0, column=1, columnspan=1, padx=5, pady=5, sticky="w")
                src_label.grid(      row=1, column=0, columnspan=1, padx=5, pady=5, sticky="w")
                source_combobox.grid(row=1, column=1, columnspan=2, padx=5, pady=5, sticky="w")
                mode_label.grid(     row=1, column=2, columnspan=1, padx=5, pady=5, sticky="w")
                mode_combobox.grid(  row=1, column=3, columnspan=2, padx=5, pady=5, sticky="w")
                act_lo_label.grid(   row=2, column=0, columnspan=1, padx=5, pady=5, sticky="w")
                act_lo_spinbox.grid( row=2, column=1, columnspan=1, padx=5, pady=5, sticky="w")
                act_hi_label.grid(   row=2, column=2, columnspan=1, padx=5, pady=5, sticky="w")
                act_hi_spinbox.grid( row=2, column=3, columnspan=1, padx=5, pady=5, sticky="w")
                target_label.grid(   row=3, column=0, columnspan=1, padx=5, pady=5, sticky="w")
                target_combobox.grid(row=3, column=1, columnspan=2, padx=5, pady=5, sticky="w")
                min_label.grid(      row=4, column=0, columnspan=1, padx=5, pady=5, sticky="w")
                min_combobox.grid(   row=4, column=1, columnspan=2, padx=5, pady=5, sticky="w")
                max_label.grid(      row=4, column=2, columnspan=1, padx=5, pady=5, sticky="w")
                max_combobox.grid(   row=4, column=3, columnspan=2, padx=5, pady=5, sticky="w")

                self.components.append({
                    'enable': enable_var,
                    'source': source_var,
                    'mode': mode_var,
                    'act_lo': act_lo_var,
                    'act_hi': act_hi_var,
                    'target': target_var,
                    'min': min_var,
                    'max': max_var
                })

# root = tk.Tk()
# root.title("Assigns")
# AssignsFrame(root).pack(fill="both", expand=True)
# root.mainloop()