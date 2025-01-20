import re
# This is a function to read a file as text and get all of the XML non-nested tags
# from the file. This is used to read the settings file for the program.
def readSettingsFile(fileName):
    with open(fileName, "r") as file:
        data = file.read()
    # This is a regular expression to get all of the XML tags from the file.
    # This will return a list of all of the tags in the file.
    # print(data)
    settings = re.findall(r"(?=\n)<[^>]+>", data)
    return settings
myFile = r"C:\Users\cjbag\Documents\projects\rc600-editor\exampleData\ROLAND\DATA\MEMORY001A.RC0"
settings = readSettingsFile(myFile)
print(settings)