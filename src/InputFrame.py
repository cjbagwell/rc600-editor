import tkinter as tk
from tkinter import ttk
import json

class InputFrame(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.create_widgets()
    
    def create_widgets(self):
        # Create Microphone columns
        self.microphone_elements = []
        for i in range(2):
            subframe = ttk.Frame(self)
            subframe.grid(row=0, column=i, sticky="nsew", padx=5, pady=5)
            # Create Labels
            mic_label = ttk.Label(subframe, text=f"Microphone {i+1}")
            phantomLabel = ttk.Label(subframe, text="Phantom Power")
            eqSwitchLabel = ttk.Label(subframe, text="EQ Enabled")
            loGainLabel = ttk.Label(subframe, text="Low Gain")
            hiGainLabel = ttk.Label(subframe, text="High Gain")
            loMidFreqLabel = ttk.Label(subframe, text="Low Mid Frequency")
            loMidGainLabel = ttk.Label(subframe, text="Low Mid Gain")
            hiMidGainLabel = ttk.Label(subframe, text="High Mid Gain")
            hiMidFreqLabel = ttk.Label(subframe, text="High Mid Frequency")
            loCutlabel = ttk.Label(subframe, text="Low Cut")
            hiCutLabel = ttk.Label(subframe, text="High Cut")
            levelLabel = ttk.Label(subframe, text="Level")
            compressionLabel = ttk.Label(subframe, text="Compression")
            noiseSuppressionLabel = ttk.Label(subframe, text="Noise Suppression")

            # Create Elements
            phantomPower = ttk.Checkbutton(subframe)
            eqSwitch = ttk.Checkbutton(subframe)
            loGain = ttk.Spinbox(subframe, from_=0, to=41, increment=1)#TODO: verify the range
            hiGain = ttk.Spinbox(subframe, from_=0, to=41, increment=1)
            loMidFreq = ttk.Spinbox(subframe, from_=0, to=41, increment=1)
            loMidGain = ttk.Spinbox(subframe, from_=0, to=41, increment=1)
            hiMidFreq = ttk.Spinbox(subframe, from_=0, to=41, increment=1)
            hiMidGain = ttk.Spinbox(subframe, from_=0, to=41, increment=1)
            level = ttk.Spinbox(subframe, from_=0, to=41, increment=1)
            loCut = ttk.Spinbox(subframe, from_=0, to=100, increment=1) #TODO: verify the range
            hiCut = ttk.Spinbox(subframe, from_=0, to=100, increment=1) #TODO: verify the range
            compression = ttk.Spinbox(subframe, from_=0, to=100, increment=1) #TODO: verify the range
            noiseSuppression = ttk.Spinbox(subframe, from_=0, to=100, increment=1) #TODO: verify the range

            # Position labels
            mic_label.grid(      row=0, column=i, columnspan=2, sticky="nsew", padx=5, pady=5)
            phantomLabel.grid(   row=1, column=i, sticky="nsew", padx=5, pady=5)
            eqSwitchLabel.grid(  row=2, column=i, sticky="nsew", padx=5, pady=5)
            loGainLabel.grid(    row=3, column=i, sticky="nsew", padx=5, pady=5)
            hiGainLabel.grid(    row=4, column=i, sticky="nsew", padx=5, pady=5)
            loMidFreqLabel.grid( row=5, column=i, sticky="nsew", padx=5, pady=5)
            loMidGainLabel.grid( row=6, column=i, sticky="nsew", padx=5, pady=5)
            hiMidFreqLabel.grid( row=7, column=i, sticky="nsew", padx=5, pady=5)
            hiMidGainLabel.grid( row=8, column=i, sticky="nsew", padx=5, pady=5)
            levelLabel.grid(     row=9, column=i, sticky="nsew", padx=5, pady=5)
            loCutlabel.grid(     row=10, column=i, sticky="nsew", padx=5, pady=5)
            hiCutLabel.grid(     row=11, column=i, sticky="nsew", padx=5, pady=5)
            compressionLabel.grid(row=12, column=i, sticky="nsew", padx=5, pady=5)
            noiseSuppressionLabel.grid(row=13, column=i, sticky="nsew", padx=5, pady=5)

            # Position elements
            phantomPower.grid(row=1, column=i+1, sticky="nsew", padx=5, pady=5)
            eqSwitch.grid(    row=2, column=i+1, sticky="nsew", padx=5, pady=5)
            loGain.grid(      row=3, column=i+1, sticky="nsew", padx=5, pady=5)
            hiGain.grid(      row=4, column=i+1, sticky="nsew", padx=5, pady=5)
            loMidFreq.grid(   row=5, column=i+1, sticky="nsew", padx=5, pady=5)
            loMidGain.grid(   row=6, column=i+1, sticky="nsew", padx=5, pady=5)
            hiMidFreq.grid(   row=7, column=i+1, sticky="nsew", padx=5, pady=5)
            hiMidGain.grid(   row=8, column=i+1, sticky="nsew", padx=5, pady=5)
            level.grid(       row=9, column=i+1, sticky="nsew", padx=5, pady=5)
            loCut.grid(       row=10, column=i+1, sticky="nsew", padx=5, pady=5)
            hiCut.grid(       row=11, column=i+1, sticky="nsew", padx=5, pady=5)
            compression.grid( row=12, column=i+1, sticky="nsew", padx=5, pady=5)
            noiseSuppression.grid( row=13, column=i+1, sticky="nsew", padx=5, pady=5)

            # Add elements to list
            self.microphone_elements.append({
                'phantomPower': phantomPower,
                'eqSwitch': eqSwitch,
                'loGain': loGain,
                'hiGain': hiGain,
                'loMidFreq': loMidFreq,
                'loMidGain': loMidGain,
                'hiMidFreq': hiMidFreq,
                'hiMidGain': hiMidGain,
                'level': level,
                'loCut': loCut,
                'hiCut': hiCut,
                'compression': compression,
                'noiseSuppression': noiseSuppression
            })
        
        # Create Instrument columns
        self.instrument_elements = []
        for i in range(2):
            subframe = ttk.Frame(self)
            subframe.grid(row=0, column=i+2, sticky="nsew", padx=5, pady=5)
            # Create Labels
            instrument_label = ttk.Label(subframe, text=f"Instrument {i+1}")
            gainLabel = ttk.Label(subframe, text="Gain")
            eqSwitchLabel = ttk.Label(subframe, text="EQ Enabled")
            loGainLabel = ttk.Label(subframe, text="Low Gain")
            hiGainLabel = ttk.Label(subframe, text="High Gain")
            loMidFreqLabel = ttk.Label(subframe, text="Low Mid Frequency")
            loMidGainLabel = ttk.Label(subframe, text="Low Mid Gain")
            hiMidGainLabel = ttk.Label(subframe, text="High Mid Gain")
            hiMidFreqLabel = ttk.Label(subframe, text="High Mid Frequency")
            loCutlabel = ttk.Label(subframe, text="Low Cut")
            hiCutLabel = ttk.Label(subframe, text="High Cut")
            levelLabel = ttk.Label(subframe, text="Level")
            compressionLabel = ttk.Label(subframe, text="Compression")
            noiseSuppressionLabel = ttk.Label(subframe, text="Noise Suppression")

            # Create Elements
            eqSwitch = ttk.Checkbutton(subframe)
            gain = ttk.Combobox(subframe, values=["instrument", "line"])
            loGain = ttk.Spinbox(subframe, from_=0, to=41, increment=1)
            hiGain = ttk.Spinbox(subframe, from_=0, to=41, increment=1)
            loMidFreq = ttk.Spinbox(subframe, from_=0, to=41, increment=1)
            loMidGain = ttk.Spinbox(subframe, from_=0, to=41, increment=1)
            hiMidFreq = ttk.Spinbox(subframe, from_=0, to=41, increment=1)
            hiMidGain = ttk.Spinbox(subframe, from_=0, to=41, increment=1)
            level = ttk.Spinbox(subframe, from_=0, to=41, increment=1)
            loCut = ttk.Spinbox(subframe, from_=0, to=100, increment=1)
            hiCut = ttk.Spinbox(subframe, from_=0, to=100, increment=1)
            compression = ttk.Spinbox(subframe, from_=0, to=100, increment=1)
            noiseSuppression = ttk.Spinbox(subframe, from_=0, to=100, increment=1)

            # Position labels
            instrument_label.grid( row=0, column=0, columnspan=2, sticky="nsew", padx=5, pady=5)
            eqSwitchLabel.grid(    row=1, column=0, sticky="nsew", padx=5, pady=5)
            gainLabel.grid(        row=2, column=0, sticky="nsew", padx=5, pady=5)
            loGainLabel.grid(      row=3, column=0, sticky="nsew", padx=5, pady=5)
            hiGainLabel.grid(      row=4, column=0, sticky="nsew", padx=5, pady=5)
            loMidFreqLabel.grid(   row=5, column=0, sticky="nsew", padx=5, pady=5)
            loMidGainLabel.grid(   row=6, column=0, sticky="nsew", padx=5, pady=5)
            hiMidFreqLabel.grid(   row=7, column=0, sticky="nsew", padx=5, pady=5)
            hiMidGainLabel.grid(   row=8, column=0, sticky="nsew", padx=5, pady=5)
            levelLabel.grid(       row=9, column=0, sticky="nsew", padx=5, pady=5)
            loCutlabel.grid(       row=10, column=0, sticky="nsew", padx=5, pady=5)
            hiCutLabel.grid(       row=11, column=0, sticky="nsew", padx=5, pady=5)
            compressionLabel.grid( row=12, column=0, sticky="nsew", padx=5, pady=5)
            noiseSuppressionLabel.grid(row=13, column=0, sticky="nsew", padx=5, pady=5)

            # Position elements
            eqSwitch.grid(    row=1, column=1, sticky="nsew", padx=5, pady=5)
            gain.grid(        row=2, column=1, sticky="nsew", padx=5, pady=5)
            loGain.grid(      row=3, column=1, sticky="nsew", padx=5, pady=5)
            hiGain.grid(      row=4, column=1, sticky="nsew", padx=5, pady=5)
            loMidFreq.grid(   row=5, column=1, sticky="nsew", padx=5, pady=5)
            loMidGain.grid(   row=6, column=1, sticky="nsew", padx=5, pady=5)
            hiMidFreq.grid(   row=7, column=1, sticky="nsew", padx=5, pady=5)
            hiMidGain.grid(   row=8, column=1, sticky="nsew", padx=5, pady=5)
            level.grid(       row=9, column=1, sticky="nsew", padx=5, pady=5)
            loCut.grid(       row=10, column=1, sticky="nsew", padx=5, pady=5)
            hiCut.grid(       row=11, column=1, sticky="nsew", padx=5, pady=5)
            compression.grid( row=12, column=1, sticky="nsew", padx=5, pady=5)
            noiseSuppression.grid( row=13, column=1, sticky="nsew", padx=5, pady=5)

            # Add elements to list
            self.instrument_elements.append({
                'eqSwitch': eqSwitch,
                'gain': gain,
                'loGain': loGain,
                'hiGain': hiGain,
                'loMidFreq': loMidFreq,
                'loMidGain': loMidGain,
                'hiMidFreq': hiMidFreq,
                'hiMidGain': hiMidGain,
                'level': level,
                'loCut': loCut,
                'hiCut': hiCut,
                'compression': compression,
                'noiseSuppression': noiseSuppression
            })





root = tk.Tk()
root.title("Input Editor")
tmp = InputFrame(root)
tmp.pack(expand=True, fill="both")
root.mainloop()





