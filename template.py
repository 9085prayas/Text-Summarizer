#this is just the templet of our repo we are writting it in a python code

import os
from pathlib import Path
import logging # for all the log 


logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

project_name = 'text_summarizer'

#all the files in your project
list_of_files = [ 
    '.github/workflows/.gitkeep',
    f'src/{project_name}/__init__.py',
    f'src/{project_name}/conponents/__init__.py',
    f'src/{project_name}/utils/__init__.py',
    f'src/{project_name}/utils/common.py',
    f'src/{project_name}/logging/__init__.py',
    f'src/{project_name}/config/__init__.py',
    f'src/{project_name}/config/config.py',
    f'src/{project_name}/constant/__init__.py',
    f'src/{project_name}/pipeline/__init__.py',
    f'src/{project_name}/entities/__init__.py',
    'config/config.yaml',
    'params.yaml',
    'Docerfile',
    'main.py',
    'app.py',
    'requirements.txt',
    'setup.py',
    'notebook/trials.ipynb',
]

# create the project directory
for filepath in list_of_files:
    filepath = Path(filepath)
    filedir , filename = os.path.split(filepath)

    if filedir != '':
        Path(filedir).mkdir(parents=True, exist_ok=True) #create file directory if not exist
        logging.info(f'Created directory: {filedir}')

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0): #create file if not exist or file is empty
        with open(filepath,'w') as f:
            pass
            logging.info(f"Creating empty file: {filepath}")
    
    else:  
        logging.info(f"{filename} is already exists")