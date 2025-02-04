import tkinter as tk
from tkinter import ttk
from memoryEditorComponent import MemoryEditorComponent
from os import listdir
from os.path import isfile, join
import settingsUtil as su

class DeviceMemoryEditor(ttk.Frame):
    def __init__(self, parent, rootDir):
        super().__init__(parent)
        self.parent = parent
        self.is_loading_config = False
        # get a list of all files under the root directory
        self.rootDir = rootDir
        self.configsList = []
        for f in listdir(rootDir + "/Data"):
            if isfile(join(rootDir + "/Data", f)) and f.endswith("B.RC0"):
                curItem = {}
                curDict = su.read_settings_file(join(rootDir + "/Data", f))
                curItem["file"] = f
                curItem["title"] = su.uni2Str(curDict['database']['mem']['NAME'])
                curItem["settings"] = curDict
                self.configsList.append(curItem)
        self.create_widgets()

    def create_widgets(self):
        # Create a frame for the listbox and scrollbar
        list_frame = ttk.Frame(self)
        list_frame.grid(row=0, column=0, sticky="ns")

        # Create Save and Restore buttons above the listbox
        save_button = ttk.Button(list_frame, text="Save")
        save_button.grid(row=0, column=0, sticky="ew")
        restore_button = ttk.Button(list_frame, text="Restore")
        restore_button.grid(row=1, column=0, sticky="ew")
        save_button.bind("<Button-1>", self.save_config)
        restore_button.bind("<Button-1>", self.restore_config)

        # Create a scrollbar
        scrollbar = ttk.Scrollbar(list_frame, orient="vertical")
        scrollbar.grid(row=2, column=1, sticky="ns")

        # Create a listbox
        self.listbox = tk.Listbox(list_frame, yscrollcommand=scrollbar.set,exportselection=False)
        self.listbox.grid(row=2, column=0, sticky="nsew")
        scrollbar.config(command=self.listbox.yview)

        # Configure grid weights for list_frame
        list_frame.grid_rowconfigure(2, weight=1)
        list_frame.grid_columnconfigure(0, weight=1)

        # Populate the listbox with items
        for idx, config in enumerate(self.configsList):
            self.listbox.insert(tk.END, f"{idx + 1}. {config['title']}")

        # Bind the listbox selection event
        self.listbox.bind("<<ListboxSelect>>", self.on_config_item_selected)

        # Create a frame for the MemoryEditorComponent
        self.editor_frame = ttk.Frame(self)
        self.editor_frame.grid(row=0, column=1, sticky="nsew")

        # Configure grid weights for the main frame
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

    def on_config_item_selected(self, event):
        # Get the selected item index
        if self.is_loading_config:
            return
        self.is_loading_config = True
        print("Loading config")
        selection = event.widget.curselection()
        if selection:
            index = selection[0]
            item = self.configsList[index]
            self.cur_config_index = index
            self.load_editor_from_config_item(item)
        # set the selection to what was initially selected
        self.listbox.selection_clear(0, tk.END)
        self.is_loading_config = False

    def load_editor_from_config_item(self, item):
        # Clear the editor frame
        for widget in self.editor_frame.winfo_children():
            widget.destroy()

        # Create a new MemoryEditorComponent
        self.cur_editor_item = item
        self.editor = MemoryEditorComponent(self.editor_frame)
        self.editor.load_from_settings_dict(item["settings"])
        self.editor.pack(expand=True, fill="both")

    def save_config(self, event):
        settings_dict = self.editor.export_as_settings_dict()
        self.cur_editor_item["settings"] = settings_dict
        su.write_settings_file(settings_dict, join(self.rootDir + "/Data", self.cur_editor_item["file"]))
        self.configsList[self.cur_config_index]["settings"] = settings_dict
        self.configsList[self.cur_config_index]["title"] = su.uni2Str(settings_dict['database']['mem']['NAME']) 
        self.listbox.delete(self.cur_config_index)
        self.listbox.insert(self.cur_config_index, f"{self.cur_config_index + 1}. {self.configsList[self.cur_config_index]['title']}")
        # self.
        # self.editor_config = settings_dict

    def restore_config(self, event):
        self.load_editor_from_config_item(self.cur_editor_item)


# Example usage
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Device Memory Editor")

    rootDir = r"C:\Users\cjbag\Documents\projects\rc600-editor\exampleData\ROLAND"

    app = DeviceMemoryEditor(root, rootDir)
    app.pack(expand=True, fill="both")

    root.mainloop()