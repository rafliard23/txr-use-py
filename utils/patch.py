import json
import sys
from . import constants
from . import patch_constants
from . import utils

# General for patches
json_data_patches = None

def load_json_patches() -> None:
    global json_data_patches
    
    if json_data_patches is None:
        with open(constants.TMP_PATH,"r", encoding="utf-8") as file:
            json_data_patches = json.load(file)

# Setter Patches
def set_patch_engine_swap_aura() -> bool:
    global json_data_patches
    write = False

    player_perk_data = (
        json_data_patches.get("root", {})
        .get("properties", {})
        .get("user_info_0", {})
        .get("Struct", {})
        .get("Struct", {})
        .get("Perk_0", {})
        .get("Struct", {})
        .get("Struct", {})
        .get("AcquiredPerks_0", {})
        .get("Map", [])
    )

    perks = next((perk for perk in player_perk_data if perk["key"]["Enum"] == "ESkillTreeType::STT_ENABLE_ENGINE_REPLACEMENT"), None)
    if perks:
        pass
    else:
        player_perk_data.append(patch_constants.PLPJ_EG_SWAP)
        write = True

    perks = next((perk for perk in player_perk_data if perk["key"]["Enum"] == "ESkillTreeType::STT_AURA"), None)
    if perks:
        pass
    else:
        player_perk_data.append(patch_constants.PLPJ_AURA)
        write = True

    if write:
        with open(constants.TMP_PATH, "w", encoding="utf-8") as file:
            json.dump(json_data_patches, file, indent=2)
    
    return write

def set_patch_dealer_cars() -> bool:
    global json_data_patches
    write = False

    player_perk_data = (
        json_data_patches.get("root", {})
        .get("properties", {})
        .get("user_info_0", {})
        .get("Struct", {})
        .get("Struct", {})
        .get("CanBoughtCarNameIds_0", {})
        .get("Array", {})
        .get("Base", {})
    )

    if sys.getsizeof(player_perk_data) != sys.getsizeof(patch_constants.Cars):
        player_perk_data["Name"] = patch_constants.Cars
        write = True
    else:
        pass

    if write:
        with open(constants.TMP_PATH, "w", encoding="utf-8") as file:
            json.dump(json_data_patches, file, indent=2)
    
    return write

def set_patch_vinyls_emblem_auras() -> bool:
    global json_data_patches
    write = False

    player_livery_editor = (
        json_data_patches.get("root", {})
        .get("properties", {})
        .get("user_info_0", {})
        .get("Struct", {})
        .get("Struct", {})
    )

    save_vinyls = player_livery_editor["UnlockVinyls_0"]["Array"]["Base"]
    save_stickers = player_livery_editor["UnlockStickers_0"]["Array"]["Base"]
    save_auras = player_livery_editor["UnlockAuras_0"]["Array"]["Base"]

    if sys.getsizeof(save_vinyls) != sys.getsizeof(patch_constants.Vinyls):
        save_vinyls["Name"] = patch_constants.Vinyls
        write = True
    else:
        pass

    if sys.getsizeof(save_stickers) != sys.getsizeof(patch_constants.Stickers):
        save_stickers["Name"] = patch_constants.Stickers
        write = True
    else:
        pass

    if sys.getsizeof(save_auras) != sys.getsizeof(patch_constants.Aura):
        save_auras["Name"] = patch_constants.Aura
        write = True
    else:
        pass

    if write:
        with open(constants.TMP_PATH, "w", encoding="utf-8") as file:
            json.dump(json_data_patches, file, indent=2)

    return write

