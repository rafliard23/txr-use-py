import json
import os
import shutil
import subprocess
import customtkinter as ctk
from customtkinter import filedialog
from pathlib import Path
from enum import IntFlag
from . import constants

default_start_dir = None
default_backup_dir = None

json_data = None

isBackupDone = False

PLAYER_DATA_FLAG = IntFlag("USER_DATA_FLAG", ["RW", "R"])

def check_tmp_exist() -> None:
    # check if tmp dir exist or not in ./bin; if not, we will create one.
    if (os.path.exists('./bin/tmp')):
        pass
    else:
        os.makedirs("./bin/tmp")

# Setter for default starting location based off U/name
def set_default_start_dir() -> None:
    global default_start_dir
    
    default_start_dir = os.path.join(os.environ.get('LOCALAPPDATA'),
                                     'TokyoXtremeRacer').replace("\\","/")
    
def set_default_backup_dir() -> None:
    global default_start_dir, default_backup_dir

    default_backup_dir = default_start_dir + '/saved/SaveGamesBackup'
    if os.path.exists(default_backup_dir):
        pass
    else:
        os.makedirs(default_backup_dir)

# Getter save file location based on loaded save file
def get_save_file() -> str:
    save_path = filedialog.askopenfilename(filetypes=[('UE5 Save File', '*.sav'),
                                                ('All Files', '*.*')],
                                                initialdir=default_start_dir).replace("\\","/")
    return save_path

# Set path for save as operation    
def set_saveas_file() -> str:
    save_path = filedialog.asksaveasfilename(filetypes=[('UE5 Save File', '*.sav'),
                                                ('All Files', '*.*')],
                                                initialdir=default_start_dir).replace("\\","/")
    return save_path

# Backup save file processing, we take save file and then back it up to somewhere safe
def backup_save_file(save_path: str) -> None:
    global isBackupDone

    # Rebuild path from user base backup dir
    default_backup_save = default_backup_dir + "/UserData_00.sav.bak"
    
    if os.path.exists(default_backup_save) and isBackupDone == False:
        # We want to overwrite the file here
        shutil.copy(save_path, default_backup_save)
        isBackupDone = True
    else:
        set_default_backup_dir()
        shutil.copy(save_path, default_backup_save)
        isBackupDone = True

# End of Save File related I/O
# --- JSON I/O --- #

def load_json() -> None:
    # For efficient process, we put the JSON data as global var for read operation
    global json_data

    if not os.path.exists(constants.TMP_PATH):
        print("Error: JSON file not found!")
        return
    
    with open(constants.TMP_PATH,"r", encoding="utf-8") as file:
        json_data = json.load(file)
 
# --- Data Getter Starts here  --- #
# Fetch list of cars owned in save file
def get_car_list() -> list[str | int]:
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

# Get player current car counter
def get_player_car_count() -> int:
    global json_data

    counter_data = (
            json_data.get("root", {})
            .get("properties", {})
            .get("user_info_0", {})
            .get("Struct", {})
            .get("Struct", {})
            .get("MyCarIdSrc_0", {})
        )
    
    id = counter_data["Int"]

    return id

# Fetch player stats from JSON
def get_player_data(DATA_FLAG) -> list:
    # Navigate to MyCars_0
    player_data = (
        json_data.get("root", {})
        .get("properties", {})
        .get("user_info_0", {})
        .get("Struct", {})
        .get("Struct", {})
    )

    # Collecting several values here
    Cp              = player_data["Cp_0"]["Int64"]
    MaxCP           = player_data["UpperLimitCP_0"]["Int64"]
    Bp              = player_data["PP_0"]["Int"]
    Win             = player_data["WinNum_0"]["Int"]
    Lose            = player_data["LoseNum_0"]["Int"]
    Draw            = player_data["DrawNum_0"]["Int"]
    WinStreak       = player_data["MaxWiningStreak_0"]["Int"]
    TotalMileage    = player_data["TotalMileages_0"]["Double"]
    EarnedCP        = player_data["CumulativeAcquisitionCP_0"]["Int64"]
    GarageSize      = player_data["MaxGarageMyCarNum_0"]["Int"]
    Day             = player_data["Day_0"]["Int"]

    # Preprocess the TotalMileage value to Human Readable value
    TotalMileage = round((TotalMileage / 1000), 1)

    # Sending the data based on given flag during method call
    # R for Read Only (displayed on rightern most stats section)
    # RW for Read/Write for player data tab
    if (DATA_FLAG & PLAYER_DATA_FLAG.R):
        return (list(((MaxCP), (Cp), (EarnedCP),
                      (Bp), (Win), (Lose),
                      (Draw), (WinStreak),
                      (TotalMileage), (Day),
                      (GarageSize))))
    elif (DATA_FLAG & PLAYER_DATA_FLAG.RW):
        return (list(((MaxCP), (Cp), (Bp), (TotalMileage),
                     (EarnedCP), (GarageSize))))

