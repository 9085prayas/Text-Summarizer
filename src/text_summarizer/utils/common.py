import os
import yaml 
from text_summarizer.logging import logger
from pathlib import Path
from typing import Any
from box.exceptions import BoxValueError
from box import ConfigBox #to access the value of key value value pair like d.key rather than d["key"]


def read_yaml(path_to_yaml: Path) -> ConfigBox: # takes ymal file and returns its content as a ConfigBox

    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e

def create_directories(path_to_directories: list, verbose=True): # takes list of directories and creates them if not exist
    
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"created directory at: {path}")

def get_size(path: Path) -> str: # takes a path and returns its size in kb

    size_in_kb = round(os.path.getsize(path)/1024)
    return f"~ {size_in_kb} KB"