def set_patch_wanderer_fix() -> bool:
    global json_data_patches
    write = False

    wanderers_data = (
        json_data_patches.get("root", {})
        .get("properties", {})
        .get("user_info_0", {})
        .get("Struct", {})
        .get("Struct", {})
        .get("RivalSituations", {})
    )

    betelguese_data = next((wanderer for wanderer in wanderers_data if wanderer["key"]["Name"] == "Rival_0027"), None)
    if betelguese_data:
        if betelguese_data["value"]["Struct"]["Struct"]["WinNum_0"] >= 1:
            betelguese_data["value"]["Struct"]["Struct"]["WinNum_0"] = 5
            betelguese_data["value"]["Struct"]["Struct"]["NumOfWinsWithoutNitro_0"] = 5
            write = True
        else:
            pass
    
    crimson_boy_data = next((wanderer for wanderer in wanderers_data if wanderer["key"]["Name"] == "Boss_0012_2"), None)
    if crimson_boy_data:
        if crimson_boy_data["value"]["Struct"]["Struct"]["WinNum_0"] >= 1:
            crimson_boy_data["value"]["Struct"]["Struct"]["WinNum_0"] = 2
            crimson_boy_data["value"]["Struct"]["Struct"]["NumOfWinsWithoutNitro_0"] = 2
            write = True
        else:
            pass

    golden_hannya_data = next((wanderer for wanderer in wanderers_data if wanderer["key"]["Name"] == "Boss_0013_2"), None)
    if golden_hannya_data:
        if golden_hannya_data["value"]["Struct"]["Struct"]["WinNum_0"] >= 1:
            golden_hannya_data["value"]["Struct"]["Struct"]["WinNum_0"] = 2
            golden_hannya_data["value"]["Struct"]["Struct"]["NumOfWinsWithoutNitro_0"] = 2
            write = True
        else:
            pass
    
    iron_oldman_data = next((wanderer for wanderer in wanderers_data if wanderer["key"]["Name"] == "Boss_0014_2"), None)
    if iron_oldman_data:
        if iron_oldman_data["value"]["Struct"]["Struct"]["WinNum_0"] >= 1:
            iron_oldman_data["value"]["Struct"]["Struct"]["WinNum_0"] = 2
            iron_oldman_data["value"]["Struct"]["Struct"]["NumOfWinsWithoutNitro_0"] = 2
            write = True
        else:
            pass
    
    if write:
        with open(constants.TMP_PATH, "w", encoding="utf-8") as file:
            json.dump(json_data_patches, file, indent=2)
    
    return write

def set_patch_value_int(patch_query: list) -> None:
    global json_data_patches
    write = False

    patch = (
        json_data_patches.get("root", {})
        .get("properties", {})
        .get("user_info_0", {})
        .get("Struct", {})
        .get("Struct", {})
    )

    patch_data = utils.bool_list_to_int(patch_query)
    if (patch["PatchSE_0"]["Int64"] != patch_data):
        patch["PatchSE_0"]["Int64"] = patch_data
        write = True

    if write:
        with open(constants.TMP_PATH, "w", encoding="utf-8") as file:
            json.dump(json_data_patches, file, indent=2)

# Proper patch function
# def patch_handler(patch_request: list, patch_data: list, functions):
#     for i, flag in enumerate(patch_request):
#         if (flag) and (patch_data[i] is not True):
#             functions[i]()  # call the function if True

# Multi applicable
def patch_handler(patch_request: list, functions):
    for i, flag in enumerate(patch_request):
        if flag:
            functions[i]()  # call the function if True

# /------- End of Setter -------/
# Getter
def get_save_patch_status() -> list:
    global json_data_patches

    patch = (
        json_data_patches.get("root", {})
        .get("properties", {})
        .get("user_info_0", {})
        .get("Struct", {})
        .get("Struct", {})
    )

    if "PatchSE_0" not in patch:
        patch.update(patch_constants.SE_PATCH)
        patch_data = 0
    else:
        patch_data = patch["PatchSE_0"]["Int64"]
    patch_status = utils.int_to_bool_list(patch_data, len(patch_constants.PATCH_DESC))

    return patch_status

# /------- End of Getter -------/
PATCH_FUNCS = [set_patch_dealer_cars,
               set_patch_vinyls_emblem_auras,
               set_patch_engine_swap_aura,
               set_patch_wanderer_fix]