VERSION = "1.2.0"
MAIN_AUTHOR = "Credits: \n\
trumank⠀\t - uesave-cli \n\
TomSchimansky \t - CustomTkinter \n\
rafli.ard23 \t - App creator"

TMP_PATH = "./bin/tmp/tmp.json"

STATUS_STRINGS = ["Max CP", "CP", "Accumulated CP",
                  "BP", "Win", "Loss", "Draw",
                  "Win Streak", "Total Mileage", 
                  "Day", "Garage Size", "Owned Cars"]

UPGRADES_STRINGS = ["Chassis Code", "Engine Swap", "Aura",
                    "Power Unit", "Intake",
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

PLJ_CP = {"Cp_0":{"tag":{"data":{"Other":"Int64Property"}},"Int64":0}}

PLJ_PP = {"PP_0":{"tag":{"data":{"Other":"IntProperty"}},"Int":0}}

PLJ_WIN = {"WinNum_0":{"tag":{"data":{"Other":"IntProperty"}},"Int":0}}

PLJ_LOSS = {"LoseNum_0":{"tag":{"data":{"Other":"IntProperty"}},"Int":0}}

PLJ_DRAW = {"DrawNum_0":{"tag":{"data":{"Other":"IntProperty"}},"Int":0}}

PLJ_WIN_STRK = {"MaxWiningStreak_0":{"tag":{"data":{"Other":"IntProperty"}},"Int":0}}

PLJ_SUM_MILE = {"TotalMileages_0":{"tag":{"data":{"Other":"DoubleProperty"}},"Double":0}}

PLJ_SUM_CP = {"CumulativeAcquisitionCP_0":{"tag":{"data":{"Other":"Int64Property"}},"Int64":0}}

PLJ_DAY = {"Day_0":{"tag":{"data":{"Other":"IntProperty"}},"Int":0}}

# JSON Player Perk Template

PLPJ_AURA = {"key":{"Enum":"ESkillTreeType::STT_AURA"},"value":{"Struct":{"Struct":{"Level_0":{"tag":{"data":{"Other":"IntProperty"}},"Int":0},"CategoryName_0":{"tag":{"data":{"Other":"NameProperty"}},"Name":"PerkOncome"},"RowName_0":{"tag":{"data":{"Other":"NameProperty"}},"Name":"Perk_enable_aura"}}}}}

PLPJ_EG_SWAP = {"key":{"Enum":"ESkillTreeType::STT_ENABLE_ENGINE_REPLACEMENT"},"value":{"Struct":{"Struct":{"Level_0":{"tag":{"data":{"Other":"IntProperty"}},"Int":0},"CategoryName_0":{"tag":{"data":{"Other":"NameProperty"}},"Name":"PerkOncome"},"RowName_0":{"tag":{"data":{"Other":"NameProperty"}},"Name":"Perk_enable_engine_replacement"}}}}}


# JSON Car Template

PLC_TEMPLATE = {"key":{"Int":1},"value":{"Struct":{"Struct":{"CarNameId_0":{"tag":{"data":{"Other":"NameProperty"}},"Name":"AE86L"},"EngineNameId_0":{"tag":{"data":{"Other":"NameProperty"}},"Name":"AE86L"},"IsReplacedEngine_0":{"tag":{"data":{"Other":"BoolProperty"}},"Bool":False},"ReplacementEngines_0":{"tag":{"data":{"Map":{"key_type":{"Other":"NameProperty"},"value_type":{"Struct":{"struct_type":{"Struct":"/Script/TokyoXtremeRacer.SMyEngineReplacementInfo"},"id":"00000000-0000-0000-0000-000000000000"}}}}},"Map":[]},"Mileages_0":{"tag":{"data":{"Other":"DoubleProperty"}},"Double":0},"MaxSpeed_0":{"tag":{"data":{"Other":"FloatProperty"}},"Float":0},"TuneInfos_0":{"tag":{"data":{"Map":{"key_type":{"Enum":["/Script/TokyoXtremeRacer.EVehicleTuneKind","ByteProperty"]},"value_type":{"Struct":{"struct_type":{"Struct":"/Script/TokyoXtremeRacer.STuneInfo"},"id":"00000000-0000-0000-0000-000000000000"}}}}},"Map":[{"key":{"Enum":"EVehicleTuneKind::PowerUnit"},"value":{"Struct":{"Struct":{"HaveFlags_0":{"tag":{"data":{"Other":"IntProperty"}},"Int":1},"EquipLevel_0":{"tag":{"data":{"Enum":["/Script/TokyoXtremeRacer.EVehicleTuneLevel","ByteProperty"]}},"Enum":"EVehicleTuneLevel::Normal"},"TunerEffect_0":{"tag":{"data":{"Other":"BoolProperty"}},"Bool":False}}}}},{"key":{"Enum":"EVehicleTuneKind::IntakeSystem"},"value":{"Struct":{"Struct":{"HaveFlags_0":{"tag":{"data":{"Other":"IntProperty"}},"Int":1},"EquipLevel_0":{"tag":{"data":{"Enum":["/Script/TokyoXtremeRacer.EVehicleTuneLevel","ByteProperty"]}},"Enum":"EVehicleTuneLevel::Normal"},"TunerEffect_0":{"tag":{"data":{"Other":"BoolProperty"}},"Bool":False}}}}},{"key":{"Enum":"EVehicleTuneKind::ExhaustSystem"},"value":{"Struct":{"Struct":{"HaveFlags_0":{"tag":{"data":{"Other":"IntProperty"}},"Int":1},"EquipLevel_0":{"tag":{"data":{"Enum":["/Script/TokyoXtremeRacer.EVehicleTuneLevel","ByteProperty"]}},"Enum":"EVehicleTuneLevel::Normal"},"TunerEffect_0":{"tag":{"data":{"Other":"BoolProperty"}},"Bool":False}}}}},{"key":{"Enum":"EVehicleTuneKind::Transmission"},"value":{"Struct":{"Struct":{"HaveFlags_0":{"tag":{"data":{"Other":"IntProperty"}},"Int":1},"EquipLevel_0":{"tag":{"data":{"Enum":["/Script/TokyoXtremeRacer.EVehicleTuneLevel","ByteProperty"]}},"Enum":"EVehicleTuneLevel::Normal"},"TunerEffect_0":{"tag":{"data":{"Other":"BoolProperty"}},"Bool":False}}}}},{"key":{"Enum":"EVehicleTuneKind::Clutch"},"value":{"Struct":{"Struct":{"HaveFlags_0":{"tag":{"data":{"Other":"IntProperty"}},"Int":1},"EquipLevel_0":{"tag":{"data":{"Enum":["/Script/TokyoXtremeRacer.EVehicleTuneLevel","ByteProperty"]}},"Enum":"EVehicleTuneLevel::Normal"},"TunerEffect_0":{"tag":{"data":{"Other":"BoolProperty"}},"Bool":False}}}}},{"key":{"Enum":"EVehicleTuneKind::Suspension"},"value":{"Struct":{"Struct":{"HaveFlags_0":{"tag":{"data":{"Other":"IntProperty"}},"Int":1},"EquipLevel_0":{"tag":{"data":{"Enum":["/Script/TokyoXtremeRacer.EVehicleTuneLevel","ByteProperty"]}},"Enum":"EVehicleTuneLevel::Normal"},"TunerEffect_0":{"tag":{"data":{"Other":"BoolProperty"}},"Bool":False}}}}},{"key":{"Enum":"EVehicleTuneKind::Brake"},"value":{"Struct":{"Struct":{"HaveFlags_0":{"tag":{"data":{"Other":"IntProperty"}},"Int":1},"EquipLevel_0":{"tag":{"data":{"Enum":["/Script/TokyoXtremeRacer.EVehicleTuneLevel","ByteProperty"]}},"Enum":"EVehicleTuneLevel::Normal"},"TunerEffect_0":{"tag":{"data":{"Other":"BoolProperty"}},"Bool":False}}}}},{"key":{"Enum":"EVehicleTuneKind::Body"},"value":{"Struct":{"Struct":{"HaveFlags_0":{"tag":{"data":{"Other":"IntProperty"}},"Int":1},"EquipLevel_0":{"tag":{"data":{"Enum":["/Script/TokyoXtremeRacer.EVehicleTuneLevel","ByteProperty"]}},"Enum":"EVehicleTuneLevel::Normal"},"TunerEffect_0":{"tag":{"data":{"Other":"BoolProperty"}},"Bool":False}}}}},{"key":{"Enum":"EVehicleTuneKind::FrontTire"},"value":{"Struct":{"Struct":{"HaveFlags_0":{"tag":{"data":{"Other":"IntProperty"}},"Int":1},"EquipLevel_0":{"tag":{"data":{"Enum":["/Script/TokyoXtremeRacer.EVehicleTuneLevel","ByteProperty"]}},"Enum":"EVehicleTuneLevel::Normal"},"TunerEffect_0":{"tag":{"data":{"Other":"BoolProperty"}},"Bool":False}}}}},{"key":{"Enum":"EVehicleTuneKind::RearTire"},"value":{"Struct":{"Struct":{"HaveFlags_0":{"tag":{"data":{"Other":"IntProperty"}},"Int":1},"EquipLevel_0":{"tag":{"data":{"Enum":["/Script/TokyoXtremeRacer.EVehicleTuneLevel","ByteProperty"]}},"Enum":"EVehicleTuneLevel::Normal"},"TunerEffect_0":{"tag":{"data":{"Other":"BoolProperty"}},"Bool":False}}}}},{"key":{"Enum":"EVehicleTuneKind::LSD"},"value":{"Struct":{"Struct":{"HaveFlags_0":{"tag":{"data":{"Other":"IntProperty"}},"Int":1},"EquipLevel_0":{"tag":{"data":{"Enum":["/Script/TokyoXtremeRacer.EVehicleTuneLevel","ByteProperty"]}},"Enum":"EVehicleTuneLevel::Normal"},"TunerEffect_0":{"tag":{"data":{"Other":"BoolProperty"}},"Bool":False}}}}},{"key":{"Enum":"EVehicleTuneKind::Nitro"},"value":{"Struct":{"Struct":{"HaveFlags_0":{"tag":{"data":{"Other":"IntProperty"}},"Int":1},"EquipLevel_0":{"tag":{"data":{"Enum":["/Script/TokyoXtremeRacer.EVehicleTuneLevel","ByteProperty"]}},"Enum":"EVehicleTuneLevel::Normal"},"TunerEffect_0":{"tag":{"data":{"Other":"BoolProperty"}},"Bool":False}}}}}]},"SettingInfo_0":{"tag":{"data":{"Struct":{"struct_type":{"Struct":"/Script/TokyoXtremeRacer.SCarSettingInfo"},"id":"00000000-0000-0000-0000-000000000000"}}},"Struct":{"Struct":{"transmission_0":{"tag":{"data":{"Struct":{"struct_type":{"Struct":"/Script/TokyoXtremeRacer.SCarSettingTransmissionInfo"},"id":"00000000-0000-0000-0000-000000000000"}}},"Struct":{"Struct":{"NumberOfGears_0":{"tag":{"data":{"Other":"IntProperty"}},"Int":5},"ReverseGearRatio_0":{"tag":{"data":{"Other":"FloatProperty"}},"Float":3.484},"FinalGearRatio_0":{"tag":{"data":{"Other":"FloatProperty"}},"Float":4.3},"GearRatios_0":{"tag":{"data":{"Array":{"Other":"FloatProperty"}}},"Array":{"Base":{"Float":[3.587,2.022,1.384,1,0.861]}}}}}},"Settings_0":{"tag":{"data":{"Map":{"key_type":{"Enum":["/Script/TokyoXtremeRacer.ECarSetting","ByteProperty"]},"value_type":{"Other":"IntProperty"}}}},"Map":[{"key":{"Enum":"ECarSetting::LSDRearInitialTorque"},"value":{"Int":5}},{"key":{"Enum":"ECarSetting::LSDRearRatio"},"value":{"Int":5}},{"key":{"Enum":"ECarSetting::CamberFront"},"value":{"Int":0}},{"key":{"Enum":"ECarSetting::CamberRear"},"value":{"Int":0}},{"key":{"Enum":"ECarSetting::ToeFront"},"value":{"Int":0}},{"key":{"Enum":"ECarSetting::ToeRear"},"value":{"Int":0}},{"key":{"Enum":"ECarSetting::SpringFront"},"value":{"Int":0}},{"key":{"Enum":"ECarSetting::SpringRear"},"value":{"Int":0}},{"key":{"Enum":"ECarSetting::DumperFront"},"value":{"Int":0}},{"key":{"Enum":"ECarSetting::DumperRear"},"value":{"Int":0}},{"key":{"Enum":"ECarSetting::DumperBalanceFront"},"value":{"Int":50}},{"key":{"Enum":"ECarSetting::DumperBalanceRear"},"value":{"Int":50}},{"key":{"Enum":"ECarSetting::StabilizerFront"},"value":{"Int":0}},{"key":{"Enum":"ECarSetting::StabilizerRear"},"value":{"Int":0}},{"key":{"Enum":"ECarSetting::RideHeightFront"},"value":{"Int":0}},{"key":{"Enum":"ECarSetting::RideHeightRear"},"value":{"Int":0}},{"key":{"Enum":"ECarSetting::Downforce"},"value":{"Int":0}},{"key":{"Enum":"ECarSetting::BrakeBalaneFront"},"value":{"Int":0}},{"key":{"Enum":"ECarSetting::BrakeBalaneRear"},"value":{"Int":0}},{"key":{"Enum":"ECarSetting::TractionControl"},"value":{"Int":0}},{"key":{"Enum":"ECarSetting::ABS"},"value":{"Int":1}},{"key":{"Enum":"ECarSetting::OffsetFront"},"value":{"Int":0}},{"key":{"Enum":"ECarSetting::OffsetRear"},"value":{"Int":0}},{"key":{"Enum":"ECarSetting::LSDTypeRear"},"value":{"Int":0}},{"key":{"Enum":"ECarSetting::TCS"},"value":{"Int":1}},{"key":{"Enum":"ECarSetting::Num"},"value":{"Int":0}}]},"AutoSettings_0":{"tag":{"data":{"Map":{"key_type":{"Enum":["/Script/TokyoXtremeRacer.ECarSettingAutoKind","ByteProperty"]},"value_type":{"Enum":["/Script/TokyoXtremeRacer.ECarSettingAutoType","ByteProperty"]}}}},"Map":[{"key":{"Enum":"ECarSettingAutoKind::Speed"},"value":{"Enum":"ECarSettingAutoType::None"}},{"key":{"Enum":"ECarSettingAutoKind::Handling"},"value":{"Enum":"ECarSettingAutoType::None"}},{"key":{"Enum":"ECarSettingAutoKind::BrakeBalance"},"value":{"Enum":"ECarSettingAutoType::None"}}]}}}},"NewSettingInfo_0":{"tag":{"data":{"Array":{"Enum":["/Script/TokyoXtremeRacer.ECarSetting","ByteProperty"]}}},"Array":{"Base":{"Enum":[]}}},"AlreadyNewSettingInfo_0":{"tag":{"data":{"Array":{"Enum":["/Script/TokyoXtremeRacer.ECarSetting","ByteProperty"]}}},"Array":{"Base":{"Enum":[]}}},"Paint_0":{"tag":{"data":{"Struct":{"struct_type":{"Struct":"/Script/TokyoXtremeRacer.SCarPaint"},"id":"00000000-0000-0000-0000-000000000000"}}},"Struct":{"Struct":{"IsGenuine_0":{"tag":{"data":{"Other":"BoolProperty"}},"Bool":True},"MainBodyColor_0":{"tag":{"data":{"Other":"IntProperty"}},"Int":2},"SubBodyColor_0":{"tag":{"data":{"Other":"IntProperty"}},"Int":-1},"MainColor_0":{"tag":{"data":{"Struct":{"struct_type":{"Struct":"/Script/TokyoXtremeRacer.SCarPaintColor"},"id":"00000000-0000-0000-0000-000000000000"}}},"Struct":{"Struct":{"IsEnable_0":{"tag":{"data":{"Other":"BoolProperty"}},"Bool":False},"Color_0":{"tag":{"data":{"Struct":{"struct_type":"LinearColor","id":"00000000-0000-0000-0000-000000000000"}}},"Struct":{"LinearColor":{"r":1,"g":1,"b":1,"a":1}}},"Color_Metal_0":{"tag":{"data":{"Other":"FloatProperty"}},"Float":0},"Color_Mat_0":{"tag":{"data":{"Other":"FloatProperty"}},"Float":0}}}},"SubColor_0":{"tag":{"data":{"Struct":{"struct_type":{"Struct":"/Script/TokyoXtremeRacer.SCarPaintColor"},"id":"00000000-0000-0000-0000-000000000000"}}},"Struct":{"Struct":{"IsEnable_0":{"tag":{"data":{"Other":"BoolProperty"}},"Bool":False},"Color_0":{"tag":{"data":{"Struct":{"struct_type":"LinearColor","id":"00000000-0000-0000-0000-000000000000"}}},"Struct":{"LinearColor":{"r":1,"g":1,"b":1,"a":1}}},"Color_Metal_0":{"tag":{"data":{"Other":"FloatProperty"}},"Float":0},"Color_Mat_0":{"tag":{"data":{"Other":"FloatProperty"}},"Float":0}}}}}}},"DressUpInfo_0":{"tag":{"data":{"Map":{"key_type":{"Enum":["/Script/TokyoXtremeRacer.ECustomCarPartsKind","ByteProperty"]},"value_type":{"Struct":{"struct_type":{"Struct":"/Script/TokyoXtremeRacer.SCustomCarParts"},"id":"00000000-0000-0000-0000-000000000000"}}}}},"Map":[{"key":{"Enum":"ECustomCarPartsKind::Muffler"},"value":{"Struct":{"Struct":{"EquipType_0":{"tag":{"data":{"Enum":["/Script/TokyoXtremeRacer.ECustomCarPartsType","ByteProperty"]}},"Enum":"ECustomCarPartsType::Normal"},"HaveTypes_0":{"tag":{"data":{"Array":{"Enum":["/Script/TokyoXtremeRacer.ECustomCarPartsType","ByteProperty"]}}},"Array":{"Base":{"Enum":["ECustomCarPartsType::Normal"]}}}}}}},{"key":{"Enum":"ECustomCarPartsKind::FrontBumper"},"value":{"Struct":{"Struct":{"EquipType_0":{"tag":{"data":{"Enum":["/Script/TokyoXtremeRacer.ECustomCarPartsType","ByteProperty"]}},"Enum":"ECustomCarPartsType::Normal"},"HaveTypes_0":{"tag":{"data":{"Array":{"Enum":["/Script/TokyoXtremeRacer.ECustomCarPartsType","ByteProperty"]}}},"Array":{"Base":{"Enum":["ECustomCarPartsType::Normal"]}}}}}}},{"key":{"Enum":"ECustomCarPartsKind::RearBumper"},"value":{"Struct":{"Struct":{"EquipType_0":{"tag":{"data":{"Enum":["/Script/TokyoXtremeRacer.ECustomCarPartsType","ByteProperty"]}},"Enum":"ECustomCarPartsType::Normal"},"HaveTypes_0":{"tag":{"data":{"Array":{"Enum":["/Script/TokyoXtremeRacer.ECustomCarPartsType","ByteProperty"]}}},"Array":{"Base":{"Enum":["ECustomCarPartsType::Normal"]}}}}}}},{"key":{"Enum":"ECustomCarPartsKind::SideSkirt"},"value":{"Struct":{"Struct":{"EquipType_0":{"tag":{"data":{"Enum":["/Script/TokyoXtremeRacer.ECustomCarPartsType","ByteProperty"]}},"Enum":"ECustomCarPartsType::Normal"},"HaveTypes_0":{"tag":{"data":{"Array":{"Enum":["/Script/TokyoXtremeRacer.ECustomCarPartsType","ByteProperty"]}}},"Array":{"Base":{"Enum":["ECustomCarPartsType::Normal"]}}}}}}},{"key":{"Enum":"ECustomCarPartsKind::Bonnet"},"value":{"Struct":{"Struct":{"EquipType_0":{"tag":{"data":{"Enum":["/Script/TokyoXtremeRacer.ECustomCarPartsType","ByteProperty"]}},"Enum":"ECustomCarPartsType::Normal"},"HaveTypes_0":{"tag":{"data":{"Array":{"Enum":["/Script/TokyoXtremeRacer.ECustomCarPartsType","ByteProperty"]}}},"Array":{"Base":{"Enum":["ECustomCarPartsType::Normal"]}}}}}}},{"key":{"Enum":"ECustomCarPartsKind::RearSpoiler"},"value":{"Struct":{"Struct":{"EquipType_0":{"tag":{"data":{"Enum":["/Script/TokyoXtremeRacer.ECustomCarPartsType","ByteProperty"]}},"Enum":"ECustomCarPartsType::Normal"},"HaveTypes_0":{"tag":{"data":{"Array":{"Enum":["/Script/TokyoXtremeRacer.ECustomCarPartsType","ByteProperty"]}}},"Array":{"Base":{"Enum":["ECustomCarPartsType::Normal"]}}}}}}},{"key":{"Enum":"ECustomCarPartsKind::Front_Wheel"},"value":{"Struct":{"Struct":{"EquipType_0":{"tag":{"data":{"Enum":["/Script/TokyoXtremeRacer.ECustomCarPartsType","ByteProperty"]}},"Enum":"ECustomCarPartsType::Normal"},"HaveTypes_0":{"tag":{"data":{"Array":{"Enum":["/Script/TokyoXtremeRacer.ECustomCarPartsType","ByteProperty"]}}},"Array":{"Base":{"Enum":["ECustomCarPartsType::Normal"]}}}}}}},{"key":{"Enum":"ECustomCarPartsKind::Rear_Wheel"},"value":{"Struct":{"Struct":{"EquipType_0":{"tag":{"data":{"Enum":["/Script/TokyoXtremeRacer.ECustomCarPartsType","ByteProperty"]}},"Enum":"ECustomCarPartsType::Normal"},"HaveTypes_0":{"tag":{"data":{"Array":{"Enum":["/Script/TokyoXtremeRacer.ECustomCarPartsType","ByteProperty"]}}},"Array":{"Base":{"Enum":["ECustomCarPartsType::Normal"]}}}}}}},{"key":{"Enum":"ECustomCarPartsKind::FL_BrakeCaliper"},"value":{"Struct":{"Struct":{"EquipType_0":{"tag":{"data":{"Enum":["/Script/TokyoXtremeRacer.ECustomCarPartsType","ByteProperty"]}},"Enum":"ECustomCarPartsType::Normal"},"HaveTypes_0":{"tag":{"data":{"Array":{"Enum":["/Script/TokyoXtremeRacer.ECustomCarPartsType","ByteProperty"]}}},"Array":{"Base":{"Enum":["ECustomCarPartsType::Normal"]}}}}}}},{"key":{"Enum":"ECustomCarPartsKind::FR_BrakeCaliper"},"value":{"Struct":{"Struct":{"EquipType_0":{"tag":{"data":{"Enum":["/Script/TokyoXtremeRacer.ECustomCarPartsType","ByteProperty"]}},"Enum":"ECustomCarPartsType::Normal"},"HaveTypes_0":{"tag":{"data":{"Array":{"Enum":["/Script/TokyoXtremeRacer.ECustomCarPartsType","ByteProperty"]}}},"Array":{"Base":{"Enum":["ECustomCarPartsType::Normal"]}}}}}}},{"key":{"Enum":"ECustomCarPartsKind::RL_BrakeCaliper"},"value":{"Struct":{"Struct":{"EquipType_0":{"tag":{"data":{"Enum":["/Script/TokyoXtremeRacer.ECustomCarPartsType","ByteProperty"]}},"Enum":"ECustomCarPartsType::Normal"},"HaveTypes_0":{"tag":{"data":{"Array":{"Enum":["/Script/TokyoXtremeRacer.ECustomCarPartsType","ByteProperty"]}}},"Array":{"Base":{"Enum":["ECustomCarPartsType::Normal"]}}}}}}},{"key":{"Enum":"ECustomCarPartsKind::RR_BrakeCaliper"},"value":{"Struct":{"Struct":{"EquipType_0":{"tag":{"data":{"Enum":["/Script/TokyoXtremeRacer.ECustomCarPartsType","ByteProperty"]}},"Enum":"ECustomCarPartsType::Normal"},"HaveTypes_0":{"tag":{"data":{"Array":{"Enum":["/Script/TokyoXtremeRacer.ECustomCarPartsType","ByteProperty"]}}},"Array":{"Base":{"Enum":["ECustomCarPartsType::Normal"]}}}}}}},{"key":{"Enum":"ECustomCarPartsKind::FL_BrakeRotar"},"value":{"Struct":{"Struct":{"EquipType_0":{"tag":{"data":{"Enum":["/Script/TokyoXtremeRacer.ECustomCarPartsType","ByteProperty"]}},"Enum":"ECustomCarPartsType::Normal"},"HaveTypes_0":{"tag":{"data":{"Array":{"Enum":["/Script/TokyoXtremeRacer.ECustomCarPartsType","ByteProperty"]}}},"Array":{"Base":{"Enum":["ECustomCarPartsType::Normal"]}}}}}}},{"key":{"Enum":"ECustomCarPartsKind::FR_BrakeRotar"},"value":{"Struct":{"Struct":{"EquipType_0":{"tag":{"data":{"Enum":["/Script/TokyoXtremeRacer.ECustomCarPartsType","ByteProperty"]}},"Enum":"ECustomCarPartsType::Normal"},"HaveTypes_0":{"tag":{"data":{"Array":{"Enum":["/Script/TokyoXtremeRacer.ECustomCarPartsType","ByteProperty"]}}},"Array":{"Base":{"Enum":["ECustomCarPartsType::Normal"]}}}}}}},{"key":{"Enum":"ECustomCarPartsKind::RL_BrakeRotar"},"value":{"Struct":{"Struct":{"EquipType_0":{"tag":{"data":{"Enum":["/Script/TokyoXtremeRacer.ECustomCarPartsType","ByteProperty"]}},"Enum":"ECustomCarPartsType::Normal"},"HaveTypes_0":{"tag":{"data":{"Array":{"Enum":["/Script/TokyoXtremeRacer.ECustomCarPartsType","ByteProperty"]}}},"Array":{"Base":{"Enum":["ECustomCarPartsType::Normal"]}}}}}}},{"key":{"Enum":"ECustomCarPartsKind::RR_BrakeRotar"},"value":{"Struct":{"Struct":{"EquipType_0":{"tag":{"data":{"Enum":["/Script/TokyoXtremeRacer.ECustomCarPartsType","ByteProperty"]}},"Enum":"ECustomCarPartsType::Normal"},"HaveTypes_0":{"tag":{"data":{"Array":{"Enum":["/Script/TokyoXtremeRacer.ECustomCarPartsType","ByteProperty"]}}},"Array":{"Base":{"Enum":["ECustomCarPartsType::Normal"]}}}}}}},{"key":{"Enum":"ECustomCarPartsKind::FrontBumperHeadLight"},"value":{"Struct":{"Struct":{"EquipType_0":{"tag":{"data":{"Enum":["/Script/TokyoXtremeRacer.ECustomCarPartsType","ByteProperty"]}},"Enum":"ECustomCarPartsType::Normal"},"HaveTypes_0":{"tag":{"data":{"Array":{"Enum":["/Script/TokyoXtremeRacer.ECustomCarPartsType","ByteProperty"]}}},"Array":{"Base":{"Enum":["ECustomCarPartsType::Normal"]}}}}}}},{"key":{"Enum":"ECustomCarPartsKind::FrontBumperWinkerR"},"value":{"Struct":{"Struct":{"EquipType_0":{"tag":{"data":{"Enum":["/Script/TokyoXtremeRacer.ECustomCarPartsType","ByteProperty"]}},"Enum":"ECustomCarPartsType::Normal"},"HaveTypes_0":{"tag":{"data":{"Array":{"Enum":["/Script/TokyoXtremeRacer.ECustomCarPartsType","ByteProperty"]}}},"Array":{"Base":{"Enum":["ECustomCarPartsType::Normal"]}}}}}}},{"key":{"Enum":"ECustomCarPartsKind::FrontBumperWinkerL"},"value":{"Struct":{"Struct":{"EquipType_0":{"tag":{"data":{"Enum":["/Script/TokyoXtremeRacer.ECustomCarPartsType","ByteProperty"]}},"Enum":"ECustomCarPartsType::Normal"},"HaveTypes_0":{"tag":{"data":{"Array":{"Enum":["/Script/TokyoXtremeRacer.ECustomCarPartsType","ByteProperty"]}}},"Array":{"Base":{"Enum":["ECustomCarPartsType::Normal"]}}}}}}},{"key":{"Enum":"ECustomCarPartsKind::RearBumperWinkerR"},"value":{"Struct":{"Struct":{"EquipType_0":{"tag":{"data":{"Enum":["/Script/TokyoXtremeRacer.ECustomCarPartsType","ByteProperty"]}},"Enum":"ECustomCarPartsType::Normal"},"HaveTypes_0":{"tag":{"data":{"Array":{"Enum":["/Script/TokyoXtremeRacer.ECustomCarPartsType","ByteProperty"]}}},"Array":{"Base":{"Enum":["ECustomCarPartsType::Normal"]}}}}}}},{"key":{"Enum":"ECustomCarPartsKind::RearBumperWinkerL"},"value":{"Struct":{"Struct":{"EquipType_0":{"tag":{"data":{"Enum":["/Script/TokyoXtremeRacer.ECustomCarPartsType","ByteProperty"]}},"Enum":"ECustomCarPartsType::Normal"},"HaveTypes_0":{"tag":{"data":{"Array":{"Enum":["/Script/TokyoXtremeRacer.ECustomCarPartsType","ByteProperty"]}}},"Array":{"Base":{"Enum":["ECustomCarPartsType::Normal"]}}}}}}},{"key":{"Enum":"ECustomCarPartsKind::RearBumperBrakeLamp"},"value":{"Struct":{"Struct":{"EquipType_0":{"tag":{"data":{"Enum":["/Script/TokyoXtremeRacer.ECustomCarPartsType","ByteProperty"]}},"Enum":"ECustomCarPartsType::Normal"},"HaveTypes_0":{"tag":{"data":{"Array":{"Enum":["/Script/TokyoXtremeRacer.ECustomCarPartsType","ByteProperty"]}}},"Array":{"Base":{"Enum":["ECustomCarPartsType::Normal"]}}}}}}},{"key":{"Enum":"ECustomCarPartsKind::RearBumperBackLamp"},"value":{"Struct":{"Struct":{"EquipType_0":{"tag":{"data":{"Enum":["/Script/TokyoXtremeRacer.ECustomCarPartsType","ByteProperty"]}},"Enum":"ECustomCarPartsType::Normal"},"HaveTypes_0":{"tag":{"data":{"Array":{"Enum":["/Script/TokyoXtremeRacer.ECustomCarPartsType","ByteProperty"]}}},"Array":{"Base":{"Enum":["ECustomCarPartsType::Normal"]}}}}}}},{"key":{"Enum":"ECustomCarPartsKind::RearSpoilerBrakeLamp"},"value":{"Struct":{"Struct":{"EquipType_0":{"tag":{"data":{"Enum":["/Script/TokyoXtremeRacer.ECustomCarPartsType","ByteProperty"]}},"Enum":"ECustomCarPartsType::Normal"},"HaveTypes_0":{"tag":{"data":{"Array":{"Enum":["/Script/TokyoXtremeRacer.ECustomCarPartsType","ByteProperty"]}}},"Array":{"Base":{"Enum":["ECustomCarPartsType::Normal"]}}}}}}},{"key":{"Enum":"ECustomCarPartsKind::FrontBumperHeadLightL"},"value":{"Struct":{"Struct":{"EquipType_0":{"tag":{"data":{"Enum":["/Script/TokyoXtremeRacer.ECustomCarPartsType","ByteProperty"]}},"Enum":"ECustomCarPartsType::Normal"},"HaveTypes_0":{"tag":{"data":{"Array":{"Enum":["/Script/TokyoXtremeRacer.ECustomCarPartsType","ByteProperty"]}}},"Array":{"Base":{"Enum":["ECustomCarPartsType::Normal"]}}}}}}},{"key":{"Enum":"ECustomCarPartsKind::FrontBumperHeadLightR"},"value":{"Struct":{"Struct":{"EquipType_0":{"tag":{"data":{"Enum":["/Script/TokyoXtremeRacer.ECustomCarPartsType","ByteProperty"]}},"Enum":"ECustomCarPartsType::Normal"},"HaveTypes_0":{"tag":{"data":{"Array":{"Enum":["/Script/TokyoXtremeRacer.ECustomCarPartsType","ByteProperty"]}}},"Array":{"Base":{"Enum":["ECustomCarPartsType::Normal"]}}}}}}}]},"NewDressUpInfo_0":{"tag":{"data":{"Array":{"Enum":["/Script/TokyoXtremeRacer.ECustomCarPartsSimpleKind","ByteProperty"]}}},"Array":{"Base":{"Enum":[]}}},"AlreadyNewDressUpInfo_0":{"tag":{"data":{"Array":{"Enum":["/Script/TokyoXtremeRacer.ECustomCarPartsSimpleKind","ByteProperty"]}}},"Array":{"Base":{"Enum":[]}}},"FrontTire_0":{"tag":{"data":{"Struct":{"struct_type":{"Struct":"/Script/TokyoXtremeRacer.SCarTireInfo"},"id":"00000000-0000-0000-0000-000000000000"}}},"Struct":{"Struct":{"Width_0":{"tag":{"data":{"Other":"IntProperty"}},"Int":195},"Inchi_0":{"tag":{"data":{"Other":"IntProperty"}},"Int":14},"AspectRatio_0":{"tag":{"data":{"Other":"IntProperty"}},"Int":60},"Pulling_0":{"tag":{"data":{"Other":"IntProperty"}},"Int":0}}}},"RearTire_0":{"tag":{"data":{"Struct":{"struct_type":{"Struct":"/Script/TokyoXtremeRacer.SCarTireInfo"},"id":"00000000-0000-0000-0000-000000000000"}}},"Struct":{"Struct":{"Width_0":{"tag":{"data":{"Other":"IntProperty"}},"Int":195},"Inchi_0":{"tag":{"data":{"Other":"IntProperty"}},"Int":14},"AspectRatio_0":{"tag":{"data":{"Other":"IntProperty"}},"Int":60},"Pulling_0":{"tag":{"data":{"Other":"IntProperty"}},"Int":0}}}},"FrontTireType_0":{"tag":{"data":{"Enum":["/Script/TokyoXtremeRacer.ECarTireType","ByteProperty"]}},"Enum":"ECarTireType::Medium"},"RearTireType_0":{"tag":{"data":{"Enum":["/Script/TokyoXtremeRacer.ECarTireType","ByteProperty"]}},"Enum":"ECarTireType::Medium"},"FrontWheelInfo_0":{"tag":{"data":{"Struct":{"struct_type":{"Struct":"/Script/TokyoXtremeRacer.SWheelInfo"},"id":"00000000-0000-0000-0000-000000000000"}}},"Struct":{"Struct":{"WheelId_0":{"tag":{"data":{"Other":"NameProperty"}},"Name":"Normal"},"ColorId_0":{"tag":{"data":{"Other":"NameProperty"}},"Name":"None"}}}},"RearWheelInfo_0":{"tag":{"data":{"Struct":{"struct_type":{"Struct":"/Script/TokyoXtremeRacer.SWheelInfo"},"id":"00000000-0000-0000-0000-000000000000"}}},"Struct":{"Struct":{"WheelId_0":{"tag":{"data":{"Other":"NameProperty"}},"Name":"Normal"},"ColorId_0":{"tag":{"data":{"Other":"NameProperty"}},"Name":"None"}}}},"HaveWheels_0":{"tag":{"data":{"Array":{"Other":"NameProperty"}}},"Array":{"Base":{"Name":[]}}},"FrontBrake_0":{"tag":{"data":{"Struct":{"struct_type":{"Struct":"/Script/TokyoXtremeRacer.SBrakeInfo"},"id":"00000000-0000-0000-0000-000000000000"}}},"Struct":{"Struct":{"RotorId_0":{"tag":{"data":{"Other":"NameProperty"}},"Name":"Normal"},"CaliperId_0":{"tag":{"data":{"Other":"NameProperty"}},"Name":"Normal"},"RotorScale_0":{"tag":{"data":{"Other":"IntProperty"}},"Int":100},"CaliperAngle_0":{"tag":{"data":{"Other":"IntProperty"}},"Int":0},"CaliperColor_0":{"tag":{"data":{"Other":"NameProperty"}},"Name":"None"}}}},"RearBrake_0":{"tag":{"data":{"Struct":{"struct_type":{"Struct":"/Script/TokyoXtremeRacer.SBrakeInfo"},"id":"00000000-0000-0000-0000-000000000000"}}},"Struct":{"Struct":{"RotorId_0":{"tag":{"data":{"Other":"NameProperty"}},"Name":"Normal"},"CaliperId_0":{"tag":{"data":{"Other":"NameProperty"}},"Name":"Normal"},"RotorScale_0":{"tag":{"data":{"Other":"IntProperty"}},"Int":100},"CaliperAngle_0":{"tag":{"data":{"Other":"IntProperty"}},"Int":0},"CaliperColor_0":{"tag":{"data":{"Other":"NameProperty"}},"Name":"None"}}}},"HaveBrakes_0":{"tag":{"data":{"Array":{"Other":"NameProperty"}}},"Array":{"Base":{"Name":[]}}},"HaveRearBrakes_0":{"tag":{"data":{"Array":{"Other":"NameProperty"}}},"Array":{"Base":{"Name":[]}}},"LicensePlate_0":{"tag":{"data":{"Struct":{"struct_type":{"Struct":"/Script/TokyoXtremeRacer.SCarLicensePlate"},"id":"00000000-0000-0000-0000-000000000000"}}},"Struct":{"Struct":{"Area_0":{"tag":{"data":{"Enum":["/Script/TokyoXtremeRacer.ECarLicensePlateArea","ByteProperty"]}},"Enum":"ECarLicensePlateArea::Chiba_Sodegaura"},"PlateCategory_0":{"tag":{"data":{"Other":"IntProperty"}},"Int":0},"PlaceNameIndex_0":{"tag":{"data":{"Other":"IntProperty"}},"Int":48},"ClassNumber100_0":{"tag":{"data":{"Other":"IntProperty"}},"Int":5},"ClassNumber010_0":{"tag":{"data":{"Other":"IntProperty"}},"Int":8},"ClassNumber001_0":{"tag":{"data":{"Other":"IntProperty"}},"Int":1},"CharactorIndex_0":{"tag":{"data":{"Other":"IntProperty"}},"Int":30},"IndividualNumber1000_0":{"tag":{"data":{"Other":"IntProperty"}},"Int":3},"IndividualNumber0100_0":{"tag":{"data":{"Other":"IntProperty"}},"Int":8},"IndividualNumberHyphen_0":{"tag":{"data":{"Other":"IntProperty"}},"Int":0},"IndividualNumber0010_0":{"tag":{"data":{"Other":"IntProperty"}},"Int":4},"IndividualNumber0001_0":{"tag":{"data":{"Other":"IntProperty"}},"Int":1}}}},"NumberOfCourseEntries_0":{"tag":{"data":{"Other":"IntProperty"}},"Int":0},"WindowStickers_0":{"tag":{"data":{"Map":{"key_type":{"Enum":["/Script/TokyoXtremeRacer.EWindowStickerIndex","ByteProperty"]},"value_type":{"Struct":{"struct_type":{"Struct":"/Script/TokyoXtremeRacer.SMyCarWindowSticker"},"id":"00000000-0000-0000-0000-000000000000"}}}}},"Map":[]},"BodyStickers_0":{"tag":{"data":{"Map":{"key_type":{"Other":"IntProperty"},"value_type":{"Struct":{"struct_type":{"Struct":"/Script/TokyoXtremeRacer.SMyCarBodySticker"},"id":"00000000-0000-0000-0000-000000000000"}}}}},"Map":[]},"RearWingStickers_0":{"tag":{"data":{"Map":{"key_type":{"Other":"IntProperty"},"value_type":{"Struct":{"struct_type":{"Struct":"/Script/TokyoXtremeRacer.SMyCarBodySticker"},"id":"00000000-0000-0000-0000-000000000000"}}}}},"Map":[]},"Effect_0":{"tag":{"data":{"Struct":{"struct_type":{"Struct":"/Script/TokyoXtremeRacer.SCarEffect"},"id":"00000000-0000-0000-0000-000000000000"}}},"Struct":{"Struct":{"AuraNameId_0":{"tag":{"data":{"Other":"NameProperty"}},"Name":"None"},"AfterFireNameId_0":{"tag":{"data":{"Other":"NameProperty"}},"Name":"Default"},"NitroNameId_0":{"tag":{"data":{"Other":"NameProperty"}},"Name":"Default"}}}},"Neons_0":{"tag":{"data":{"Map":{"key_type":{"Enum":["/Script/TokyoXtremeRacer.ENeonLightPositionType","ByteProperty"]},"value_type":{"Struct":{"struct_type":{"Struct":"/Script/TokyoXtremeRacer.SMyCarNeon"},"id":"00000000-0000-0000-0000-000000000000"}}}}},"Map":[]},"HaveNeons_0":{"tag":{"data":{"Array":{"Enum":["/Script/TokyoXtremeRacer.ENeonLightPositionType","ByteProperty"]}}},"Array":{"Base":{"Enum":[]}}},"OrgGenuineColor_0":{"tag":{"data":{"Other":"IntProperty"}},"Int":2}}}}}

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