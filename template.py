import os 
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s: %(message)s]:')

project_name = "textSummarizer"
list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/logging/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    ".gitignore",
    "README.md",
    "requirements.txt",
    "app.py",
    "main.py",
    "Dockerfile",
    "setup.py",
    "research/trails.ipynb"
]

for file_path in list_of_files:
    file_path = Path(file_path)
    file_dir, file_name = os.path.split(file_path)

    
    if file_dir !="":
        os.makedirs(file_dir, exist_ok=True)
        logging.info(f"Creating directory: {file_dir} for file {file_name}")
    if (not os.path.exists(file_path)) or (os.path.getsize(file_path) == 0):
        # Check if the file already exists and is not empty
        with open(file_path, 'w') as f:
            pass
            logging.info(f"Creating file: {file_path} for file {file_name}")
    else:
        logging.info(f"File {file_path} already exists and is not empty. Skipping creation.")
    