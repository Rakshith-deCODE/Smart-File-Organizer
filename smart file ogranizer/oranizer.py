import os
import shutil

print("Smart File Organizer")

folder_path = input("Enter folder path: ")

if not os.path.exists(folder_path):
    print("Folder does not exist")
    exit()

for file in os.listdir(folder_path):
    file_path = os.path.join(folder_path, file)

    if os.path.isfile(file_path):
        if file.endswith(".jpg") or file.endswith(".png"):
            os.makedirs(folder_path + "/Images", exist_ok=True)
            shutil.move(file_path, folder_path + "/Images/" + file)

        elif file.endswith(".pdf") or file.endswith(".docx"):
            os.makedirs(folder_path + "/Documents", exist_ok=True)
            shutil.move(file_path, folder_path + "/Documents/" + file)

        elif file.endswith(".mp4"):
            os.makedirs(folder_path + "/Videos", exist_ok=True)
            shutil.move(file_path, folder_path + "/Videos/" + file)

print("Files organized successfully")