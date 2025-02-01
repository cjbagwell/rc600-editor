import re
import json

# This function reads xml text and returns the setting as a dictionary
def read_settings_text(inputText):
    settings = {}
    # find all tags
    matches = re.findall(r"<(\w+)[^>]*>(.*?)</\1>", inputText, re.DOTALL)
    for match in matches:
        tagName = match[0]
        tagValue = match[1]
        # recursively process the tag value
        processedValue = read_settings_text(tagValue)
        if tagName in settings:
            if isinstance(settings[tagName], list):
                settings[tagName].append(processedValue)
            else:
                settings[tagName] = [settings[tagName], processedValue]
        else:
            settings[tagName] = processedValue
    return settings if settings else inputText

"""This function reads a single settings file from the boss rc600.  The file should be formatted
 just like an XML file, but the tags are allowed to start with numeric values. The value
 that is returned from the function is in a dictionary format.  The keys are the tags and the
 values are the values of the tags."""
def read_settings_file(fileName):
    with open(fileName, "r") as file:
        data = file.read()
        # remove the xml version tag
        data = re.sub(r"<\?xml[^>]+\?>", "", data)
    # replace numeric tags with a double letter letter
    return read_settings_text(data)

# This function converts a dictionary to a string
def uni2Str(d):
    outStr = ""
    for key, value in d.items():
        outStr += chr(int(value))
    return outStr

# # Function to export a dictionary as a JSON file
# def export_to_json(data, filename):
#     with open(filename, 'w') as json_file:
#         json.dump(data, json_file, indent=4)

def printTrackSettings(trackDict):
    # None of this is confirmed yet, just predictions
    # print(f"REVERSE:         {trackDict['A']}")#CONFIRMED
    # print(f"1SHOT:           {trackDict['B']}")#CONFIRMED
    # print(f"PAN:             {trackDict['C']}")#CONFIRMED
    # print(f"PLAY_LEVEL:      {trackDict['D']}")#CONFIRMED
    # print(f"START_MODE:      {trackDict['E']}")#CONFIRMED
    # print(f"STOP_MODE:       {trackDict['F']}")#CONFIRMED
    # print(f"DUB_MODE:        {trackDict['G']}")#CONFIRMED
    # print(f"FX:              {trackDict['H']}")#CONFIRMED
    # print(f"PLAY_MODE:       {trackDict['I']}")#CONFIRMED
    # print(f"MEASURE:         {trackDict['J']}")#CONFIRMED
    # print(f"LOOPSYNC_SW:     {trackDict['K']}")
    # print(f"LOOPSYNC_MODE:   {trackDict['L']}")
    # print(f"TEMPOSYNC_SW:    {trackDict['M']}")#CONFIRMED
    # print(f"TEMPOSYNC_MODE:  {trackDict['N']}")#CONFIRMED
    # print(f"TEMPOSYNC_SPEED: {trackDict['O']}")#CONFIRMED
    # print(f"BOUNCE_IN:       {trackDict['P']}")#CONFIRMED
    print(f"MIC1:            {trackDict['Q']}")
    # print(f"MIC2:            {trackDict['R']}")
    # print(f"INST1:           {trackDict['S']}")
    # print(f"INST2:           {trackDict['T']}")
    # print(f"RHYTHM:          {trackDict['U']}")
    # print(f"SETTING-V:       {trackDict['V']}")
    # print(f"SETTING-W:       {trackDict['W']}")
    # print(f"SETTING-X:       {trackDict['X']}")
    # print(f"SETTING-Y:       {trackDict['Y']}")

if __name__ == "__main__":
    myFile =  r'exampleData\ROLAND\DATA\MEMORY062B.RC0'# Sweethome
    # myFile = r'exampleData\ROLAND\DATA\MEMORY001A.RC0'
    settings = read_settings_file(myFile)
    # export_to_json(settings, 'settings.json')
    myStr = uni2Str(settings['database']['mem']['NAME'])
    myDic = str2Uni(myStr)
    print(myStr)
    # print(f"Tempo {int(settings['database']['mem']['MASTER']['A'])/10} BPM")
    # print(f'Track 1')
    # printTrackSettings(settings['database']['mem']['TRACK1'])
    # print(f'\nTrack 2')
    # printTrackSettings(settings['database']['mem']['TRACK2'])
    # print(f'\nTrack 3')
    # printTrackSettings(settings['database']['mem']['TRACK3'])
    # print(f'\nTrack 4')
    # printTrackSettings(settings['database']['mem']['TRACK4'])
    # print(f'\nTrack 5')
    # printTrackSettings(settings['database']['mem']['TRACK5'])
    # print(f'\nTrack 6')
    # printTrackSettings(settings['database']['mem']['TRACK6'])
    # print(settings['database']['mem']['MASTER']['D'])
    # [print(x) for x in settings['database']['mem']]
    # print(settings['database']['mem'].keys())
    print('here')