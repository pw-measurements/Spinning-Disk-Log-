from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
import csv
import time
import os
from time import gmtime, strftime
from kivy.config import Config
Config.set('graphics', 'width', '600')
Config.set('graphics', 'height', '100')
class launcher(BoxLayout):

	
	def checker(self,item,value):
		if item=="name":
			if len(value)<2:
				return True
			else:
				return False
		if item=="group":
			if len(value)<2:
				return True
			else:
				return False
		if item=="dept":
			if len(value)<2:
				return True
			else:
				return False
			
		if item=="launch":
			if len(value)<2:
				return True
			else:
				return False
	def launch(self):
		with open("Launcher Log.csv",'a') as file_object:
			file_object.write(
				strftime("%b %d %Y")
				+","
				+strftime("%X")
				+","
				+self.ids.name.text.strip().title()
				+","
				+self.ids.group.text.strip().title()
				+","
				+self.ids.dept.text.strip()
				+"\n"
				)
		os.startfile('C:\\Program Files (x86)\\Microsoft Office\\root\\Office16\\excel.exe')
		exit()		
class LauncherApp(App):
	def build (self):
		self.title="Spinning Disk Launcher"
		return launcher()
	

if __name__=="__main__":
	LauncherApp().run()
