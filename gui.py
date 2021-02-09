import tkinter as tk
import passwordgen as core

def doPasswordGen():
	#function used to create a password using the maincode.py create_password function.
	givenSize = entrySize.get()
	givenPass = entryPass.get()
	givenApp = entryApp.get()
	genpass = core.create_password(givenPass, givenApp, givenSize)
	genPassword["text"] = genpass
	
def doClipboardAppend():
	#Function used to copy the generated password onto the clipboard
	mainWindow.clipboard_clear()
	mainWindow.clipboard_append(genPassword["text"])
	mainWindow.update

#window setup
mainWindow = tk.Tk()
mainWindow.title("Simple password generator")
mainWindow.resizable(width = False, height = True)

#creating entry boxes for text input by user
inputFrame = tk.Frame(master = mainWindow)
inputSize = tk.Label(master = inputFrame, text = "Desired Size:")
entrySize = tk.Entry(master = inputFrame, width = 15)
inputPass = tk.Label(master = inputFrame, text = "Global Password:")
entryPass = tk.Entry(master = inputFrame, width = 15)
inputApp = tk.Label(master = inputFrame, text = "Application Name:")
entryApp = tk.Entry(master = inputFrame, width = 15)

#grid for setting layout of the inputFrame
inputSize.grid(row=0,column=0,sticky="e")
entrySize.grid(row=1,column=0,sticky="e")
inputPass.grid(row=0,column=1)
entryPass.grid(row=1,column=1)
inputApp.grid(row=0,column=2,sticky="w")
entryApp.grid(row=1,column=2,sticky="w")

#create the button to generate the password.
genButton = tk.Button(master=mainWindow, text="Generate Password", command=lambda:[doPasswordGen(),clipButton.grid()])
outputFrame = tk.Frame(master=mainWindow)
genPassLabel = tk.Label(master=outputFrame, text="Generated Password:")
genPassword = tk.Label(master=outputFrame, text="")
genPassLabel.grid(row=0,column=0,sticky="n")
genPassword.grid(row=1,column=0,sticky="s")

#create second button for adding output to clipboard
clipButton = tk.Button(master=mainWindow, text="Add to clipboard", command=doClipboardAppend)
clipButton.grid(row=3,column=0,sticky="s")
clipButton.grid_forget()

#make final layout using grid()
inputFrame.grid(row=0, column=0, sticky="n")
genButton.grid(row=1, column=0, pady=10)
outputFrame.grid(row=2, column=0, pady=10)

mainWindow.mainloop()