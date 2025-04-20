VERSION = "1.1.1"
MAIN_AUTHOR = "rafli.ard23"

TMP_PATH = "./bin/tmp/tmp.json"

STATUS_STRINGS = ["Max CP", "CP", "Accumulated CP",
                  "BP", "Win", "Loss", "Draw",
                  "Win Streak", "Total Mileage", 
                  "Day", "Garage Size", "Owned Cars"]

UPGRADES_STRINGS = ["Chassis Code", "Power Unit", "Intake",
                    "Exhaust", "Transmission", "Clutch",
                    "Suspension", "Brake", "Body", 
                    "Front Tires", "Rear Tires", "LSD",
                    "Nitro", "Mileages (km)"]

UPGRADES_RAW_STRINGS = ["EVehicleTuneKind::PowerUnit", "EVehicleTuneKind::IntakeSystem",
                        "EVehicleTuneKind::ExhaustSystem", "EVehicleTuneKind::Transmission",
                        "EVehicleTuneKind::Clutch", "EVehicleTuneKind::Suspension",
                        "EVehicleTuneKind::Brake", "EVehicleTuneKind::Body",
                        "EVehicleTuneKind::FrontTire", "EVehicleTuneKind::RearTire",
                        "EVehicleTuneKind::LSD", "EVehicleTuneKind::Nitro"]

PLAYER_STRINGS = STATUS_STRINGS[:11]

LEVEL_STRINGS = ["Normal", "Level 1",
                 "Level 2", "Level 3",
                 "Level 4", "Level 5",
                 "Level 6", "Level 7",
                 "Level 8", "Level 9" ]

LEVEL_EXH_INTK = LEVEL_STRINGS[:7]

LEVEL_HANDLINGS = LEVEL_STRINGS[:6]

LEVEL_MISC = LEVEL_STRINGS[:4]

LEVEL_RAW_STRINGS = ["EVehicleTuneLevel::Normal", "EVehicleTuneLevel::Level1",
                     "EVehicleTuneLevel::Level2", "EVehicleTuneLevel::Level3",
                     "EVehicleTuneLevel::Level4", "EVehicleTuneLevel::Level5",
                     "EVehicleTuneLevel::Level6", "EVehicleTuneLevel::Level7",
                     "EVehicleTuneLevel::Level8", "EVehicleTuneLevel::Level9"]

SET_WRITE_PLAYER_KEY = [
    ("UpperLimitCP_0", "Int64"),
    ("Cp_0", "Int64"),
    ("CumulativeAcquisitionCP_0", "Int64"),
    ("PP_0", "Int"),
    ("WinNum_0", "Int"),
    ("LoseNum_0", "Int"),
    ("DrawNum_0", "Int"),
    ("MaxWiningStreak_0", "Int"),
    ("TotalMileages_0", "Double"),
    ("Day_0", "Int"),
    ("MaxGarageMyCarNum_0", "Int")
]

# ----- JSON Player Data Template ----- #

PLJ_CP = {
    "Cp_0": {
        "tag": {
          "data": {
            "Other": "Int64Property"
          }
        },
        "Int64": 0
    }
}

PLJ_PP = {
    "PP_0": {
        "tag": {
          "data": {
            "Other": "IntProperty"
          }
        },
        "Int": 0
    }
}

PLJ_WIN = {
    "WinNum_0": {
        "tag": {
          "data": {
            "Other": "IntProperty"
          }
        },
        "Int": 0
    }
}

PLJ_LOSS = {
    "LoseNum_0": {
        "tag": {
          "data": {
            "Other": "IntProperty"
          }
        },
        "Int": 0
    }
}

PLJ_DRAW = {
    "DrawNum_0": {
        "tag": {
          "data": {
            "Other": "IntProperty"
          }
        },
        "Int": 0
    }
}

PLJ_WIN_STRK = {
    "MaxWiningStreak_0": {
        "tag": {
          "data": {
            "Other": "IntProperty"
          }
        },
        "Int": 0
    }
}

# ----- JSON Player Data Template ends here ----- #
# ----- Strings Const ----- #

STR_TT_MAXCP = """
Sum of money you can hold on wallet. Player stats in garage does not reflect \
(edited value) as it checks based on your current wallet perk, the edited \
works properly as edited.\n
Max value should be 2^63-1.
I recommend to cap it 1,000,000,000,000,000
"""

STR_TT_CP = """
Your current money on wallet.\n
Max value should be 2^63-1.
I recommend to cap it 1,000,000,000,000,000
"""

STR_TT_ACCP = """
Sum of your earned money throughout career.\n
Max value should be 2^63-1.
I recommend to cap it 1,000,000,000,000,000
"""

STR_TT_BP = """
Your current perk point.\n
Virtually the max value is 2^16-1 but the display only show you 999 Max
"""

STR_TT_WIN = """
Sum of attained win in career.\n
You can edit as much as you want.
"""

STR_TT_LOSS = """
Sum of attained loss in career.\n
You can edit as much as you want.
"""

STR_TT_DRAW = """
Sum of attained draw in career.\n
You can edit as much as you want.
"""

STR_TT_WSTRK = """
Sum of longest win streak in career.\n
You can edit as much as you want.
"""

STR_TT_TMIL = """
Your total mileage throughout career.\n
Should write the decimal using period/dot (.)
"""

STR_TT_DAY = """
Number of day that has been passed in career.\n
You can edit as much as you want.
"""

STR_TT_GRGSIZE = """
Number of maximum cars your garage can contain.\n
You can edit as much as you want.
"""

STR_TT_PLYR_CONST = [
    STR_TT_MAXCP,
    STR_TT_CP,
    STR_TT_ACCP,
    STR_TT_BP,
    STR_TT_WIN,
    STR_TT_LOSS,
    STR_TT_DRAW,
    STR_TT_WSTRK,
    STR_TT_TMIL,
    STR_TT_DAY,
    STR_TT_GRGSIZE
]