
# Lockscreen Collage Toggler

Program which turns lockscreen collages on or off. 

By default in Windows 10 and Windows 11 when you set your Lock Screen to show a Slideshow, it'll automatically create collages and show multiple images on screen at once. This program allows you to show only one image at a time. 

There is no Microsoft documentation on this "feature" and there's no way to turn it on or off in System Settings. 

This is what a lock screen slideshow looks like when you have collages turned off:
![Image](https://github.com/AngryTurboprop/Wallpaper-Collage-Toggler/blob/master/Collages_Off.jpg?raw=true)

This is what shows up every few images when lock screen collages are turned on:
![Image](https://github.com/AngryTurboprop/Wallpaper-Collage-Toggler/blob/master/Collages_On.jpg?raw=true)
## Usage

When the program is run, it will automatically toggle Locks Screen Collages. You'll see a message saying that collages have been turned on or off. You can delete the program afterwards if you want and the changes will stay, but you'll need to download it again and run it if you want to re-enable collages. 

You can download the program from [Releases](https://github.com/AngryTurboprop/Wallpaper-Collage-Toggler/releases)
## How It Works

The program accesses the Windows Registry and looks for a key called `SlideShowLayout` at `Computer\HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Lock Screen`. If `SlideShowLayout` does not exist, or it's not set to `1`, collages will be displayed on the lock screen.

If the registry key does not exist, this program will will attempt to create it and set it to `1`. If the key does exist, the program will assume that the user wants to turn collages back on and it will delete the key.

All of this is taken care of behind the scenes and all you'll see is a dialog box saying that collages have been turned on or off. If something goes wrong, it'll display the error code. If this happens, please report it in the [Issues](https://github.com/AngryTurboprop/Wallpaper-Collage-Toggler/issues) section.
