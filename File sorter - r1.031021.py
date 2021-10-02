import os
import shutil
import time

# Path that needs to be sorted goes here:
#path = "C:\\Users\\Toby\\Desktop\\sorthere"

def filesetup(path):
    try:
        print("\ninitialising...")
        time.sleep(1)
        os.makedirs(path + "\\sorted files")
        input("Made file. Press enter to continue")
    except FileExistsError:
        pass
        

def photo(file, path):
    ext = -1
    photos = [".png", ".jpg", ".jpeg"]
    for x in photos:
        ext = ext + 1
        extension = photos[ext]
        if extension in file:
            destination = path + "\\sorted files\\photos"
            photopath = path + "\\" + file
            try:
                os.makedirs(path + "\\sorted files\\photos")
                shutil.copy2(photopath, destination)
                os.remove(photopath)
            except FileExistsError:
                shutil.copy2(photopath, destination)
                os.remove(photopath)
            
        else:
            pass

def video(file, path):
    ext = -1
    videos = [".mp4", ".webm", ".mkv", ".gif", "wmv", ".amv", ".vpg", "m4p", ".mpg"]
    for x in videos:
        ext = ext + 1
        extension = videos[ext]
        if extension in file:
            destination = path + "\\sorted files\\videos"
            vidpath = path + "\\" + file
            try:
                os.makedirs(path + "\\sorted files\\videos")
                shutil.copy2(vidpath, destination)
                os.remove(vidpath)
            except FileExistsError:
                shutil.copy2(vidpath, destination)
                os.remove(vidpath)
            
        else:
            pass


def main(sortpath): 
    #filesetup()
    documents = [".docx", ".txt", ".pdf"]
    videos = [".mp4", ".webm", ".mkv", ".gif", "wmv", ".amv", ".vpg", "m4p", ".mpg"]
    pythonprojects = ".py"
    names = os.listdir(sortpath)
    numberoffile = -1
    for x in names:
        totalfiles = len(names)
        numberoffile = numberoffile + 1
        file = names[numberoffile]
        photo(file, sortpath)
        video(file, sortpath)
        print("Sorted file: ",numberoffile,"/",totalfiles)
    print("All files sorted. Thank me later ;)")

def setup():
    print("""
    --File sorter r1.2909--

    1. Run with default settings
    2. View default settings
    3. Run with custom settings (will take longer)
    """)
    number = input("Enter Number: ")
    if number == "1":
        path = input(r"Enter path with two slashes e.g C:\\Users\\Toby\\Desktop : ")
        if r"\\" not in path:
            print("\nPlease enter the correct path!")
            time.sleep(2)
            setup()
        time.sleep(1)
        print("\nReady to sort")
        input("\nPress enter to sort files: ")
        main(path)
    elif number == "2":
        print("""---Default Settings---

    Images --> Images folder
    Videos --> Videos folder
    Documents --> documents folder

    Note: You can make it sort more files in custom settings!""")
        time.sleep(5)
        setup()
        
    else:
        pass

setup()
