import os
import time
import pyautogui

from colorama import Fore, Back, Style


def clear():
    os.system("clear")

def logo():
    print(Fore.GREEN + '''
    
    
                                            
 ,-----.,--.,--.      ,--.                  
'  .--./|  |`--' ,---.|  |,-. ,---. ,--.--. 
|  |    |  |,--.| .--'|     /| .-. :|  .--' 
'  '--'\|  ||  |\ `--.|  \  \\   --.|  |    
 `-----'`--'`--' `---'`--'`--'`----'`--'    
                                            

    
    
    ''')

def main():
    clear()
    logo()
    pyautogui.alert('Program is started... Waiting 5 secounds')
    time.sleep(5)

    print(Fore.GREEN + "Starting...")

    while True:
        pyautogui.click()

#start

main()