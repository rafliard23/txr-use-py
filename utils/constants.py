VERSION = "0.9-beta"
MAIN_AUTHOR = "rafli.ard23"

TMP_PATH = "./bin/tmp/tmp.json"

STATUS_STRINGS = ["Max CP", "CP", "BP", "Win", 
                  "Loss", "Draw", "Win Streak",
                  "Total Mileage","Accumulated CP",
                  "Garage Size", "Owned Cars"]

UPGRADES_STRINGS = ["Power Unit", "Intake", "Exhaust",
                    "Transmission", "Clutch", "Suspension",
                    "Brake", "Body", "Tires",
                    "LSD", "Nitro", "Mileages (km)"]

UPGRADES_RAW_STRINGS = ["EVehicleTuneKind::PowerUnit", "EVehicleTuneKind::IntakeSystem",
                        "EVehicleTuneKind::ExhaustSystem", "EVehicleTuneKind::Transmission",
                        "EVehicleTuneKind::Clutch", "EVehicleTuneKind::Suspension",
                        "EVehicleTuneKind::Brake", "EVehicleTuneKind::Body",
                        "EVehicleTuneKind::FrontTire", "EVehicleTuneKind::RearTire",
                        "EVehicleTuneKind::LSD", "EVehicleTuneKind::Nitro"]

PLAYER_STRINGS = ["Max CP", "CP", "BP",
                  "Total Mileage",
                  "Accumulated CP",
                  "Garage Size"]

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