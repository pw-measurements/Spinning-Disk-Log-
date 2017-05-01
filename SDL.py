from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
import csv
import time
import os
from time import gmtime, strftime
instruemnt="spinning disk"
class UserData(BoxLayout):
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
			
		if item=="timein":
			if ":" not in value:
				return True
			else:
				return False
		if item=="timeout":
			if ":" not in value:
				return True
			else:
				return False

		if item=="afil":
			value=value.strip().lower()
			if value!="y" and value !="n":
				return True
			else:
				return False
				
		if item=="slider":
			if value<.25:
				return True
			else:
				return False
		
		if item=="sample":
			if len(value)<2:
				return True
			else:
				return False
		
		if item=="submit":
			if len(value)<2:
				return True
			else:
				return False
	
	def submit(self):
		with open("Spinning_Disk_Log.csv",'a') as file_object:
			file_object.write(
				strftime("%b %d %Y")
				+","
				+self.ids.name.text.strip().title()
				+","
				+self.ids.group.text.strip().title()
				+","
				+self.ids.dept.text.strip()
				+","
				+instruemnt
				+","
				+self.ids.timein.text.strip()
				+","
				+self.ids.timeout.text.strip()
				+","
				+str(self.ids.timeused.value)
				+","
				+self.ids.affiliation.text.strip()
				+","
				+self.ids.sample.text.strip()
				+","
				+self.ids.comment.text.strip()
				+"\n"
				)
			if "scientist time" in self.ids.comment.text.strip().lower():
				file_object.write(
					strftime("%b %d %Y")
					+","
					+self.ids.name.text.strip().title()
					+","
					+self.ids.group.text.strip().title()
					+","
					+self.ids.dept.text.strip()
					+","
					+"Scientist Time"
					+","
					+self.ids.timein.text.strip()
					+","
					+self.ids.timeout.text.strip()
					+","
					+str(self.ids.timeused.value)
					+","
					+self.ids.affiliation.text.strip()
					+","
					+self.ids.sample.text.strip()
					+","
					+"Samples for "+self.ids.name.text.strip().title()
					+"\n"
					) 	
		quit()
class SDLApp(App):
	User_data={"date":0,"name":0,"group":0,"dept":0,"timein":0,"timeout":0,"timeused":0,"affiliation":0,"sample":0,"comment":0}
	def build (self):
		self.title="Spinning Disk Log"
		return UserData()

if __name__=="__main__":
	SDLApp().run()
