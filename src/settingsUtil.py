import re
import json
import xmltodict

# These are the tags that are not allowed in standard XML but stupid Roland uses them
bad_tags = [("0", "ZERO"), ("1", "ONE"), ("2", "TWO"), ("3", "THREE"), ("4", "FOUR"), ("5", "FIVE"), ("6", "SIX"), ("7", "SEVEN"), ("8", "EIGHT"), ("9", "NINE"),("#","POUND")]
# This function reads a settings file string and returns the setting as a dictionary
def read_settings_text(data):
    # remove the bad tags
    for tag in bad_tags:
        data = data.replace(f"<{tag[0]}>", f"<{tag[1]}>")
        data = data.replace(f"</{tag[0]}>", f"</{tag[1]}>")
    # remove last tag "count"
    cVal = re.findall(r"\n<count>(.*?)</count>", data)[0]
    data = re.sub(r"\n<count>.*?</count>", "", data)
    outputDict = xmltodict.parse(data)
    outputDict['count'] = cVal
    return outputDict

def write_settings_text(data):
    cVal = data['count']
    del data['count']
    settingsText = xmltodict.unparse(data, pretty=True)
    # Replace the temporary tags with the original tags
    for tag in bad_tags:
        settingsText = settingsText.replace(f"<{tag[1]}>", f"<{tag[0]}>")
        settingsText = settingsText.replace(f"</{tag[1]}>", f"</{tag[0]}>")
    # put back to initial tab formatting
    settingsText = re.sub(r"\t+", "", settingsText, flags=re.MULTILINE)
    settingsText = re.sub(r"^<([^>]+)>([^\n]+?)<\/\1>$",r"\t<\1>\2</\1>",settingsText,flags=re.MULTILINE)
    # add the count tag back
    settingsText += f"\n<count>{cVal}</count>"
    return settingsText

def write_settings_file(data, filename):
    settingsText = write_settings_text(data)
    with open(filename, 'w') as file:
        file.write(settingsText)

"""This function reads a single settings file from the boss rc600.  The file should be formatted
 just like an XML file, but the tags are allowed to start with numeric values. The value
 that is returned from the function is in a dictionary format.  The keys are the tags and the
 values are the values of the tags."""
def read_settings_file(fileName):
    with open(fileName, "r") as file:
        data = file.read()
    return read_settings_text(data)

# This function converts a dictionary to a string
def uni2Str(d):
    outStr = ""
    for key, value in d.items():
        outStr += chr(int(value))
    return outStr

# This function converts a string to a dictionary with
# alphabetic keys up to 12 characters
def str2Uni(s):
    outDict = {}
    for i in range(12):
        if i >= len(s):
            # pad with spaces
            s += chr(32)
        outDict[chr(65+i)] = ord(s[i])
    return outDict
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