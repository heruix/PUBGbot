import win32api
from win32api import *



def get_mouse():
	state_f2=win32api.GetKeyState(0x71)	
	while True:
		localf2 = win32api.GetKeyState(0x71)
		if localf2 != state_f2:
			state_f2 = localf2
			if localf2 < 0:
				print(GetCursorPos())
				#win32api.Beep(1600,50)
				win32api.Beep(2000,100)
			else:
				pass
				#win32api.Beep(400,100)
				#win32api.Beep(300,50)
	
get_mouse()