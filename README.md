# Tokyo Xtreme Racer - Save Editor

![TXR Save Editor](https://github.com/rafliard23/txr-livery-editor-py/blob/main/img/livery_tool-gui.png)

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

### Player Stats Edit
While in theory you can almost edit any value that exposed in UserData_00.sav, I limited (vars that can be edited) to several vars to encourage players play the game as intended. Variables that included in my Save Editor are the following:
- Max Money (Working, the displayed value on player garage shows your current Wallet perk value, just ignore it)
- Money (CP)
- BP Point
- Player' total mileage
- Accumulated Money (Acc. CP)
- Garage Size

### Vehicle Performance Upgrades
Based on tested and dump data, we know maximum upgrades levels for each type, then I tried to write the current owned upgrade levels into something player desired. Car' mileage also added (in case you want to quickly finish certain wanderers).

All vehicle upgrades type and car' mileage data are editable.

### Graphical User Interface
GUI makes it everyone can use this tool without tinkering with terminal/command prompt and automated file processing.

## Disclaimer
- To ensure minimal damage, always make a backup before processing a file.
- This software released purely for educational purpose. Author is not responsible for any damage outside of intended purpose of this software.
- This software has no affiliation with Tokyo Xtreme Racer (2025), or Genki Co., Ltd.