import os
import shutil

from_directory ="C:/Users/vasan/Downloads"
to_directory="C:/Users/vasan/Downloads/downloadedimages"

listOfFiles = os.listdir(from_directory)
for filename in listOfFiles :
    name,extension=os.path.splitext(filename)
    if extension == "":
        continue
    if extension in ['.txt','doc', '.docx', '.pdf']:
        path1=from_directory+"/"+filename
        path2=to_directory+"/"+"Document_Files"
        path3=to_directory+"/"+"Document_Files"+"/"+filename
        if os.path.exists(path2):
            print("moving"+filename+"...")
            shutil.move(path1,path3)
        else:
            os.makedirs(path2)
            print("moving"+filename+"...")
            shutil.move(path1,path3)