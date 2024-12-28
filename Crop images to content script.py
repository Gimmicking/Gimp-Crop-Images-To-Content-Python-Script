#Download: https://github.com/Gimmicking/Gimp-Crop-Images-To-Content-Python-Script

numberofimages = 5


import pyautogui
import time

#Countdown
print("This session has been configured to crop to content and override ", numberofimages, " images.")
print("Please have all the images you wish to crop opened in separate Gimp tabs in the same Gimp session.")
print("You must make Gimp your currently opened and selected session for this to work. Please click/select in the Gimp window now.")
print("10 seconds until program starts...")

time.sleep(10)

print("You can stop the program at any point by pressing ctrl + alt + delete")

x = 0
while x < numberofimages:
	#Crop current image to content
	pyautogui.hotkey('alt', 'i')
	pyautogui.press('down', 9)
	pyautogui.press('enter')
	#Export to override original image
	time.sleep(0.2)
	pyautogui.hotkey('alt', 'f')
	pyautogui.press('w')
	#Move to next image
	pyautogui.press('enter')
	pyautogui.hotkey('ctrl', 'pagedown')
	x += 1

