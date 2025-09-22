from pathlib import Path
from useful import user_input_directories
import os
from datetime import datetime

folders = user_input_directories()

def organise_files_by_date():
    for folder in folders:
        folder = Path(folder)  # creates a path object from the string

        for file in folder.rglob('*'):  # iterates through all files in the folder
            if file.is_file():  # checks if the file is a file
                modified_date = datetime.fromtimestamp(os.path.getmtime(file)) # gets the 'modified date' info of the file
                file_year = str(modified_date.year)
                file_month = modified_date.strftime("%B")
                if not Path(folder / file_year).exists():  # checks if the year folder does not exist yet
                    year_folder = Path(folder / file_year)
                    year_folder.mkdir()  # creates folder with new name
                if not Path(folder / file_year / file_month).exists(): # checks if the month folder does not exist yet
                    month_folder = Path(folder / file_year / file_month)
                    month_folder.mkdir()  # creates folder with new name
                try:
                    file.rename(folder / file_year / file_month / file.name)  # tries to move file to new folder
                except FileExistsError:  # if file already exists in new folder
                    notice = f'"{file}" already exists in {folder + file_year + file_month}'
                    print(notice)


    print("\n Completed. Any unmoved files remain because there is already a file with the given name in the target directory.")


if __name__ == "__main__":
    organise_files_by_date()