# Fetch car' equipped upgrades on selected car from vehicle list    
def get_selected_car_upgrades(id: int) -> list:
    if id != 0:
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

        # finding our selected car based on passsed id arg & aliasing
        current_car = next((car for car in my_cars if car["key"]["Int"] == id), None)
        current_car = current_car["value"]["Struct"]["Struct"]

        # We scrape car' chassis code/internal name
        data.append(current_car["CarNameId_0"]["Name"])

        # Engine Swap & Aura
        data.append(current_car["EngineNameId_0"]["Name"])
        data.append(current_car["Effect_0"]["Struct"]["Struct"]["AuraNameId_0"]["Name"])

        # we collect each upgrades level, and append them as list
        for tunes in current_car["TuneInfos_0"]["Map"]:
            for i, value in enumerate(constants.UPGRADES_RAW_STRINGS, start=0):
                if tunes["key"]["Enum"] == constants.UPGRADES_RAW_STRINGS[i]:
                    tune = tunes["value"]["Struct"]["Struct"]["EquipLevel_0"]["Enum"]
                    tune = constants.LEVEL_RAW_STRINGS.index(tune)

                    data.append(tune)

        data.append(round(current_car["Mileages_0"]["Double"],1))

        return data

def get_vehicle_preset(car: list) -> str:
    global json_data

    if car[0] != 0:
        save_path = filedialog.asksaveasfilename(filetypes=[('TXR 25 Car Preset File', '*.sb25_preset'),
                                                    ('All Files', '*.*')],
                                                    defaultextension='.sb25_preset',
                                                    confirmoverwrite=True,
                                                    initialfile=f"{car[1]}_Untitled")
    if save_path:
        selected_car = (
                json_data.get("root", {})
                .get("properties", {})
                .get("user_info_0", {})
                .get("Struct", {})
                .get("Struct", {})
                .get("MyCars_0", {})
                .get("Map", [])
            )

        # fix for "next" line, dang it python
        id = car[0]

        current_car = next((car for car in selected_car if car["key"]["Int"] == id), None)
        current_car = current_car["value"]["Struct"]["Struct"]

        if current_car:
            preset = {
                "Paint_0": current_car["Paint_0"],
                "BodyStickers_0": current_car["BodyStickers_0"],
                "RearWingStickers_0": current_car["RearWingStickers_0"],
                "WindowStickers_0": current_car["WindowStickers_0"],
                "FrontBrake_0": current_car["FrontBrake_0"],
                "RearBrake_0": current_car["RearBrake_0"],
                "FrontTire_0": current_car["FrontTire_0"],
                "RearTire_0": current_car["RearTire_0"],
                "FrontWheelInfo_0": current_car["FrontWheelInfo_0"],
                "RearWheelInfo_0": current_car["RearWheelInfo_0"],
                "DressUpInfo_0": current_car["DressUpInfo_0"],
                "TuneInfos_0": current_car["TuneInfos_0"],
                "EngineNameId_0": current_car["EngineNameId_0"],
                "IsReplacedEngine_0": current_car["IsReplacedEngine_0"],
                "SettingInfo_0": current_car["SettingInfo_0"]
            }
        
        
        with open(save_path, "w", encoding="utf-8") as buffer_data:
            json.dump(preset, buffer_data, separators=(',', ':'), ensure_ascii=False)
    
    return save_path

# --- Data Getter ends here  --- #
# --- Data Setter starts here  --- #

def set_player_data(data: list[str]) -> None:
    global json_data

    data_count = len(data) - 1
    # Check whether we have data or not; data count always on tail
    if (data[data_count] != 294):    # As I said earlier, it's handy
        processed = []

        # preprocessor to convert from string to their respective data type
        for i in range(11):
            # We check it first if it's not empty we processed th data 
            if ((data[i]).__sizeof__() != 49):
                # If we reached mileage, treat is as float and do processing on it
                if i == 8:
                    conversion = round((float(data[i]) * 1000.001), 3)
                    processed.append(conversion)
                    continue # Move to next iteration
                conversion = int(data[i])
                processed.append(conversion)
            else:
                # We simply fill 'Empty'
                conversion = ''
                processed.append(conversion)
    
    # Now we check if we truly have empty entries back in player_data tab
    if (data[data_count] != 294):
        player_data = (
            json_data.get("root", {})
            .get("properties", {})
            .get("user_info_0", {})
            .get("Struct", {})
            .get("Struct", {})
        )

        # Buffer CP, BP, MaxCP, TotalMileage, Acc.CP, Garage 
        for i, (key, data_type) in enumerate(constants.SET_WRITE_PLAYER_KEY):
            if data[i]:
                player_data[key][data_type] = processed[i]

        with open(constants.TMP_PATH, "w", encoding="utf-8") as file:
            json.dump(json_data, file, indent=2)

        load_json()

        del processed, data, conversion

