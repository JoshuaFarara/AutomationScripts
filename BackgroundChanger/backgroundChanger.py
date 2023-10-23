'''
This script is a windows desktop background changer.
The main function of this script is to change the background daily at a specifice time using a folder of backgound images. 

'''

import ctypes
import os
import random
import shutil

def background_changer():
    # Constants
    SPI_SETDESKWALLPAPER = 0x0014

    # Path to the folder containing the images
    folder_path = r"C:\Users\User\Desktop\Backgrounds"
    # folder_path = r"C:\Users\User\Desktop\backgroundScriptTESTER"

    # Path to the folder where used images will be moved
    used_images_folder = r"C:\Users\User\Desktop\Backgrounds\UsedBackgrounds"
    # used_images_folder = r"C:\Users\User\Desktop\backgroundScriptTESTER\UsedBackgroundsTESTER"

    # Get a list of all image files in the folder ----> next comments explain the list comprehension
    # os.listdir(folder_path): This function returns a list of all files and directories in the specified folder_path.
    # for file in os.listdir(folder_path): This is the iteration part of the list comprehension. It loops over each element (file) in the list returned by os.listdir(folder_path).
    # if file.endswith((".jpg", ".jpeg", ".png")): This is a condition that filters out files that don't have the specified file extensions (.jpg, .jpeg, .png). The endswith() method is used to check if the file name ends with any of the given extensions.
    # os.path.join(folder_path, file): This is the expression part of the list comprehension. It combines the folder_path and file name using os.path.join() to create the full path of the image file.
    image_files = [os.path.join(folder_path, file) for file in os.listdir(folder_path) if file.endswith((".jpg", ".jpeg", ".png", ".jfif"))]

    # Shuffle the image files list to ensure random selection
    random.shuffle(image_files)

    if image_files:
        if len(image_files) > 1:
            image_path = image_files.pop(0)
            print(image_path)
        else:
            image_path = image_files[-1]  # Select the last image
            print("The final image {} from the {} folder was used.".format(image_path, image_files))

        # Set the background image
        ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, image_path, 3)

        used_image_name = os.path.basename(image_path)
        used_image_destination = os.path.join(used_images_folder, used_image_name)
        shutil.move(image_path, used_image_destination)
    else:
        print("No more background images in the folder")
