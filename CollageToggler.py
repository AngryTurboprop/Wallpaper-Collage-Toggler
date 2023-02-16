"""
Program which toggles the slideshow collages on or off when run

2023 Michael Vogl
"""

import winreg, ctypes

def toggleSlideshow():
    #Check to see if the registry entry exists. If not, create it. Windows does not have this registry entry by default
    try:
        access_registry = winreg.ConnectRegistry(None,winreg.HKEY_CURRENT_USER)
        access_key = winreg.OpenKey(access_registry,r"Software\Microsoft\Windows\CurrentVersion\Lock Screen", reserved=0, access=winreg.KEY_READ)
        winreg.QueryValueEx(access_key, "SlideShowLayout")[0]
    except Exception as e:
        #Create the registry key and set it to 0 to turn off 
        try:
            access_registry = winreg.ConnectRegistry(None,winreg.HKEY_CURRENT_USER)
            access_key = winreg.CreateKey(access_registry,r"Software\Microsoft\Windows\CurrentVersion\Lock Screen")
            winreg.SetValueEx(access_key, "SlideShowLayout", 1, winreg.REG_DWORD, 0)
        #Fail and display the error
        except Exception as ef:
            ctypes.windll.user32.MessageBoxW(0, ("FATAL: Failed to find and create registry entry:\n")+str(e), "Michael's Tools", 0)
            return False

    access_key = winreg.OpenKey(access_registry,r"Software\Microsoft\Windows\CurrentVersion\Lock Screen", reserved=0, access=winreg.KEY_READ)

    #Check to see if hte registry entry is enabled or disabled, then toggle it and display a message
    if (winreg.QueryValueEx(access_key, "SlideShowLayout")[0] != 1):
        access_key = winreg.OpenKey(access_registry,r"Software\Microsoft\Windows\CurrentVersion\Lock Screen", reserved=0, access=winreg.KEY_WRITE)
        winreg.SetValueEx(access_key, "SlideShowLayout", 1, winreg.REG_DWORD, 1)
        ctypes.windll.user32.MessageBoxW(0, "Turned off Slideshow Collage", "Michael's Tools", 0)

    elif (winreg.QueryValueEx(access_key, "SlideShowLayout")[0] == 1):
        access_key = winreg.OpenKey(access_registry,r"Software\Microsoft\Windows\CurrentVersion\Lock Screen", reserved=0, access=winreg.KEY_WRITE)
        winreg.DeleteValue(access_key, "SlideShowLayout")
        ctypes.windll.user32.MessageBoxW(0, "Turned on Slideshow Collage", "Michael's Tools", 0)
    
    #If the registry key is set to something other than 0 or 1, display it and fail
    else:
        ctypes.windll.user32.MessageBoxW(0, "Registry key is not equal to 0 or 1: " + winreg.QueryValueEx(access_key, "SlideShowLayout"), 0)
        return False

    winreg.CloseKey(access_key)
    return True

toggleSlideshow()