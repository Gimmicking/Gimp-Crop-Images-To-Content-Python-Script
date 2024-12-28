#This script will crop a specified number of images that are opened in a Gimp section to the content and override the original image with this cropped image
#You must have Python and pyautogui installed for this script to work. Install Python 3.8 (or later) on your PC. You can install pyautogui by typing the command "pip3 install pyautogui"
#I am using Python 3.8.10 with pyautogui version 0.9.54
#I am using Gimp version 2.10.38

numberofimages = 7


import pyautogui
import time

#Countdown
print("This session has been configured to crop to content and override ", numberofimages, " images.")
print("Please have all the images you wish to crop opened in separate Gimp tabs in the same Gimp session.")
print("You must make Gimp your currently opened and selected session for this to work. Please click/select in the Gimp window now.")
print("10 seconds until program starts...")

time.sleep(10)

print("You can stop the program at any point by typing ctrl + alt + delete")

x = 0
while x < numberofimages:
	#Crop current image to content
	pyautogui.hotkey('alt', 'i')
	pyautogui.press('down', 9)
	pyautogui.press('enter')
	#Export to override original image
	pyautogui.hotkey('alt', 'f')
	pyautogui.press('w')
	#Move to next image
	pyautogui.hotkey('ctrl', 'pagedown')
	x += 1

