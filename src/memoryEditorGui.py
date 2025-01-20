import tkinter as tk
from tkinter import ttk
import csv
import json

# Create the main window
root = tk.Tk()
root.title("RC600 Editor")

# Create a notebook (tabbed interface)
notebook = ttk.Notebook(root)

# Create frames for each tab
info_frame = ttk.Frame(notebook)
loop_frame = ttk.Frame(notebook)
ctl_func_frame = ttk.Frame(notebook)
assigns_frame = ttk.Frame(notebook)
input_frame = ttk.Frame(notebook)
output_frame = ttk.Frame(notebook)
mixer_frame = ttk.Frame(notebook)
ifx_frame = ttk.Frame(notebook)
tfx_frame = ttk.Frame(notebook)

# Add frames to the notebook
notebook.add(info_frame, text="Info")
notebook.add(loop_frame, text="Loop")
notebook.add(ctl_func_frame, text="Ctl Func")
notebook.add(assigns_frame, text="Assigns")
notebook.add(input_frame, text="Input")
notebook.add(output_frame, text="Output")
notebook.add(mixer_frame, text="Mixer")
notebook.add(ifx_frame, text="iFx")
notebook.add(tfx_frame, text="tFx")

#%% Create the Info Tab 
# Validation functions

def validate_name(P):
    return len(P) <= 12

def validate_tempo(P):
    if P == "":
        return True
    try:
        value = float(P)
        ret = 0 <= value <= 300.0
        if P.find('.') != -1:
            ret = ret and len(P.split('.')[1]) <= 1
        return ret
    except (ValueError, IndexError):
        return False

# Register validation functions
vcmd_name = (root.register(validate_name), '%P')
vcmd_tempo = (root.register(validate_tempo), '%P')

# Add elements to the info tab
ttk.Label(info_frame, text="Name:").grid(
    row=0, column=0, padx=10, pady=10, sticky="w")
name_entry = ttk.Entry(info_frame, validate="key", validatecommand=vcmd_name)
name_entry.grid(row=0, column=1, padx=10, pady=10, sticky="w")

ttk.Label(info_frame, text="Tempo:").grid(
    row=1, column=0, padx=10, pady=10, sticky="w")
tempo_entry = ttk.Entry(info_frame, validate="key", validatecommand=vcmd_tempo)
tempo_entry.grid(row=1, column=1, padx=10, pady=10, sticky="w")
tempo_entry.insert(0, "40.0")  # Set default value to 40.0

#%% Create the Loop Tab
# Create a nested notebook for the loop tab
loop_notebook = ttk.Notebook(loop_frame)

# Create frames for each nested tab
track_frames = [ttk.Frame(loop_notebook) for _ in range(6)]
track_labels = ["Track1", "Track2", "Track3", "Track4", "Track5", "Track6"]

# Add frames to the nested notebook
for i, frame in enumerate(track_frames):
    loop_notebook.add(frame, text=track_labels[i])

# Add elements to each track tab
with open('data/trackOptions.json','r') as f:
    track_options = json.load(f)


track_components = []
for frame in track_frames:
    row = 0
    cur_dict = {}
    for label, values in track_options.items():
        lab = ttk.Label(frame, text=label + ":")
        lab.grid(row=row, column=0, padx=10, pady=5, sticky="w")
        cbx = ttk.Combobox(frame, values=values)
        cbx.grid(row=row, column=1, padx=10, pady=5, sticky="w")
        cbx.insert(0, values[0])
        cur_dict[label] = cbx
        row += 1
    track_components.append(cur_dict)

# Add the record tab with specified labels and dropdowns
with open('data/recordOptions.json','r') as f:
    record_options = json.load(f)

record_frame = ttk.Frame(loop_notebook)

record_components = {}
row = 0
for label, values in record_options.items():
    lbl = ttk.Label(record_frame, text=label + ":")
    lbl.grid(row=row, column=0, padx=10, pady=5, sticky="w")
    cmbx = ttk.Combobox(record_frame, values=values)
    cmbx.grid(row=row, column=1, padx=10, pady=5, sticky="w")
    cmbx.insert(0, values[0])
    row += 1
    record_components[label] = cmbx
