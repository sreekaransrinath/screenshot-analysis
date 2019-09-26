import os
from datetime import datetime
from time import strftime

images_folder = '/home/skaranzx16/Media/Images/2019/'
screenshots_folder = '/home/skaranzx16/Media/Images/Screenshots/'

def movescreenshots():
    for imagefile in os.listdir(images_folder):
        is_a_screenshot = False
        print(imagefile)
        stripped_filename = imagefile.replace(" ", "\\ ")

        mdate = os.path.getmtime(images_folder + imagefile)
        year = datetime.fromtimestamp(int(mdate)).strftime("%Y") 
        print('The year of modification for this file is', year)

        dest = screenshots_folder + year + "/"

        year_exists = os.path.exists(dest)
        print("Does the appropriate year directory exist? ", year_exists)

        if not year_exists:
            os.makedirs(dest)
            year_exists = os.path.exists(dest)
            print("The year directory now exists.")

        if not imagefile.lower().find('screenshot') == -1:
            print('The name contains the word Screenshot')
            is_a_screenshot = True

            

    

        if is_a_screenshot:
            movefile(images_folder + stripped_filename, dest)


def movefile(src, dst):
    command = 'mv ' + src + ' ' + dst
    print('The command to be passed to shell is ', command)
    os.system(command)
    print("The file was successfully transferred\n\n")

movescreenshots()