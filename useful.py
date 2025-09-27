def user_input_directories()-> list:
    """
    Provides a way for a user to add the directories that they want to be organised.
    Loops continually until the user 

    Returns: Array of directories
    """
    folders_chosen = False

    folders = [
    ]

    while not folders_chosen:
        new_folder = input("Please paste the path of the folder you would like organised:\n")
        folders.append(new_folder)

        print("\nHere is your list of folders to organise:\n")
        for folder in folders: print(folder)
        while True:
            finished = input("Is this the entire list of folders to organise? [y/n]   ")
            if finished.upper() == "Y":
                folders_chosen = True
                break
            elif finished in ("n", "no"):
                folders_chosen = False
                break
            else:
                print("Please enter 'y' or 'n'.")

    return folders