loop_notebook.add(record_frame, text="Record")

# Create the play tab with specified labels and dropdowns
play_frame = ttk.Frame(loop_notebook)
with open('data/playOptions.json','r') as f:
    play_options = json.load(f)

play_components = {}
row = 0
for label, values in play_options.items():
    ttk.Label(play_frame, text=label + ":").grid(row=row,
                                                 column=0, padx=10, pady=5, sticky="w")
    cmbx = ttk.Combobox(play_frame, values=values)
    cmbx.grid(row=row, column=1, padx=10, pady=5, sticky="w")
    cmbx.insert(0, values[0])
    play_components[label] = cmbx
    row += 1
loop_notebook.add(play_frame, text="Play")

# Create the callbacks for rhythm tab
with open('data/beatGenreOptions.json','r') as f:
    beat_genre_map = json.load(f)

beatGenre_pattern_map = {
    ('2/4', 'TRAD'): ['TRAIN 2'],
    ('2/4', 'BALLRM'): ['CUMBIA'],
    ('2/4', 'GUIDE'): ['2/4', '2/4 TRIPLE'],
    ('3/4', 'BALLAD'): ['SHUFFLE 2'],
    ('3/4', 'BLUES'): ['3 BEAT'],
    ('3/4', 'BALLRM'): ['WALTZ 1', 'WALTZ 2'],
    ('3/4', 'GUIDE'): ['3/4', '3/4 TRIPLE'],
    ('4/4', 'ACOUSTIC'): ['SIDE STICK', 'BOSSA', 'BRUSH1', 'BRUSH2', 'CONGA 8 BEAT', 'CONGA 16 BEAT', 'CONGA 4 BEAT', 'CONGA SWING', 'CONGA BOSSA', 'CAJON 1', 'CAJON 2'],
    ('4/4', 'BALLAD'): ['SIDE STICK 1', 'SIDE STICK 2', 'SIDE STICK 3', 'SIDE STICK 4', 'SHUFFLE1', '8 BEAT', '16 BEAT 1', '16 BEAT 2', 'SWING'],
    ('4/4', 'BLUES'): ['12 BARS', 'SHUFFLE 1', 'SHUFFLE 2', 'SWING'],
    ('4/4', 'JAZZ'): ['JAZZ BLUES', 'FAST 4 BEAT', 'HARD BOP', 'BRUSH BOP', 'BRUSH SWING', 'FAST SWING', 'MED SWING', 'SLOW LEGATO', 'JAZZ SAMBA'],
    ('4/4', 'FUSION'): ['16 BEAT 1', '16 BEAT 2', '16 BEAT 3', '16 BEAT 4', '16 BEAT 5', '16 BEAT 6', '16 BEAT 7', 'SWING'],
    ('4/4', 'R&B'): ['SWING1', 'SWING2', 'SWING3', 'SIDE STICK 1', 'SIDE STICK 2', 'SIDE STICK 3', 'SHUFFLE 1', 'SHUFFLE 2', '8BEAT 1', '16 BEAT'],
    ('4/4', 'SOUL'): ['SWING1', 'SWING2', 'SWING3', 'SWING4', '16 BEAT1', '16 BEAT2', '16 BEAT3', 'SIDE STICK1', 'SIDE STICK 2', 'MOTOWN', 'PERCUS'],
    ('4/4', 'FUNK'): ['8 BEAT 1', '8 BEAT 2', '8 BEAT 3', '8 BEAT 4', '16 BEAT 1', '16 BEAT 2', '16 BEAT 3', '16 BEAT 4', 'SWING 1', 'SWING 2', 'SWING 3'],
    ('4/4', 'POP'): ['8 BEAT 1', '8 BEAT 2', '16 BEAT 1', '16 BEAT 2', 'PERCUS 1', 'SHUFFLE 1', 'SHUFFLE 2', 'SIDE STICK1', 'SIDE STICK2', 'SWING 1', 'SWING 2'],
    ('4/4', 'SOFT ROCK'): ['16 BEAT 1', '16 BEAT 2', '16 BEAT 3', '16 BEAT 4', '8 BEAT', 'SWING 1', 'SWING 2', 'SWING 3', 'SWING 4', 'SIDE STICK 1', 'SIDE STICK 2', 'PERCUS 1', 'PERCUS 2'],
    ('4/4', 'ROCK'): ['8 BEAT 1', '8 BEAT 2', '8 BEAT 3', '8 BEAT 4', '8 BEAT 5', '8 BEAT 6', '16 BEAT 1', '16 BEAT 2', '16 BEAT 3', '16 BEAT 4', 'SHUFFLE 1', 'SHUFFLE 2', 'SWING 1', 'SWING 2', 'SWING 3', 'SWING 4'],
    ('4/4', 'ALT ROCK'): ['RIDE BEAT', '8 BEAT 1', '8 BEAT 2', '8 BEAT 3', '8 BEAT 4', '16 BEAT 1', '16 BEAT 2', '16 BEAT 3', '16 BEAT 4', 'SWING'],
    ('4/4', 'PUNK'): ['8 BEAT 1', '8 BEAT 2', '8 BEAT 3', '8 BEAT 4', '8 BEAT 5', '8 BEAT 6', '16 BEAT 1', '16 BEAT 2', '16 BEAT 3', 'SIDE STICK', '8 BEAT 6.1'],
    ('4/4', 'HEAVY ROCK'): ['8 BEAT  1', '8 BEAT  2', '8 BEAT  3', '16 BEAT 1', '16 BEAT 2', '16 BEAT 3', 'SHUFFLE 1', 'SHUFFLE 2', 'SWING 1', 'SWING 2', 'SWING 3'],
    ('4/4', 'METAL'): ['8 BEAT 1', '8 BEAT 2', '8 BEAT 3', '8 BEAT 4', '8 BEAT 5', '8 BEAT 6', '2X DB1', '2X DB2', '2X DB3', '2X DB4', '2X DB5'],
    ('4/4', 'TRAD'): ['ROCKN ROLL', 'TRAIN 1', 'COUNTRY 1', 'COUNTRY 2', 'COUNTRY 3', 'FOXTROT', 'TRAD 1', 'TRAD 2'],
    ('4/4', 'WORLD'): ['BOSSA 1', 'BOSSA 2', 'SAMBA 1', 'SAMBA 2', 'BOOGALOO', 'MERENGUE', 'REGGAE', 'LATIN ROCK 1', 'LATIN ROCK 2', 'LATIN PERC', 'SURDO', 'LATIN 1', 'LATIN 2'],
    ('4/4', 'BALLRM'): ['CHACHA', 'BEGUINE', 'RHUMBA', 'TANGO 1', 'TANGO 2', 'JIVE', 'CHARLESTON'],
    ('4/4', 'ELECTRO'): ['ELECTRO 1', 'ELECTRO 2', 'ELECTRO 3', 'ELECTRO 4', 'ELECTRO 5', 'ELECTRO 6', 'ELECTRO 7', 'ELECTRO 8'],
    ('4/4', 'GUIDE'): ['4/4', '4/4 TRIPLE', 'BD 8 BEAT', 'BD 16 BEAT', 'BD SHUFFLE', 'HH 8 BEAT', 'HH 16 BEAT', 'HH SWING 1', 'HH SWING 2', '8 BEAT 1', '8 BEAT 2', '8 BEAT 3', '8 BEAT 4'],
    ('4/4', 'USER'): ['SIMPLE BEAT'],
    ('5/4', 'ALT ROCK'): ['5/4 BEAT'],
    ('5/4', 'ELECTRO'): ['5/4 BEAT'],
    ('5/4', 'GUIDE'): ['5/4', '5/4 TRIPLE'],
    ('6/4', 'GUIDE'): ['6/4', '6/4 TRIPLE'],
    ('7/4', 'GUIDE'): ['7/4', '7/4 TRIPLE'],
    ('5/8', 'GUIDE'): ['5/8'],
    ('6/8', 'BALLAD'): ['6/8 BEAT'],
    ('6/8', 'BLUES'): ['6/8 BEAT'],
    ('6/8', 'JAZZ'): ['6/8 BEAT'],
    ('6/8', 'POP'): ['PERCUS2'],
    ('6/8', 'GUIDE'): ['6/8'],
    ('7/8', 'FUSION'): ['7/8 BEAT'],
    ('7/8', 'R&B'): ['7/8 BEAT'],
    ('7/8', 'GUIDE'): ['7/8'],
    ('8/8', 'GUIDE'): ['8/8'],
    ('9/8', 'GUIDE'): ['9/8'],
    ('10/8', 'GUIDE'): ['10/8'],
    ('11/8', 'GUIDE'): ['11/8'],
    ('12/8', 'GUIDE'): ['12/8'],
    ('13/8', 'GUIDE'): ['13/8'],
    ('14/8', 'GUIDE'): ['14/8'],
    ('15/8', 'GUIDE'): ['15/8'],
}
# TODO: make the above code compatible with json file saving

