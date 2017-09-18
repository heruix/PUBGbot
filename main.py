import win32api
from win32api import *
import win32con
from win32con import *
import win32gui
import colorama
from colorama import *
import threading
import random
import os
import sys
import time
init()

PLAY_BUTTON_XY=76, 117
SQUADFPP_BUTTON_XY=90, 675
AUTOMATCHING_XY=182, 678
DIE_EXIT_XY=1691, 947
EXIT_OK_XY=843, 573
RECONNECT_XY=937, 546



class bot():
	def __init__(self):
		self.screen_width = GetSystemMetrics(0)
		self.screen_height = GetSystemMetrics(1)
		self.x_center = int(self.screen_width/2)
		self.y_center = int(self.screen_height/2)
		self.mouse_x,self.mouse_y = GetCursorPos()
		self.fire_hotkey = 0x01
		self.switch = 0x71
		self.state_mouse = win32api.GetKeyState(self.fire_hotkey)
		self.state_f2 = win32api.GetKeyState(self.switch)
		self.run_bot = False
		self.play_cords=PLAY_BUTTON_XY
		self.squad_cords=SQUADFPP_BUTTON_XY
		self.auto_cords=AUTOMATCHING_XY
		self.exit_cords=DIE_EXIT_XY
		self.ok_cords=EXIT_OK_XY
		self.recon_cords=RECONNECT_XY
	def toggle_bot(self):
		while True:
			localf2 = win32api.GetKeyState(self.switch)
			if localf2 != self.state_f2:
				self.state_f2 = localf2
				if localf2 < 0:
					self.run_bot = not self.run_bot
					if self.run_bot:
						#print(GetCursorPos())
						win32api.Beep(1600,50)
						win32api.Beep(2000,100)
					else:
						win32api.Beep(400,100)
						win32api.Beep(300,50)
	
	def mouse_routine(self):
		while True:
			if self.run_bot:
				time.sleep(5)
				win32api.SetCursorPos((self.play_cords))
				time.sleep(1)
				win32api.SetCursorPos((self.squad_cords))
				win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,self.squad_cords[0],self.squad_cords[1],0,0)
				time.sleep(0.001)
				win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,self.squad_cords[0],self.squad_cords[1],0,0)
				time.sleep(1)
				win32api.SetCursorPos((self.auto_cords))
				win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,self.auto_cords[0],self.auto_cords[1],0,0)
				time.sleep(0.001)
				win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,self.auto_cords[0],self.auto_cords[1],0,0)
				time.sleep(1)
				win32api.SetCursorPos((self.play_cords))
				win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,self.play_cords[0],self.play_cords[1],0,0)
				time.sleep(0.001)
				win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,self.play_cords[0],self.play_cords[1],0,0)
				time.sleep(20)
				win32api.SetCursorPos((self.exit_cords))
				time.sleep(3)
				win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,self.exit_cords[0],self.exit_cords[1],0,0)
				time.sleep(0.001)
				win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,self.exit_cords[0],self.exit_cords[1],0,0)
				time.sleep(1)
				win32api.SetCursorPos((self.ok_cords))
				win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,self.ok_cords[0],self.ok_cords[1],0,0)
				time.sleep(0.001)
				win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,self.ok_cords[0],self.ok_cords[1],0,0)
				time.sleep(0.5)
				win32api.SetCursorPos((self.recon_cords))
				win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,self.recon_cords[0],self.recon_cords[1],0,0)
				time.sleep(0.001)
				win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,self.recon_cords[0],self.recon_cords[1],0,0)
	def keyboard_routine1(self):
		while True:
			if self.run_bot:
				time.sleep(5)
				win32api.keybd_event(0xA0, 0, win32con.KEYEVENTF_EXTENDEDKEY, 0)
				win32api.keybd_event(0x57, 0, win32con.KEYEVENTF_EXTENDEDKEY, 0)
				
				"""
				win32api.keybd_event(0x44, 0, win32con.KEYEVENTF_EXTENDEDKEY, 0) 
				time.sleep(5)
				win32api.keybd_event(0x44, 0, win32con.KEYEVENTF_EXTENDEDKEY | win32con.KEYEVENTF_KEYUP, 0)
				"""
			else:
				win32api.keybd_event(0x57, 0, win32con.KEYEVENTF_EXTENDEDKEY | win32con.KEYEVENTF_KEYUP, 0)
				win32api.keybd_event(0xA0, 0, win32con.KEYEVENTF_EXTENDEDKEY | win32con.KEYEVENTF_KEYUP, 0)

	def keyboard_routine2(self):
		while True:
			if self.run_bot:
				win32api.keybd_event(0x20, 0, win32con.KEYEVENTF_EXTENDEDKEY, 0)
				time.sleep(5)
				win32api.keybd_event(0x20, 0, win32con.KEYEVENTF_EXTENDEDKEY | win32con.KEYEVENTF_KEYUP, 0)
				if random.randint(-15, 15) < -10:
					win32api.keybd_event(0x44, 0, win32con.KEYEVENTF_EXTENDEDKEY, 0)
					time.sleep(0.005)
					win32api.keybd_event(0x44, 0, win32con.KEYEVENTF_EXTENDEDKEY | win32con.KEYEVENTF_KEYUP, 0)
					win32api.keybd_event(0x46, 0, win32con.KEYEVENTF_EXTENDEDKEY, 0)
					time.sleep(0.005)
					win32api.keybd_event(0x46, 0, win32con.KEYEVENTF_EXTENDEDKEY | win32con.KEYEVENTF_KEYUP, 0)
				if random.randint(-15, 15) > 10:
					win32api.keybd_event(0x41, 0, win32con.KEYEVENTF_EXTENDEDKEY , 0)
					time.sleep(0.005)
					win32api.keybd_event(0x41, 0, win32con.KEYEVENTF_EXTENDEDKEY | win32con.KEYEVENTF_KEYUP, 0)
					win32api.keybd_event(0x46, 0, win32con.KEYEVENTF_EXTENDEDKEY, 0)
					time.sleep(0.005)
					win32api.keybd_event(0x46, 0, win32con.KEYEVENTF_EXTENDEDKEY | win32con.KEYEVENTF_KEYUP, 0)
				
			else:
				
				win32api.keybd_event(0x46, 0, win32con.KEYEVENTF_EXTENDEDKEY | win32con.KEYEVENTF_KEYUP, 0)
				win32api.keybd_event(0x20, 0, win32con.KEYEVENTF_EXTENDEDKEY | win32con.KEYEVENTF_KEYUP, 0)
				win32api.keybd_event(0x44, 0, win32con.KEYEVENTF_EXTENDEDKEY | win32con.KEYEVENTF_KEYUP, 0)
				win32api.keybd_event(0x41, 0, win32con.KEYEVENTF_EXTENDEDKEY | win32con.KEYEVENTF_KEYUP, 0)
bot1 = bot()
print(bot1.screen_height,bot1.screen_width)
switch = threading.Thread(target=bot1.toggle_bot)
mroutine = threading.Thread(target=bot1.mouse_routine)
kroutine = threading.Thread(target=bot1.keyboard_routine1)
kroutine2 = threading.Thread(target=bot1.keyboard_routine2)
switch.start()
mroutine.start()
kroutine.start()
kroutine2.start()