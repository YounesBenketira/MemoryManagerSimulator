from FrameQueue import FrameQueue
from tkinter import *
from tkinter.messagebox import showerror

WIDTH = 850
HEIGHT = 550

root = Tk()
root.title("Memory Management Simulator")
root.configure(bg="#FAFAFA")  # Setting background color to white
root.geometry(str(WIDTH) + "x" + str(HEIGHT))

# FRAMES

upperFrame = Frame(root, borderwidth=1, relief="solid", bg="#FAFAFA") \
	.place(relx=0.5, rely=0.03, relwidth=0.95, relheight=0.65, anchor=N)

lowerFrame = Frame(root, borderwidth=1, relief="solid", bg="#FAFAFA") \
	.place(relx=0.5, rely=0.75, relwidth=0.95, relheight=0.22, anchor=N)

# Methods
entries = list()
elements = []


# add method that adds entry fields in the gui to allow user to enter resource requests
def add():
	clear()

	try:
		int(numProccessesEntry.get())
	except ValueError:
		showerror("Input Error", "Number of pages must be an Integer")  # If invalid entry show error
		return

	numProcesses = int(numProccessesEntry.get())  # Get the amount of processes entered
	# lowestY = 0.25 || highestY = 0.65 || range = 0.4
	# lowestX = 0.049 || highestX = 0.95 || range = 0.9
	sizeP = int(numProccessesEntry.get())
	width = 0.9 / sizeP

	for i in range(0, numProcesses):  # Create entry, place it, then and add it into entries list
		entry = Entry(upperFrame, bg="#FAFAFA", borderwidth=1, relief="solid", font=("inconsolata", 20), justify=CENTER)
		entry.place(relx=0.049 + (width * i), rely=0.07, relwidth=width + 0.01, relheight=0.15, anchor=NW)

		entries.append(entry)


# clear method that deletes all entries and elements on the gui
def clear():
	#  Clear the entries and entries list and remove them from gui
	for i in range(len(entries) - 1, -1, -1):
		entries[i].destroy()
		entries.pop()

	clearResults()


def clearResults():
	#  Clear the elements and elements list and remove them from gui
	for i in range(len(elements) - 1, -1, -1):
		elements[i].destroy()
		elements.pop()


def execute():
	clearResults()

	try:
		int(numFramesEntry.get())
	except ValueError:
		showerror("Input Error", "Number of frames must be an Integer")  # If invalid entry show error
		return

	try:
		int(numProccessesEntry.get())
	except ValueError:
		showerror("Input Error", "Number of pages must be an Integer")  # If invalid entry show error
		return

	frames = int(numFramesEntry.get())  # Get number of frames
	frameQueue = FrameQueue(frames)  # Create FrameQueue Object

	sizeF = frameQueue.getSize()
	sizeP = len(entries)

	# lowestY = 0.25 || highestY = 0.65 || range = 0.4
	# lowestX = 0.049 || highestX = 0.95 || range = 0.9
	height = 0.4 / sizeF
	width = 0.9 / sizeP

	counter = 0  # Variable to keep track if PageFault was incremented

	for i in range(0, sizeP):  # For each number user enters
		if algo.get() == "FIFO":
			frameQueue.fifoE(entries[i].get())  # add number into queue using fifoE method
		else:
			frameQueue.lruE(entries[i].get())

		if frameQueue.getPF() == counter:  # if page fault was not incremented set pf to false
			pf = False
		else:  # else indicate that there was a page fault and increment counter
			pf = True
			counter += 1

		for o in range(0, frameQueue.getSize()):  # For loop that updates the gui to show whats in the queue
			queue = frameQueue.getQ()

			try:  # This is to avoid the errors we get when we run execute with an empty queue
				element = str(queue[o])
			except IndexError:
				element = ""

			if element == str(entries[
								  i].get()):  # If the element we are going to display is the one entered, check if there was a page fault
				if pf:  # If there was a page fault then set the color to red
					color = "#ff1100"
				else:  # If there wasn't set the color to green
					color = "#40de02"
			else:  # Else set color to black
				color = "#030303"

			#  Display all elements in the queue at this given time
			elementLabel = Label(upperFrame, text=element, borderwidth=1, relief="solid", font=("inconsolata", 20),
								 bg="#FAFAFA", fg=color, anchor=CENTER)
			elementLabel.place(relx=0.049 + (width * i), rely=0.25 + (height * o), relwidth=width + 0.01,
							   relheight=height + 0.01, anchor=NW)

			elements.append(elementLabel)

	# Display page faults when done
	pageFaultLabel = Label(root, text="Page Faults: " + str(frameQueue.getPF()), bg="#FAFAFA", font=("inconsolata", 19)) \
		.place(relx=0.77, rely=0.68, relwidth=0.22, relheight=0.07)

	# Display page fault ratio when done
	ratio = round(float(frameQueue.getPF()) / sizeP, 2)
	pageFaultRatioLabel = Label(root, text="PF Ratio: " + str(ratio), bg="#FAFAFA", font=("inconsolata", 19)) \
		.place(relx=0.57, rely=0.68, relwidth=0.2, relheight=0.07)


# Labels on Lower Frame
algoList = ["FIFO", "LRU"]
algo = StringVar(root)
algo.set(algoList[0])

numProccessesLabel = Label(lowerFrame, text="# Of Pages ", font=("inconsolata", 20), bg="#FAFAFA", anchor=W) \
	.place(relx=0.05, rely=0.76, relwidth=0.25, relheight=0.1)

numProccessesEntry = Entry(lowerFrame, bg="#FAFAFA", borderwidth=1, font=("inconsolata", 20), relief="solid",
						   justify=CENTER)
numProccessesEntry.place(relx=0.3, rely=0.775, relwidth=0.15, relheight=0.07)

numFramesLabel = Label(lowerFrame, text="# Of Frames ", font=("inconsolata", 20), bg="#FAFAFA", anchor=W) \
	.place(relx=0.05, rely=0.86, relwidth=0.2, relheight=0.1)

numFramesEntry = Entry(lowerFrame, bg="#FAFAFA", borderwidth=1, relief="solid", font=("inconsolata", 20),
					   justify=CENTER)
numFramesEntry.place(relx=0.3, rely=0.87, relwidth=0.15, relheight=0.07)

algoEntry = OptionMenu(lowerFrame, algo, *algoList)
algoEntry.place(relx=0.6, rely=0.87, relwidth=0.15, relheight=0.075)

addBtn = Button(lowerFrame, text="Add Pages", font=("inconsolata", 13), command=add) \
	.place(relx=0.6, rely=0.77, relwidth=0.15, relheight=0.075)

clearBtn = Button(lowerFrame, text="Clear", font=("inconsolata", 13), command=clear) \
	.place(relx=0.78, rely=0.77, relwidth=0.15, relheight=0.075)

executeBtn = Button(lowerFrame, text="Execute", font=("inconsolata", 13), command=execute) \
	.place(relx=0.78, rely=0.87, relwidth=0.15, relheight=0.075)

root.mainloop()
