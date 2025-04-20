# Tokyo Xtreme Racer - Save Editor

<img src="https://raw.githubusercontent.com/rafliard23/txr-use-py/refs/heads/main/img/txr_use-main_banner.png">

Yet, another Save Game editor for Tokyo Xtreme Racer.

Another Educational tool that I made for acquiring player data. At the moment, the current scope is limited to player data and owned vehicle data.

## Dependencies
+ ### Python 3.10
+ ### [TomSchimansky/CustomTkinter](https://github.com/TomSchimansky/CustomTkinter)  
+ ### [trumank/uesave-rs [CLI Tool]](https://github.com/trumank/uesave-rs)

## Installation

### Python
You can run this project simply by clone this project, install dependencies, for ```uesave.exe``` need to be installed in ```{project_dir}/bin```, and make new dir ```{project_dir}/bin/temp```, and run the app ```gui.py```

### Binary
You can download packaged version of the program in [Releases](https://github.com/rafliard23/txr-use-py/releases/). To run the app, extract the files and start the ```txr_use.exe```

## Functionality
This save game editor lets you edit several parts of user' data that contained in the game' save file. As of Early Access version of the game, this tool capable to edit player stats and adjust player' car performance upgrades from the simple GUI.

### Graphical User Interface
GUI makes it everyone can use this tool without tinkering with terminal/command prompt and automated file processing.

### Automatic Backup
The app automate backup process of your unmodified save file before saving new changes when you save the edit.  
Backup file located in `%LOCALAPPDATA%/TokyoXtremeRacer/Saved/USE_Save_Backup/`.  
Backup save file stored as `UserData_00.sav.bak`. To revert your save file after an edit, simply delete the `.bak` extension and replace your save file from the backup directory.

### Player Stats Edit

<img src="https://raw.githubusercontent.com/rafliard23/txr-use-py/refs/heads/main/img/txr_use-player_data.png"  width="650">

While in theory you can almost edit any value that exposed in UserData_00.sav, I limited (vars that can be edited) to several variables to encourage players play the game as intended. Variables that included in my Save Editor are the following:
- Max Money (Working, the displayed value on player garage shows your current Wallet perk value, just ignore it)
- Money (CP)
- Accumulated money (Acc. CP)
- BP point
- Win count
- Loss count
- Draw count
- Win streak count
- Player' total mileage
- Day counter
- Garage size

### Vehicle Performance Upgrades

<img src="https://raw.githubusercontent.com/rafliard23/txr-use-py/refs/heads/main/img/txr_use-vehicle_upgrades.png"  width="650">

Based on tested and dump data, we know maximum upgrades levels for each type, then I tried to write the current owned upgrade levels into something player desired. Car' mileage also added (in case you want to quickly finish certain wanderers).

All vehicle upgrades type and car' mileage data are editable. Car (chassis) swap is possible!

- Tune part upgrade
- Vehicle chassis swap
- Vehicle mileage

### Tooltip

<img src="https://raw.githubusercontent.com/rafliard23/txr-use-py/refs/heads/main/img/txr_use-tooltip.gif"  width="650">

In addition for separate wiki, in-app now also feature tooltip for quick help for editing values.

## Disclaimer
- To ensure minimal damage, always make a backup before processing a file.
- This software released purely for educational purpose. Author is not responsible for any damage outside of intended purpose of this software.
- This software has no affiliation with Tokyo Xtreme Racer (2025), or Genki Co., Ltd.
