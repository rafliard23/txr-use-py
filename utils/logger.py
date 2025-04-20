import logging
import logging.config

from typing import Union
from pathlib import Path

def fileConfig(fname: Union[str, Path]) -> None:
    # I just want to make sure it works for built in tomllib on later Python
    try:
        import tomlib
    except ModuleNotFoundError:
        import tomli as tomllib

    with open(fname, "rb") as stream:
        toml_dict = tomllib.load(stream)
    
    # Check log section in config.toml
    log_table = toml_dict.get("logging", {})
    
    if not log_table:
        raise KeyError(
            "log table not found, please edit config in config.toml"
        )
    
    logging.config.dictConfig(log_table)