# Increment player ar counter
def increment_player_car_count(id: int) -> int:
    id = id + 1 
    global json_data

    counter_data = (
            json_data.get("root", {})
            .get("properties", {})
            .get("user_info_0", {})
            .get("Struct", {})
            .get("Struct", {})
            .get("MyCarIdSrc_0", {})
        )
    
    counter_data["Int"] = id
    with open(constants.TMP_PATH, "w", encoding="utf-8") as file:
        json.dump(json_data, file, indent=2)

    return id

def set_vehicle_upgrade(data: list[str | int], id: int) -> None:
    global json_data

    if (id != 0):
        org_data = get_selected_car_upgrades(id)

        processed = []
        # Refactoring here, range max = i - 1
        for i in range(3, 15):
            # We will append everything as intended
            converted = constants.LEVEL_RAW_STRINGS[constants.LEVEL_STRINGS.index(data[i])]
            processed.append(converted)

        # We check whether it is empty or not
        if (data[0]):
            processed.append(data[0])   # Add chassis code
        else:
            processed.append('')   # Placeholder, duh

        # Engine Swap
        if (data[1]):
            processed.append(data[1])

        # We check whether it is empty or not
        if (data[2]):
            processed.append(data[2])   # Add Aura
        else:
            processed.append('')   # Placeholder, duh

        if (data[15]):
            processed.append(float(data[15]))  # Add mileage
        else:
            processed.append('')   # Placeholder, duh

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
        current_car = current_car["value"]["Struct"]["Struct"]

        for tunes in current_car["TuneInfos_0"]["Map"]:
            # we collect each upgrades level, and append them as list
            for i, value in enumerate(constants.UPGRADES_RAW_STRINGS, start=0):
                if tunes["key"]["Enum"] == constants.UPGRADES_RAW_STRINGS[i]:
                    tunes["value"]["Struct"]["Struct"]["EquipLevel_0"]["Enum"] = processed[i]
        
        if (data[0]):
            current_car["CarNameId_0"]["Name"] = processed[12]
        
        # Engine Swap
        if (data[1]):
            current_car["EngineNameId_0"]["Name"] = processed[13]
            if (processed[13] != None or data[0]):
                current_car["IsReplacedEngine_0"]["Bool"] = True
            else:
                current_car["IsReplacedEngine_0"]["Bool"] = False

        if processed[14]:
            current_car["Effect_0"]["Struct"]["Struct"]["AuraNameId_0"]["Name"] = processed[14]

        if (data[15]):
            current_car["Mileages_0"]["Double"] = processed[15]

    with open(constants.TMP_PATH, "w", encoding="utf-8") as file:
            json.dump(json_data, file, indent=2)
    
    load_json()
    
    # Just freeing memory
    del processed, converted, org_data, i

def rm_vehicle(id) -> None:
    global json_data

    if (id != 0):
        my_cars = (
            json_data.get("root", {})
            .get("properties", {})
            .get("user_info_0", {})
            .get("Struct", {})
            .get("Struct", {})
            .get("MyCars_0", {})
            .get("Map", [])
        )

        for i, entry in enumerate(my_cars):
            if entry.get("key", {}).get("Int") == id:
                rm = my_cars.pop(i)
                break
        
        with open(constants.TMP_PATH, "w", encoding="utf-8") as file:
            json.dump(json_data, file, indent=2)

def add_vehicles(id: str, chassis: str) -> None:
    global json_data

    temp_car = constants.PLC_TEMPLATE

    temp_car["key"]["Int"] = id
    temp_car["value"]["Struct"]["Struct"]["CarNameId_0"]["Name"] = chassis
    temp_car["value"]["Struct"]["Struct"]["EngineNameId_0"]["Name"] = chassis

    my_cars = (
        json_data.get("root", {})
        .get("properties", {})
        .get("user_info_0", {})
        .get("Struct", {})
        .get("Struct", {})
        .get("MyCars_0", {})
        .get("Map", [])
    )

    my_cars.append(temp_car)

    with open(constants.TMP_PATH, "w", encoding="utf-8") as file:
        json.dump(json_data, file, indent=2)
    
    load_json()

