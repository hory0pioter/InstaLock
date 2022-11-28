print("Importing...")
from os import system
try:
	import pyautogui
	import cv2
	import PIL
except:
	system('py -m pip install pyautogui')
	system('py -m pip install pillow')
	system('py -m pip install opencv-python')
	import pyautogui
from time import time, sleep

print("Everythining fine!")
sleep(1)
system('cls')

agn = ['astra','breach','brimstone','chamber','cypher','fade','harbor','jett','kayo','killjoy','neon','omen','phoenix','raze','reyna','sage','skye','sova','viper','yoru']
print("Instant Lock for Valorant\nmade by hory0pioter")
for i in range(len(agn)):
	print(str(i + 1) + ": " + agn[i])

s = input("\nenter agent:  ")
if s.isdigit():
	s = int(s)
	s = agn[s - 1]
laa = s
s = s + '.png'
print("Selected: " + laa)
p = time()
for i in range(2):
	a = 1
	while a == 1:
		lk = pyautogui.locateOnScreen(s, confidence=.9, region=(500, 860, 900, 220))
		if not lk == None:
			a = 0
		p = time() - p
		p = round(p, 2)
		print("Time between ticks: " + str(p))
		p = time()
	print(lk)
	pyautogui.click(lk)
	pyautogui.moveTo(850, 838)
	pyautogui.click(959, 838)
