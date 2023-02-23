import os
import shutil
import pandas as pd

MAIN_FOLDER = "Folder"
EXCEL_FILE = "name_of_folders.xlsx"


def folder_creator(main_folder, sub_folders) -> None:
    """Function that create folders.
    arguments:
    main_folder - main folder
    sub_folders - subfolders of main folder
    """
    if os.path.isdir(main_folder):
        shutil.rmtree(main_folder)
    os.mkdir(main_folder)
    for folder in sub_folders:
        path = os.path.join(main_folder, folder)
        os.mkdir(path)


def read_excel_file(path):
    """Read excel with pandas and return list of firs column"""
    df = pd.read_excel("name_of_folders.xlsx", sheet_name="Sheet1")
    first_column = df.iloc[:, 0].tolist()
    return first_column


sub_folders_list = read_excel_file(EXCEL_FILE)

folder_creator(main_folder=MAIN_FOLDER, sub_folders=sub_folders_list)