def set_vehicle_preset(car: list) -> str:
    global json_data

    # ID refer to our selected car to apply the patch
    id = car[0]

    # Load preset file
    car_preset = filedialog.askopenfilename(filetypes=[('TXR 25 Car Preset File', '*.sb25_preset'),
                                                             ('All Files', '*.*')]).replace("\\","/")
    
    if car_preset:
        # Load preset file
        with open(car_preset, "r", encoding="utf-8") as preset_data:
            car_preset = json.load(preset_data)
    
        selected_car = (
                json_data.get("root", {})
                .get("properties", {})
                .get("user_info_0", {})
                .get("Struct", {})
                .get("Struct", {})
                .get("MyCars_0", {})
                .get("Map", [])
            )
        
        current_car = next((car for car in selected_car if car["key"]["Int"] == id), None)
        current_car = current_car["value"]["Struct"]["Struct"]

        if current_car:
            current_car["Paint_0"] = car_preset["Paint_0"]
            current_car["BodyStickers_0"] = car_preset["BodyStickers_0"]
            current_car["RearWingStickers_0"] = car_preset["RearWingStickers_0"]
            current_car["WindowStickers_0"] = car_preset["WindowStickers_0"]
            current_car["FrontBrake_0"] = car_preset["FrontBrake_0"]
            current_car["RearBrake_0"] = car_preset["RearBrake_0"]
            current_car["FrontTire_0"] = car_preset["FrontTire_0"]
            current_car["RearTire_0"] = car_preset["RearTire_0"]
            current_car["FrontWheelInfo_0"] = car_preset["FrontWheelInfo_0"]
            current_car["RearWheelInfo_0"] = car_preset["RearWheelInfo_0"]
            current_car["DressUpInfo_0"] = car_preset["DressUpInfo_0"]
            current_car["EngineNameId_0"] = car_preset["EngineNameId_0"]
            current_car["IsReplacedEngine_0"] = car_preset["IsReplacedEngine_0"]
            current_car["SettingInfo_0"] = car_preset["SettingInfo_0"]
        
        with open(constants.TMP_PATH, "w", encoding="utf-8") as file:
            json.dump(json_data, file, indent=2)
        
        load_json()

    return car_preset

# --- Data Setter ends here  --- #
# --- Helper data getter/setter here  --- #

def check_is_player_data_complete() -> None:
    global json_data

    is_write = False
    player_data = (
        json_data.get("root", {})
        .get("properties", {})
        .get("user_info_0", {})
        .get("Struct", {})
        .get("Struct", {})
    )

    if "Cp_0" not in player_data:
        player_data.update(constants.PLJ_CP)
        is_write = True
    
    if "PP_0" not in player_data:
        player_data.update(constants.PLJ_PP)
        is_write = True
    
    if "WinNum_0" not in player_data:
        player_data.update(constants.PLJ_WIN)
        is_write = True

    if "LoseNum_0" not in player_data:
        player_data.update(constants.PLJ_LOSS)
        is_write = True

    if "DrawNum_0" not in player_data:
        player_data.update(constants.PLJ_DRAW)
        is_write = True
    
    if "MaxWiningStreak_0" not in player_data:
        player_data.update(constants.PLJ_WIN_STRK)
        is_write = True

    if "TotalMileages_0" not in player_data:
        player_data.update(constants.PLJ_SUM_MILE)
        is_write = True

    if "CumulativeAcquisitionCP_0" not in player_data:
        player_data.update(constants.PLJ_SUM_CP)
        is_write = True

    if "Day_0" not in player_data:
        player_data.update(constants.PLJ_DAY)
        is_write = True
    
    if is_write:
        with open(constants.TMP_PATH, "w", encoding="utf-8") as file:
            json.dump(json_data, file, indent=2)
        load_json()

        del is_write

# --- Helper data getter/setter ends here  --- #
# ----- uesave-cli processes here ----- #

def sav_to_json(path: str) -> None:
    if path:
        subprocess.run(['./bin/uesave', 'to-json', '-i', f'{path}', '-o', f'{constants.TMP_PATH}'])
        
def json_to_sav(path: str) -> None:
    if path:
        subprocess.run([f'./bin/uesave', 'from-json', '-i', f'{constants.TMP_PATH}', '-o', f'{path}'])