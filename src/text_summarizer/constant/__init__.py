#The constants.py file in a Python project is used to store all fixed values (constants) that are reused throughout the project. This helps keep your code:

#Clean
# - Improves readability by reducing clutter
# - Makes it easier to identify and update constants
# - Helps prevent magic numbers or strings scattered throughout the code

from pathlib import Path

CONFIG_FILE_PATH = Path("config/config.yaml")
PARAMS_FILE_PATH = Path("params.yaml")