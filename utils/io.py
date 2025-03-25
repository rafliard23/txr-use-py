import json
import os
import subprocess
import customtkinter as ctk
from customtkinter import filedialog
from enum import IntFlag
from . import constants

default_start_dir = None

json_data = None

PLAYER_DATA_FLAG = IntFlag("USER_DATA_FLAG", ["RW", "R"])

def check_tmp_exist():
    # check if tmp dir exist or not in ./bin; if not, we will create one.
    if (os.path.exists('./bin/tmp')):
        pass
    else:
        os.makedirs("./bin/tmp")

# Setter for default starting location based off U/name
def set_default_start_dir():
    global default_start_dir
    default_start_dir = os.path.join(os.environ.get('LOCALAPPDATA'),
                                     'TokyoXtremeRacer').replace("\\","/")

# Getter save file location based on loaded save file
def get_save_file():
    save_path = filedialog.askopenfilename(filetypes=[('UE5 Save File', '*.sav'),
                                                ('All Files', '*.*')],
                                                initialdir=default_start_dir).replace("\\","/")
    return save_path

# Set path for save as operation    
def set_saveas_file():
    save_path = filedialog.asksaveasfilename(filetypes=[('UE5 Save File', '*.sav'),
                                                ('All Files', '*.*')],
                                                initialdir=default_start_dir).replace("\\","/")
    return save_path

# End of Save File related I/O
# --- JSON I/O --- #

def load_json():
    # For efficient process, we put the JSON data as global var for read operation
    global json_data

    if not os.path.exists(constants.TMP_PATH):
        print("Error: JSON file not found!")
        return
    
    with open(constants.TMP_PATH,"r", encoding="utf-8") as file:
        json_data = json.load(file)
 
# --- Data Getter Starts here  --- #
# Fetch list of cars owned in save file
def get_car_list():
    # Navigate to MyCars_0
    my_cars = (
        json_data.get("root", {})
        .get("properties", {})
        .get("user_info_0", {})
        .get("Struct", {})
        .get("Struct", {})
        .get("MyCars_0", {})
        .get("Map", [])
    )
    
    # Collect each car' chassis code from Map[] entry in JSON
    car_names = [
        car["value"]["Struct"]["Struct"]["CarNameId_0"]["Name"]
        for car in my_cars
        if "CarNameId_0" in car["value"]["Struct"]["Struct"]
    ]

    # Collect each car' index id based on player' buying order in JSON
    car_ids = [
        car["key"]["Int"]
        for car in my_cars
        if "Int" in car["key"]
    ]

    return car_names, car_ids

# Fetch player stats from JSON
def get_player_data(DATA_FLAG):
    # Navigate to MyCars_0
    player_data = (
        json_data.get("root", {})
        .get("properties", {})
        .get("user_info_0", {})
        .get("Struct", {})
        .get("Struct", {})
    )

    # Collecting several values here
    Cp = player_data["Cp_0"]["Int64"]
    MaxCP = player_data["UpperLimitCP_0"]["Int64"]
    Bp = player_data["PP_0"]["Int"]
    Win = player_data["WinNum_0"]["Int"]
    Lose = player_data["LoseNum_0"]["Int"]
    Draw = player_data["DrawNum_0"]["Int"]
    WinStreak = player_data["MaxWiningStreak_0"]["Int"]
    TotalMileage = player_data["TotalMileages_0"]["Double"]
    EarnedCP = player_data["CumulativeAcquisitionCP_0"]["Int64"]
    GarageSize = player_data["MaxGarageMyCarNum_0"]["Int"]

    # Preprocess the TotalMileage value to Human Readable value
    TotalMileage = round((TotalMileage / 1000), 1)

    # Sending the data based on given flag during method call
    # R for Read Only (displayed on rightern most stats section)
    # RW for Read/Write for player data tab
    if (DATA_FLAG & PLAYER_DATA_FLAG.R):
        return (list(((MaxCP), (Cp), (Bp), (Win), (Lose),
                    (Draw), (WinStreak),(TotalMileage), 
                    (EarnedCP), (GarageSize))))
    elif (DATA_FLAG & PLAYER_DATA_FLAG.RW):
        return (list(((MaxCP), (Cp), (Bp), (TotalMileage),
                     (EarnedCP), (GarageSize))))

# Fetch car' equipped upgrades on selected car from vehicle list    
def get_selected_car_upgrades(id):
    # Init a variable for storing our level data later
    data = []

    my_cars = (
        json_data.get("root", {})
        .get("properties", {})
        .get("user_info_0", {})
        .get("Struct", {})
        .get("Struct", {})
        .get("MyCars_0", {})
        .get("Map", [])
    )
    
    # finding our selected car based on passsed id arg
    current_car = next((car for car in my_cars if car["key"]["Int"] == id), None)
    # tunes = current_car["value"]["Struct"]["Struct"]["TuneInfos_0"]["Map"]
    for tunes in current_car["value"]["Struct"]["Struct"]["TuneInfos_0"]["Map"]:
        # we collect each upgrades level, and append them as list
        for i, value in enumerate(constants.UPGRADES_RAW_STRINGS, start=0):
            if i == 9:
                # We skip rear tire, for display purpose. We can sort that later
                continue
            if tunes["key"]["Enum"] == constants.UPGRADES_RAW_STRINGS[i]:
                tune = tunes["value"]["Struct"]["Struct"]["EquipLevel_0"]["Enum"]
                tune = constants.LEVEL_RAW_STRINGS.index(tune)
                
                data.append(tune)
    
    data.append(round(current_car["value"]["Struct"]["Struct"]["Mileages_0"]["Double"],1))

    return data

