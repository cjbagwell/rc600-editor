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

    def load_from_settings_dict(self, settings):
        self.tracks_frame.load_from_settings_dict(settings)
        self.record_frame.load_from_settings_dict(settings)
        self.play_frame.load_from_settings_dict(settings)
        self.rhythm_frame.load_from_settings_dict(settings)

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

    def load_from_settings_dict(self, settings):
        # Load Track Settings
        # TODO: finish getting the settings from loop tracks implemented
        print('Loading Loop Track Settings from dict')
        for i, track in enumerate(self.track_components):
            curDict = settings['database']['mem'][f'TRACK{i+1}']
            track['REVERSE'].current((curDict['A']))
            track['1SHOT'].current(int(curDict['B']))
            track['PAN'].current(int(curDict['C']))
            track['PLAYLEVEL'].current(int(curDict['D']))
            track['STARTMODE'].current(int(curDict['E']))
            track['STOPMODE'].current(int(curDict['F']))
            track['DUBMODE'].current(int(curDict['G']))
            track['FX'].current(int(curDict['H']))
            track['PLAYMODE'].current(int(curDict['I']))
            track['MEASURE'].current(int(curDict['J']))

            # This is wrong... it appears to show up correctly whenever there is
            # audio for the track.. This is confirmed with Sweet
            # home and johnny b goode
            track['LOOPSYNC'].current(int(curDict['W']))

            # Note I am not sure what the 'x' key is supposed to be,
            # but I think it is related to LOOPSYNC and LOOPSYNCMODE
            track['LOOPSYNCMODE'].current(int(curDict['Y']))# this seems to be right based on sweet home and johnny b goode

            # The ones below have not been confirmed to be correct
            track['TEMPOSYNC'].current(int(curDict['M']))
            track['TEMPOSYNCMODE'].current(int(curDict['N']))
            track['TEMPOSYNCSPEED'].current(int(curDict['O']))
            track['BOUNCEIN'].current(int(curDict['P']))

            # The values below are confirmed to be correct
            new_val = format(int(curDict['Q']), '07b')
            track['MIC1'].current(int(new_val[-1]))
            track['MIC2'].current(int(new_val[-2]))
            track['INST1'].current(int(new_val[-3]))
            track['INST2'].current(int(new_val[-5]))
            track['RHYTHM'].current(int(new_val[-7]))

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

    def load_from_settings_dict(self, settings):
        # TODO: finish implementing this correctly
        d = settings['database']['mem']['REC']
        self.components['RECACTION'].current(int(d['A']))
        self.components['QUANTIZE'].current(int(d['B']))
        self.components['AUTO REC'].current(int(d['C']))
        self.components['AUTO REC SENS'].current(int(d['D']))
        self.components['BOUNCE'].current(int(d['E']))
        # go from decimal to binary for the bounce track settings
        bin_val = bin(int(d['F']))[2:]
        self.components['BOUNCE TRACK 1'].current(int(bin_val[0]))
        self.components['BOUNCE TRACK 2'].current(int(bin_val[1]))
        self.components['BOUNCE TRACK 3'].current(int(bin_val[2]))
        self.components['BOUNCE TRACK 4'].current(int(bin_val[3]))
        self.components['BOUNCE TRACK 5'].current(int(bin_val[4]))
        self.components['BOUNCE TRACK 6'].current(int(bin_val[5]))

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

    def load_from_settings_dict(self, settings):
        d = settings['database']['mem']['PLAY']
        self.components['S.TRK CHANGE'].current(int(d['A']))
        # TODO: this doesn't currently work...
        #   not sure where there setting is located
        # self.components['CURRENT TRACK'].current(int(d['B']))
        self.components['FADE IN TIME'].current(int(d['B']))
        self.components['FADE OUT TIME'].current(int(d['C']))
        all_start = format(int(d['D']), '06b')
        self.components['ALL START TRK1'].current(int(all_start[0]))
        self.components['ALL START TRK2'].current(int(all_start[1]))
        self.components['ALL START TRK3'].current(int(all_start[2]))
        self.components['ALL START TRK4'].current(int(all_start[3]))
        self.components['ALL START TRK5'].current(int(all_start[4]))
        self.components['ALL START TRK6'].current(int(all_start[5]))
        all_stop = format(int(d['E']), '06b')
        self.components['ALL STOP TRK1'].current(int(all_stop[0]))
        self.components['ALL STOP TRK2'].current(int(all_stop[1]))
        self.components['ALL STOP TRK3'].current(int(all_stop[2]))
        self.components['ALL STOP TRK4'].current(int(all_stop[3]))
        self.components['ALL STOP TRK5'].current(int(all_stop[4]))
        self.components['ALL STOP TRK6'].current(int(all_stop[5]))
        # self.components['LOOP LENGTH'].current(int(d['F'])) # check
        self.components['SPEED CHANGE'].current(int(d['G']))
        self.components['SYNC ADJUST'].current(int(d['H']))

        print('Loading Loop Play Settings from dict')


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

        with open('data/beat_genre.json', 'r') as f:
            self.beat_genre_dict = json.load(f)
        with open('data/beat_genre_pattern.json', 'r') as f:
            self.beat_genre_pattern_dict = json.load(f)

        # bind beat combo box to genre and pattern combo boxes
        self.components['BEAT'].bind("<<ComboboxSelected>>", self.update_genre_options)
        self.components['GENRE'].bind("<<ComboboxSelected>>", self.update_pattern_options)
        self.update_genre_options(None) # also calls update_pattern_options

    def update_genre_options(self, event):
        # get the current beat value
        beat_val = self.components['BEAT'].get()
        # get genre options and update genre combo box
        genre_options = self.beat_genre_dict[beat_val]
        cur_genre = self.components['GENRE'].get()
        self.components['GENRE'].config(values=genre_options)
        if cur_genre not in genre_options:
            self.components['GENRE'].current(0)
        self.update_pattern_options(None)

    def update_pattern_options(self, event):
        beat_val = self.components['BEAT'].get()
        cur_genre = self.components['GENRE'].get()
        # get pattern options and update pattern combo box
        pattern_options = self.beat_genre_pattern_dict[f"{beat_val},{cur_genre}"]
        cur_pattern = self.components['PATTERN'].get()
        self.components['PATTERN'].config(values=pattern_options)
        if cur_pattern not in pattern_options:
            self.components['PATTERN'].current(0)

    def load_from_settings_dict(self, settings):
        # TODO: implement this method correctly
        d = settings['database']['mem']['RHYTHM']
        self.components['BEAT'].current(int(d['F']))
        self.update_genre_options(None)
        self.components['GENRE'].current(int(d['A'])) # I suspect that the number always maps to the same value, not dependent on the beat
        self.components['PATTERN'].current(int(d['B']))
        self.components['VARIATION'].current(int(d['C']))
        self.components['KIT'].current(int(d['D']))
        self.components['START_TRIGGER'].current(int(d['G']))
        self.components['STOP_TRIGGER'].current(int(d['H']))
        self.components['INTRO_REC'].current(int(d['I']))
        self.components['INTRO_PLAY'].current(int(d['J']))
        self.components['ENDING'].current(int(d['K']))
        self.components['FILL'].current(int(d['L']))
        self.components['VARIATION_CHANGE'].current(int(d['M']))

        print('Loading Loop Rhythm Settings from dict')




if __name__ == "__main__":
    root = tk.Tk()
    lf = LoopFrame(root)

    import settingsUtil as su
    file = r'exampleData\ROLAND\DATA\MEMORY011A.RC0'
    # file = r"F:\ROLAND\DATA\MEMORY098A.RC0"
    settings_dict = su.read_settings_file(file)
    lf.load_from_settings_dict(settings_dict)
    lf.pack(expand=True, fill="both")
    lf.mainloop()