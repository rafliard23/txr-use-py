import customtkinter as ctk
from tkinter import messagebox
import utils.constants
import utils.io

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("green")

start_dir = None

class control_section(ctk.CTkFrame):
    # flag for first time
    first_run = True
    
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.save_dir = ''
        
        self.button_open = ctk.CTkButton(self, text="Open", command=self.button_open_callback)
        self.button_open.grid(row=0, column=0, padx=20, pady=(60, 20), sticky="ew")
        self.button_save = ctk.CTkButton(self, text="Save", command=self.button_save_callback)
        self.button_save.grid(row=1, column=0, padx=20, pady=(0, 20), sticky="ew")
        self.button_saveas = ctk.CTkButton(self, text="Save As", command=self.button_saveas_callback)
        self.button_saveas.grid(row=2, column=0, padx=20, pady=(0, 20), sticky="ew")
        self.button_close = ctk.CTkButton(self, text="Apply Changes", command=self.button_apply_callback)
        self.button_close.grid(row=3, column=0, padx=20, pady=(0, 20), sticky="ew")

        self.version_label = ctk.CTkLabel(self, text=f"Ver. {utils.constants.VERSION}", fg_color="transparent", text_color=("black", "white"))
        self.version_label.grid(row=8, column=0, padx=20, pady=(0, 0), sticky="sew")
        self.author_info = ctk.CTkLabel(self, text=f"by: {utils.constants.MAIN_AUTHOR}")
        self.author_info.grid(row=9, column=0, padx=20, pady=(0, 10), sticky="ews")
        self.grid_rowconfigure(6, weight=1)

    # Callback for open button and initiator for loading data
    def button_open_callback(self, event=None):
        self.save_dir = utils.io.get_save_file()
        if (self.save_dir):
            utils.io.sav_to_json(self.save_dir)
            utils.io.load_json()
            self.open_act_player_data_handler()
            self.open_act_vehicle_list_handler()
            self.open_act_player_stats_handler()
        else:
            pass
        utils.io.load_json()
        self.open_act_player_data_handler()
        self.open_act_vehicle_list_handler()
        self.open_act_player_stats_handler()    

    def button_save_callback(self, event=None):
        if (self.save_dir):
            self.button_apply_callback()
            utils.io.json_to_sav(self.save_dir)
            messagebox.showinfo("Save Complete", "All changes has been saved!")
        else:
            messagebox.showwarning("Warning!", "Load save file first!")

    def button_saveas_callback(self, event=None):
        saveas_dir = utils.io.set_saveas_file()
        # proceed to convert the json to sav if path exist
        if (saveas_dir):
            self.button_apply_callback()
            utils.io.json_to_sav(saveas_dir)
            messagebox.showinfo("Save Complete", "All changes has been saved!")
        else:
            pass
        
    def button_apply_callback(self):
        # We save the player data first
        data = self.player_data.get_entry_player_data()
        org_data = self.player_data.get_org_player_data()
        utils.io.set_player_data(data, org_data)
    
        # Afterward we save the vehicle upgrade
        id = self.vehicle_list.get_last_selected_id()
        data = self.vehicle_upgrades.get_optionMenu_edit(id)
        utils.io.set_vehicle_upgrade(data, id)
        # Now we refresh player stats
        self.open_act_player_stats_handler()

    # Wrapper for Player Data (tabbed) main task displayer
    def open_act_player_data_handler(self):
        self.player_data.update_player_data()

    # Wrapper for Vehicle List main task displayer
    def open_act_vehicle_list_handler(self):
        self.vehicle_list.get_vehicle_list()

    # Wrapper for Player Stats (Righternmost) main task displayer
    def open_act_player_stats_handler(self):
        self.player_stats.get_player_data()

    
    # Method handler for showing last selected
    def show_last_selected(self):
        last_data = self.vehicle_list.get_last_selected_vehicle()
        if (self.first_run == True):
            self.init_last_selected(last_data[0], last_data[1])
        else:
            self.last_selected_text = ctk.StringVar()
            self.last_selected_text.set(f"#{last_data[0]} {last_data[1]}")
            self.button_action.configure(textvariable=self.last_selected_text)
    
    # This method used for displaying the initial, below method used for updating and control
    def init_last_selected(self, last_selected, last_name):
        self.label_action = ctk.CTkLabel(self, text="Last selected:")
        self.label_action.grid(row=6, column=0, padx=20, pady=(20, 0), sticky="sew")
        self.last_selected_text = ctk.StringVar()
        self.last_selected_text.set(f"#{last_selected} {last_name}")
        self.button_action = ctk.CTkButton(self, textvariable=self.last_selected_text,
                                           width=100, state="disabled",
                                           text_color_disabled="white")
        self.button_action.grid(row=7, column=0, padx=20, pady=(10, 20), sticky="sew")
        self.first_run = False