# --- Data Getter ends here  --- #
# --- Data Setter starts here  --- #

def set_player_data(data, org_data):
    global json_data

    # Check whether we have data or not
    if (data[6] != 294):    # As I said earlier, it's handy
        processed = []

        # If from data is empty, we print back the placeholder data
        for i in range(6):
            # We check it first, if it's empty, we give org data
            if ((data[i]).__sizeof__() == 49):
                processed.append(org_data[i])
            else:
                # If we reached mileage, treat is as float and do processing on it
                if i == 3:
                    conversion = round((float(data[3]) * 1000.001), 3)
                    processed.append(conversion)
                    continue # Move to next iteration
                conversion = int(data[i])
                processed.append(conversion)
    
    # Now we check if we truly have empty entries back in player_data tab
    if (data[6] != 294):
        player_data = (
            json_data.get("root", {})
            .get("properties", {})
            .get("user_info_0", {})
            .get("Struct", {})
            .get("Struct", {})
        )
        # Buffer CP, BP, MaxCP, TotalMileage, Acc.CP, Garage
        player_data["UpperLimitCP_0"]["Int64"]              = processed[0]
        player_data["Cp_0"]["Int64"]                        = processed[1]
        player_data["PP_0"]["Int"]                          = processed[2]
        player_data["TotalMileages_0"]["Double"]            = processed[3]
        player_data["CumulativeAcquisitionCP_0"]["Int64"]   = processed[4]
        player_data["MaxGarageMyCarNum_0"]["Int"]           = processed[5]

        with open(constants.TMP_PATH, "w", encoding="utf-8") as file:
            json.dump(json_data, file, indent=2, separators=(",",":"))

        load_json()

    del processed, data, org_data

def set_vehicle_upgrade(data, id):
    global json_data

    if (id != 0):
        org_data = get_selected_car_upgrades(id)

        processed = []

        # Refactoring here
        for i in range(13):
            # We process rear tires from front tires data
            if (i == 9):
                converted = processed[i-1]
                processed.append(converted)
                continue
            # Several ifs, we going to shift the remaining stuffs
            if i in {10, 11}:
                converted = constants.LEVEL_RAW_STRINGS[constants.LEVEL_STRINGS.index(data[i-1])]
                processed.append(converted)
                continue
            # We process car' mileage here
            if (i == 12):
                # If we spot the entry are empty/isn't filled by user
                if (data[i-1].__sizeof__() == 49):
                    processed.append(org_data[11])
                    continue
                elif (data[i-1].__sizeof__() > 49):
                    converted = float(data[i-1])
                    processed.append(converted)
                    continue

            # 0-9 data
            converted = constants.LEVEL_RAW_STRINGS[constants.LEVEL_STRINGS.index(data[i])]
            processed.append(converted)

        my_cars = (
            json_data.get("root", {})
            .get("properties", {})
            .get("user_info_0", {})
            .get("Struct", {})
            .get("Struct", {})
            .get("MyCars_0", {})
            .get("Map", [])
        )

        # finding our selected car based on passsed id arg
        current_car = next((car for car in my_cars if car["key"]["Int"] == id), None)
        # tunes = current_car["value"]["Struct"]["Struct"]["TuneInfos_0"]["Map"]
        for tunes in current_car["value"]["Struct"]["Struct"]["TuneInfos_0"]["Map"]:
            # we collect each upgrades level, and append them as list
            for i, value in enumerate(constants.UPGRADES_RAW_STRINGS, start=0):
                if tunes["key"]["Enum"] == constants.UPGRADES_RAW_STRINGS[i]:
                    tunes["value"]["Struct"]["Struct"]["EquipLevel_0"]["Enum"] = processed[i]


        current_car["value"]["Struct"]["Struct"]["Mileages_0"]["Double"] = processed[12]

        with open(constants.TMP_PATH, "w", encoding="utf-8") as file:
                json.dump(json_data, file, indent=2, separators=(",",":"))

        load_json()

        # Just freeing memory
        del processed, converted, org_data, i

# --- Data Setter ends here  --- #
# ----- uesave-cli processes here ----- #

def sav_to_json(path):
    if path:
        subprocess.run(['./bin/uesave', 'to-json', '-i', f'{path}', '-o', f'{constants.TMP_PATH}'])
        
def json_to_sav(path):
    if path:
        subprocess.run([f'./bin/uesave', 'from-json', '-i', f'{constants.TMP_PATH}', '-o', f'{path}'])