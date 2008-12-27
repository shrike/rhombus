#!/usr/bin/env python

import wx

class ExWxpython(wx.Frame):
	def __init__(self, parent, title):
		wx.Frame.__init__(self, parent, -1, title,
						  pos=(150, 150), size=(500, 230))

		# Create Menu Bar
		self.createMenuBar()

		# Create Status Bar
		self.sb = self.CreateStatusBar()
		self.sb.SetStatusText("Done.")	

		# Here comes the Panel
		self.createPanel()


	def createPanel(self):
		panel = wx.Panel(self)

		mainHbox = wx.BoxSizer(wx.HORIZONTAL)

		vbox1 = wx.BoxSizer(wx.VERTICAL)
		
		hbox1 = wx.BoxSizer(wx.HORIZONTAL)
		labelName = wx.StaticText(panel, -1, "Name:")
		hbox1.Add(labelName, 0, wx.RIGHT, 8)
		textName = wx.TextCtrl(panel, -1)
		hbox1.Add(textName, 1)

		vbox1.Add(hbox1, 0, wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, 0)
		
		optionFresh = wx.RadioButton(panel, -1, "Freshman")
		vbox1.Add(optionFresh, 2)

		optionSofo = wx.RadioButton(panel, -1, "Sophomore")
		vbox1.Add(optionSofo, 2)
		optionJuni = wx.RadioButton(panel, -1, "Junior")
		vbox1.Add(optionJuni, 2)
		optionSeni = wx.RadioButton(panel, -1, "Senior")
		vbox1.Add(optionSeni, 2)
		
		buttonOK = wx.Button(panel, -1, "OK")
		vbox1.Add(buttonOK, 2)
		
		mainHbox.Add(vbox1, 0, wx.EXPAND | wx.ALL, 10)

		#mainHbox.Add((-1, 100))

		vbox2 = wx.BoxSizer(wx.VERTICAL)
		
		labelClass = wx.StaticText(panel, -1, "Classes:")
		vbox2.Add(labelClass, 0)
		checkA = wx.CheckBox(panel, -1, "Class A")
		vbox2.Add(checkA, 0)
		checkB = wx.CheckBox(panel, -1, "Class B")
		vbox2.Add(checkB, 0)
		checkC = wx.CheckBox(panel, -1, "Class C")
		vbox2.Add(checkC, 0)
		checkD = wx.CheckBox(panel, -1, "Class D")
		vbox2.Add(checkD, 0)
		checkE = wx.CheckBox(panel, -1, "Class E")
		vbox2.Add(checkE, 0)
		commandCancel = wx.Button(panel, -1, "Cancel")
		vbox2.Add(commandCancel, 0)
		
		mainHbox.Add(vbox2, 0, wx.EXPAND | wx.ALL, 10)

		vbox3 = wx.BoxSizer(wx.VERTICAL)
		labelNote = wx.StaticText(panel, -1, "Notes:")
		vbox3.Add(labelNote, 2)
		textNote = wx.TextCtrl(panel, -1, "Enter some notes here")
		vbox3.Add(textNote, 2)
		
		#vbox3.Add((-1, 200))    					Donno what this does
		#											Related to the form
		
		mainHbox.Add(vbox3, 0, wx.EXPAND | wx.ALL, 10)
		
		panel.SetSizer(mainHbox)
		self.Centre()
		panel.Layout()


	def createMenuBar(self):
		# Declare Menubar
		menuBar = wx.MenuBar()

		# File Menu
		fileMenu = wx.Menu()

		fileMenu.Append(wx.ID_SAVE, "&Save\tCtrl-S", "Save")
		fileMenu.Append(wx.ID_EXIT, "E&xit\tCtrl-Q", "Exit")
		self.Bind(wx.EVT_MENU, self.procClose, id=wx.ID_EXIT)
		
		menuBar.Append(fileMenu, "&File")

		# Edit Menu
		editMenu = wx.Menu()
		editMenu.Append(wx.ID_CUT, "C&ut\tCtrl-X", "Cut")
		editMenu.Append(wx.ID_COPY, "&Copy\tCtrl-C", "Copy")
		editMenu.Append(wx.ID_PASTE, "&Paste\tCtrl-V", "Paste")

		menuBar.Append(editMenu, "&Edit")

		# Help Menu
		helpMenu = wx.Menu()
		helpMenu.Append(wx.ID_HELP, "&About", "About")
		menuBar.Append(helpMenu, "&Help")

		# Set the MenuBar
		self.SetMenuBar(menuBar)

	def procClose(self, evt):
		print "Close the app."
		self.Close()


class MyApp(wx.App):
	def OnInit(self):
		frame = ExWxpython(None, "DEMO")
		self.SetTopWindow(frame)

		print "Debug info printed HERE:"

		frame.Show(True)
		return True

app = MyApp(redirect=True)
app.MainLoop()