def genre_change(rhy_comps):
    curVal = (rhy_comps['BEAT'].get(), rhy_comps['GENRE'].get())
    patterns = beatGenre_pattern_map[curVal]
    cur_pattern = rhy_comps['PATTERN'].get()
    rhy_comps['PATTERN'].config(values=patterns)
    if cur_pattern not in patterns:
        rhy_comps['PATTERN'].set(patterns[0])

def beat_change(rhy_comps):
    genres = beat_genre_map[rhy_comps['BEAT'].get()]
    cur_genre = rhy_comps['GENRE'].get()
    rhy_comps['GENRE'].config(values=genres)
    if cur_genre not in genres:
        rhy_comps['GENRE'].set(genres[0])
    genre_change(rhy_comps)

# Create the Rhythm tab with specified labels and dropdowns
rhythm_frame = ttk.Frame(loop_notebook)
with open('data/rhythmOptions.json','r') as f:
    rhythm_options = json.load(f)

rhythm_components = {}
row = 0
for label, values in rhythm_options.items():
    lbl = ttk.Label(rhythm_frame, text=label + ":")
    lbl.grid(row=row, column=0, padx=10, pady=5, sticky="w")
    cmbx = ttk.Combobox(rhythm_frame, values=values)
    cmbx.grid(row=row, column=1, padx=10, pady=5, sticky="w")
    cmbx.insert(0, values[0])
    rhythm_components[label] = cmbx
    row += 1