class tabs_section(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.grid(row=0, column=0, sticky="nsew")
        self.grid_columnconfigure(0, weight=1)


class player_data_tab(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.grid(row=0, column=0, sticky="nsew")

    # For deconstruct widgets
    def clean_player_data(self):
        for widget in self.winfo_children():
            widget.destroy()
        del self.entries, self.player_data, 
    
    def update_player_data(self):
        FLAG = utils.io.PLAYER_DATA_FLAG.RW
        self.player_data = utils.io.get_player_data(FLAG)
        
        self.grid_columnconfigure(1, weight=1)  # Make column 1 stretch
        self.entries = []

        for i, field in enumerate(utils.constants.PLAYER_STRINGS, start=0):  # Start from row 1
            self.label = ctk.CTkLabel(self, text=field + ":")
            self.label.grid(row=i, column=0, padx=10, pady=(5,0), sticky="w")  # Align left
            
            if i in {0, 1, 4}:
                self.entry = ctk.CTkEntry(self, width=150, placeholder_text=f"{self.player_data[i]:,}")
            else:
                self.entry = ctk.CTkEntry(self, width=150, placeholder_text=self.player_data[i])
            self.entry.grid(row=i, column=1, padx=10, pady=(5,0), sticky="e")  # Expand entry
            
            # Store entry widget in dictionary
            self.entries.append(self.entry)

    def get_entry_player_data(self):
        value = []

        # This one handy for checking whether it's empty or not for later
        checker = 0
        for i, entry in enumerate(self.entries):
            value.append(entry.get())
            checker += value[i].__sizeof__()

        value.append(checker)
        return value
    
    def get_org_player_data(self):
        return self.player_data
        

class vehicle_list_tab(ctk.CTkScrollableFrame):
    # variable to store the buttons
    buttons = []
    selected_button = None
    identifiers = None

    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.grid(row=0, column=0, sticky="nsew")
        master.grid_columnconfigure(0, weight=1)
        master.grid_rowconfigure(0, weight=1)

        # Label and Entry placeholder
        self.equipped_car = ctk.CTkLabel(self, text=f"Load Save File First!")
        self.equipped_car.grid(row=0, column=0, padx=10, pady=(5,0), sticky="ew")
    
    # For deconstruct placeholder label and previous entries
    def clean_widget(self):
        for widget in self.winfo_children():
            widget.destroy()
        self.buttons = []
    
    # Method to request vehicle data and display the list to the GUI element
    def get_vehicle_list(self):
        self.clean_widget()
        self.car_names, self.car_ids = utils.io.get_car_list()

        # We make tuple out of car_names, and car_ids
        identifiers = list(zip(self.car_names, self.car_ids))

        # We displaying the GUI element here
        for idx, (self.car_names, self.car_ids) in enumerate(identifiers):
            button = ctk.CTkButton(self, text=f"#{self.car_ids} {self.car_names}", fg_color="transparent",
                                   width=240, font=ctk.CTkFont("Arial", 14), border_width=2,
                                   border_color=ctk.ThemeManager.theme["CTkButton"]["fg_color"],
                                   command=lambda b=idx, id=self.car_ids,
                                           name=self.car_names: self.button_callback(b, id, name))
            button.pack(pady=6)
            self.buttons.append(button)

    # Button callback to check last selected vehicle ids
    def button_callback(self, button, id, name):
        
        self.last_car_id = id
        self.last_car_name = name

        # If a button is already selected, reset its color
        if self.selected_button is not None:
            self.buttons[self.selected_button].configure(fg_color="transparent")

        # Highlight the clicked button
        self.buttons[button].configure(fg_color=ctk.ThemeManager.theme["CTkButton"]["fg_color"])  # Change to your desired highlight color
        self.selected_button = button

        # Update UI element in Control frame, and Vehicle Upgrades attribute
        self.control_frame.show_last_selected()
        self.vehicle_upgrades.get_vehicle_upgrades()
        
        # Print the button's unique ID to the console
        # print(f"Button clicked: ID {id}")

    # Getter for selected car id and chassic code
    def get_last_selected_vehicle(self):
        return list((self.last_car_id, self.last_car_name))
    
    # Getter for selected car id only!
    def get_last_selected_id(self):
        try:
            self.last_car_id
        except AttributeError:
            self.last_car_id = 0      # We print 0 to identify that we haven't selected the car
        return self.last_car_id    

class vehicle_upgrade_tab(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.grid(row=0, column=0, sticky="nsew")
        master.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

    def clean_widget(self):
        for widget in self.winfo_children():
            widget.destroy()

    # Wrapper method for external class usage
    def get_vehicle_upgrades(self):
        id = self.vehicle_list.get_last_selected_id()
        data = utils.io.get_selected_car_upgrades(id)
        self.clean_widget()
        self.levels = []
        self.set_vehicle_upgrades(data)
    
    # Getter for current OptionMenu values
    def get_optionMenu_edit(self, id):
        # First we check whether user has selected car or not
        if (id != 0):
            data = []
            # We get the levels var to get each OptionMenu values
            for i, option_menu in enumerate(self.levels):
                value = option_menu.get()
                data.append(value)
            return data

    # This method used for displaying to GUI element
    def set_vehicle_upgrades(self, data):
        # Loop to create Labels and OptionMenus
        for i, field in enumerate(utils.constants.UPGRADES_STRINGS):
            self.label = ctk.CTkLabel(self, text=field)
            self.label.grid(row=i, column=0, padx=10, pady=5, sticky="w")

        # Dynamically set the value based off data from JSON; need several ifs
            if i == 0:
                # Engine PU
                self.option_var = ctk.StringVar(value=utils.constants.LEVEL_STRINGS[data[i]])
                self.option_menu = ctk.CTkOptionMenu(self, width=160,
                                                     values=utils.constants.LEVEL_STRINGS,
                                                     variable=self.option_var)
                self.option_menu.grid(row=i, column=1, padx=10, pady=(5,0), sticky="e")

            elif i in {1,2}:
                # Intake, Exhaust
                self.option_var = ctk.StringVar(value=utils.constants.LEVEL_STRINGS[data[i]])
                self.option_menu = ctk.CTkOptionMenu(self, width=160,
                                                     values=utils.constants.LEVEL_EXH_INTK,
                                                     variable=self.option_var)
                self.option_menu.grid(row=i, column=1, padx=10, pady=(5,0), sticky="e")
            
            elif i in {3, 4, 5, 6, 7, 8}:
                # Most of Handling
                self.option_var = ctk.StringVar(value=utils.constants.LEVEL_STRINGS[data[i]])
                self.option_menu = ctk.CTkOptionMenu(self, width=160,
                                                     values=utils.constants.LEVEL_HANDLINGS,
                                                     variable=self.option_var)
                self.option_menu.grid(row=i, column=1, padx=10, pady=(5,0), sticky="e")
            
            elif i in {9, 10}:
                # LSD and Nitro
                self.option_var = ctk.StringVar(value=utils.constants.LEVEL_STRINGS[data[i]])
                self.option_menu = ctk.CTkOptionMenu(self, width=160,
                                                     values=utils.constants.LEVEL_MISC,
                                                     variable=self.option_var)
                self.option_menu.grid(row=i, column=1, padx=10, pady=(5,0), sticky="e")
            
            else:
                # Car' mileage entry
                self.option_menu = ctk.CTkEntry(self, width=160, placeholder_text=data[i])
                self.option_menu.grid(row=i, column=1, padx=10, pady=(5,0), sticky="e")
            
            # Store OptionMenu selections (for later)
            self.levels.append(self.option_menu)

class status_section(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

    # For deconstruct placeholder label and previous entries
    def update_player_data(self):
        for widget in self.winfo_children():
            widget.destroy()

    # We get the data and prepare to display it on the UI element
    def get_player_data(self):
        FLAG = utils.io.PLAYER_DATA_FLAG.R
        self.update_player_data()
        
        # Get JSON data from Backend
        player_data = utils.io.get_player_data(FLAG)

        self.stats_title = ctk.CTkLabel(self, text="Player Stats", fg_color="transparent",
                                        anchor="center", font=ctk.CTkFont(size=16, weight="bold"))
        self.stats_title.grid(row=0, column=0, columnspan=2, padx=20, pady=(0, 10), sticky="ew")
        self.grid_columnconfigure(1, weight=1)

        for i, value in enumerate(utils.constants.STATUS_STRINGS, start=0):
            stats = ctk.CTkLabel(self, text=value, fg_color="transparent")
            stats.grid(row=(i+1), column=0, padx=10, sticky="w")
            
            # If conditional for formatting purposes
            if i in {0, 1, 8}:
                stats_value = ctk.CTkLabel(self, text=f"{player_data[i]:,}", fg_color="transparent")
            elif (i == 7):
                stats_value = ctk.CTkLabel(self, text=f"{player_data[i]} km", fg_color="transparent")
            elif (i == 10):
                stats_value = ctk.CTkLabel(self, text=f"{len(self.vehicle_list.buttons)}", fg_color="transparent")
            else:
                stats_value = ctk.CTkLabel(self, text=player_data[i], fg_color="transparent")

            stats_value.grid(row=(i+1), column=1, padx=10, sticky="w")

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        # define the the global
        global start_dir

        # Set window attributes
        self.title("Tokyo Xtreme Racer - Save Editor")
        self.iconbitmap('./app.ico')
        self.geometry(f"{760}x{560}")

        # Bootstrap things
        utils.io.check_tmp_exist()
        start_dir = utils.io.set_default_start_dir()

        # Adjust rows and columns
        self.grid_columnconfigure(2, weight=1)

        # create TabView
        self.tab_view = ctk.CTkTabview(self)
        self.tab_view.grid(row=0, rowspan=4, column=1, padx=10, pady=(5,10), sticky="nsew")
        
        # Add player status section
        self.player_stats = status_section(self, width=200)
        self.player_stats.grid(row=0, rowspan=4, column=2, padx=(0, 10), pady=(10, 10),sticky="nsew")
        self.grid_rowconfigure(3, weight=1)

        # Control frame
        self.control_frame = control_section(self, width=160)
        self.control_frame.grid(row=0, rowspan=4, column=0, sticky="ns")

        # Prepares tab
        # Player data tab
        self.player_data_tab = self.tab_view.add("Player Data")
        self.player_data = player_data_tab(self.player_data_tab)

        # Vehicles list tab
        self.vehicle_list_tab = self.tab_view.add("Vehicles List")
        self.vehicle_list = vehicle_list_tab(self.vehicle_list_tab)

        # Vehicles upgrade
        self.vehicle_upgrades_tab = self.tab_view.add("Vehicle Upgrades")
        self.vehicle_upgrades = vehicle_upgrade_tab(self.vehicle_upgrades_tab)

        # We set controllers & keybinds here
        self.set_controller()
        self.set_keybind()

    def set_controller(self):
        # Tabs
        self.player_data.control_frame = self.control_frame
        self.vehicle_list.control_frame = self.control_frame
        self.vehicle_upgrades.control_frame = self.control_frame

        self.player_stats.control_frame = self.control_frame
        self.player_stats.vehicle_list = self.vehicle_list

        # Tab with Tab
        self.vehicle_list.vehicle_upgrades = self.vehicle_upgrades
        self.vehicle_upgrades.vehicle_list = self.vehicle_list
        
        # Reference for control_frame
        self.control_frame.player_data = self.player_data
        self.control_frame.vehicle_list = self.vehicle_list
        self.control_frame.vehicle_upgrades = self.vehicle_upgrades
        self.control_frame.tab_view = self.tab_view

        self.control_frame.player_stats = self.player_stats

    def set_keybind(self):
        # We set both the lower and upper case in case capslock on or off
        # CTRL + S; for Save
        self.bind('<Control-s>', self.control_frame.button_save_callback)
        self.bind('<Control-S>', self.control_frame.button_save_callback)

        # CTRL + SHIFT + S; for Save As
        self.bind('<Control-Shift-s>', self.control_frame.button_saveas_callback)
        self.bind('<Control-Shift-S>', self.control_frame.button_saveas_callback)

        # CTRL + O; for Open
        self.bind('<Control-o>', self.control_frame.button_open_callback)
        self.bind('<Control-O>', self.control_frame.button_open_callback)

app = App()
app.mainloop()