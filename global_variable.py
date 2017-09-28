#created by malcolm mccarthy
#created on sept 2017
#created for ICS3U
#program shows difference between global and local variables

import ui

variableX = 25

def local_button_touch_up_inside(sender):
	  # shows what happens with local variables
	  
	  variableX = 10
	  variableY = 30
	  variableZ = variableX + variableY
	  
	  view['local_answer_label'].text = str(variableZ)

def global_button_touch_up_inside(sender):
	  #shows what happens with global variables
	  
	  global variableX
	  variableX = variableX + 1
	  variableY = 30
	  variableZ = variableX + variableY
	  
	  view['global_answer_label'].text = str(variableZ)
	  
view = ui.load_view()
view.present('sheet')