testVal = ('test1', 'test2', 'test3', 'test4')
# Bind components to change events
rhythm_components["BEAT"].bind(
    "<<ComboboxSelected>>", lambda e: beat_change(rhythm_components))
rhythm_components["GENRE"].bind(
    "<<ComboboxSelected>>", lambda e: genre_change(rhythm_components))
beat_change(rhythm_components) # this calls genre_change as well

loop_notebook.add(rhythm_frame, text="Rhythm")

#%% Create the Ctl Func Tab

# Function to read control functions from CSV
def read_control_functions(csv_file):
    dropdown_options = []
    label_values = {}
    with open(csv_file, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            index = int(row['CtlPedalIndex'])
            name = row['Name']
            push = row['Push']
            hold = row['Hold']
            click = row['Click']
            label_values[name] = (push, hold, click)
            dropdown_options.append(name)
    return dropdown_options, label_values

# Read control functions from CSV
csv_file = 'data/control_functions.csv'
dropdown_options, label_values = read_control_functions(csv_file)

# Function to update labels based on dropdown value
def update_labels(event, labels):
    selected_value = event.widget.get()
    values = label_values[selected_value]
    labels[0].config(text=f"Push: {values[0]}")
    labels[1].config(text=f"Hold: {values[1]}")
    labels[2].config(text=f"Click: {values[2]}")

# Create the table layout
ctlFunComponents = []
for row in range(14):
    if row == 0:
        ttk.Label(ctl_func_frame, text="Button").grid(row=row, column=0, padx=10, pady=5, sticky="w")
        ttk.Label(ctl_func_frame, text="Mode 1").grid(row=row, column=1, padx=10, pady=5, sticky="w")
        ttk.Label(ctl_func_frame, text="Mode 2").grid(row=row, column=2, padx=10, pady=5, sticky="w")
        ttk.Label(ctl_func_frame, text="Mode 3").grid(row=row, column=3, padx=10, pady=5, sticky="w")
    else:
        ttk.Label(ctl_func_frame, text=f"Button {row}").grid(row=row, column=0, padx=10, pady=5, sticky="w")
        for col in range(1, 4):
            frame = ttk.Frame(ctl_func_frame)
            frame.grid(row=row, column=col, padx=10, pady=5, sticky="w")
            cbx = ttk.Combobox(frame, values=dropdown_options)
            cbx.grid(row=0, column=0, columnspan=3, padx=5, pady=5, sticky="w")
            cbx.current(0)
            labels = [
                ttk.Label(frame, text=f"Push: { label_values[cbx.get()][0]}"),
                ttk.Label(frame, text=f"Hold: { label_values[cbx.get()][1]}"),
                ttk.Label(frame, text=f"Click: {label_values[cbx.get()][2]}")
            ]
            for i, lbl in enumerate(labels):
                lbl.grid(row=1, column=i, padx=5, pady=2, sticky="w")
            cbx.bind("<<ComboboxSelected>>", lambda e, labs=labels: update_labels(e, labs))

# Set fixed width for each column
for col in range(1,4):
    ctl_func_frame.grid_columnconfigure(col, minsize=400)

#%% Create the Assigns Tab
# Function to read options from CSV
def read_csv_options(csv_file, colName):
    options = []
    with open(csv_file, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            options.append(row[colName])
    return options

# Read options from CSV files
source_options = read_csv_options('data/Assign_Functions.csv', 'source')
target_options = read_csv_options('data/Assign_Functions.csv', 'source')

# Create the assigns tab with specified layout and functionality
# assigns_frame = ttk.Frame(notebook)
# notebook.add(assigns_frame, text="Assigns")

# Function to validate numeric input
def validate_lo_input(P):
    if P.isdigit():
        return int(P) <= 127 and int(P) >= 0
    return P == ""

# Register the validation function
vcmd = (root.register(validate_lo_input), '%P')

# Function to validate numeric input within a specific range
def validate_numeric_range(P, minval, maxval):
    if P.isdigit() or P == "":
        if P == "":
            return True
        value = int(P)
        return minval <= value <= maxval
    return False

# Function to create a validation command for ACT.LO
def create_vcmd_lo(act_hi_var):
    def vcmd_lo(P):
        try:
            hi = int(act_hi_var.get())
            return validate_numeric_range(P, 0, hi - 1)
        except ValueError:
            return validate_numeric_range(P, 0, 126)
    return vcmd_lo

# Function to create a validation command for ACT.HI
def create_vcmd_hi(act_lo_var):
    def vcmd_hi(P):
        try:
            lo = int(act_lo_var.get())
            return validate_numeric_range(P, lo + 1, 127)
        except ValueError:
            return validate_numeric_range(P, 1, 127)
    return vcmd_hi

# Function to update the range of ACT.HI based on ACT.LO
def update_act_hi_range(act_lo_var, act_hi_spinbox):
    try:
        lo = int(act_lo_var.get())
        act_hi_spinbox.config(from_=lo + 1)
    except ValueError:
        pass

# Function to update the range of ACT.LO based on ACT.HI
def update_act_lo_range(act_hi_var, act_lo_spinbox):
    try:
        hi = int(act_hi_var.get())
        act_lo_spinbox.config(to=hi - 1)
    except ValueError:
        pass

# prepare a list for the 16 assign elements
assign_elements = []
# Create the 4x4 grid layout
for row in range(4):
    for col in range(4):
        frame = ttk.Frame(assigns_frame, borderwidth=2, relief="groove")
        frame.grid(row=row, column=col, padx=10, pady=10, sticky="nsew")

        assign_label = ttk.Label(frame, text=f"Assign {row * 4 + col + 1}")
        assign_label.grid(row=0, column=0, columnspan=1, padx=5, pady=5, sticky="w")

        enable_var = tk.BooleanVar(value=False)
        enable_checkbox = ttk.Checkbutton(frame, text="Enable", variable=enable_var)
        enable_checkbox.grid(row=0, column=1, columnspan=1, padx=5, pady=5, sticky="w")

        min_var = tk.BooleanVar(value=False)
        min_checkbox = ttk.Checkbutton(frame, text="Min", variable=min_var)
        min_checkbox.grid(row=0, column=2, padx=5, pady=5, sticky="w")

        max_var = tk.BooleanVar()
        max_checkbox = ttk.Checkbutton(frame, text="Max", variable=max_var)
        max_checkbox.grid(row=0, column=3, padx=5, pady=5, sticky="w")

        ttk.Label(frame, text="Source:").grid(row=1, column=0, padx=5, pady=5, sticky="w")
        source_combobox = ttk.Combobox(frame, values=source_options)
        source_combobox.grid(row=1, column=1, columnspan=2,padx=5, pady=5, sticky="w")

        ttk.Label(frame, text="Mode:").grid(row=2, column=0, padx=5, pady=5, sticky="w")
        mode_combobox = ttk.Combobox(frame, values=["Moment", "Toggle"])
        mode_combobox.grid(row=2, column=1, columnspan=2, padx=5, pady=5, sticky="w")

        ttk.Label(frame, text="ACT.LO:").grid(row=3, column=0, padx=5, pady=5, sticky="w")
        act_lo_var = tk.StringVar()
        act_hi_var = tk.StringVar()  # Ensure act_hi_var is defined before using it
        vcmd_lo = (root.register(create_vcmd_lo(act_hi_var)), '%P')
        act_lo_spinbox = ttk.Spinbox(frame, from_=0, to=126, textvariable=act_lo_var, validate="key", validatecommand=vcmd_lo)
        act_lo_spinbox.grid(row=3, column=1, columnspan=2, padx=5, pady=5, sticky="w")

        ttk.Label(frame, text="ACT.HI:").grid(row=4, column=0, padx=5, pady=5, sticky="w")
        vcmd_hi = (root.register(create_vcmd_hi(act_lo_var)), '%P')
        act_hi_spinbox = ttk.Spinbox(frame, from_=1, to=127, textvariable=act_hi_var, validate="key", validatecommand=vcmd_hi)
        act_hi_spinbox.grid(row=4, column=1, columnspan=2, padx=5, pady=5, sticky="w")

        ttk.Label(frame, text="Target:").grid(row=5, column=0, padx=5, pady=5, sticky="w")
        target_combobox = ttk.Combobox(frame, values=target_options)
        target_combobox.grid(row=5, column=1, columnspan=2, padx=5, pady=5, sticky="w")

        # Update the range of ACT.HI based on ACT.LO
        act_lo_var.trace_add("write", lambda name, index, mode, lo_var=act_lo_var, hi_spinbox=act_hi_spinbox: update_act_hi_range(lo_var, hi_spinbox))

        # Update the range of ACT.LO based on ACT.HI
        act_hi_var.trace_add("write", lambda name, index, mode, hi_var=act_hi_var, lo_spinbox=act_lo_spinbox: update_act_lo_range(hi_var, lo_spinbox))
        assign_elements.append({
            'enable': enable_var,
            'source': source_combobox,
            'mode': mode_combobox,
            'act_lo': act_lo_var,
            'act_hi': act_hi_var,
            'target': target_combobox,
            'min': min_var,
            'max': max_var
        })

# Pack the nested notebook
loop_notebook.pack(expand=True, fill="both")

# Pack the main notebook
notebook.pack(expand=True, fill="both")

# Run the application
root.mainloop()
