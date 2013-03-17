import wx

class hello_world(wx.Frame):
	def __init__(self,parent,id):
		wx.Frame.__init__(self,parent,id,'Window', size=(300,200))


if __name__=='__main__':
	app=wx.PySimpleApp()
	frame=hello_world(parent=None,id=-1)
	frame.Show()
	app.MainLoop()