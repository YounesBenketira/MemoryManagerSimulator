from FrameQueue import FrameQueue
from tkinter import *

''' This Code is to test the logic behind the DataStructure that was made
nums = [0,1,2,3,0,1,4,0,1,2,3,4]
letters = ['A','B','C','A','D','A','C','D','B','C','A']

frameQueue = FrameQueue(4)

frameQueue.fifo(nums)
print(frameQueue.getPF())

frameQueue.lru(letters)
print(frameQueue.getPF())
'''

WIDTH = 850
HEIGHT = 550

root = Tk()
root.title("Memory Management Simulator")
root.configure(bg="#FAFAFA")
root.geometry(str(WIDTH) + "x" + str(HEIGHT))

# FRAMES

upperFrame = Frame(root, borderwidth=1, relief="solid", bg="#FAFAFA")\
	.place(relx=0.5, rely=0.03, relwidth=0.95, relheight=0.65, anchor=N)

lowerFrame = Frame(root, borderwidth=1, relief="solid", bg="#FAFAFA")\
	.place(relx=0.5, rely=0.75, relwidth=0.95, relheight=0.22, anchor=N)

# Methods
entries = list()
elements = []

# add method that adds entry fields in the gui to allow user to enter resource requests
def add():
	clear()
	numProcesses = int(numProccessesEntry.get())  # Get the amount of processes entered

	for i in range(0,numProcesses):  # Create entry, place it, then and add it into entries list
		entry = Entry(upperFrame, bg="#FAFAFA", borderwidth=1, relief="solid", font=("inconsolata", 20), justify=CENTER)
		entry.place(relx=0.14 + (0.1*i), rely=0.13, relwidth=0.09, relheight=0.15, anchor=E)

		entries.append(entry)

# clear method that deletes all entries and elements on the gui
def clear():
	#  Clear the entries and entries list and remove them from gui
	for i in range(len(entries)-1, -1, -1):
		entries[i].destroy()
		entries.pop()

	#  Clear the elements and elements list and remove them from gui
	for i in range(len(elements)-1, -1, -1):
		elements[i].destroy()
		elements.pop()

def execute():
	frames = int(numFramesEntry.get())  # Get number of frames
	frameQueue = FrameQueue(frames)  # Create FrameQueue Object

	if algo.get() == "FIFO":
		counter = 0  # Variable to keep track if PageFault was incremented
		for i in range(0, len(entries)):  # For each number user enters
			frameQueue.fifoE(entries[i].get())  # add number into queue using fifoE method

			if frameQueue.getPF() == counter:  # if pagefault was not incremented set pf to false
				pf = False
			else:  # else indicate that there was a pagefault and increment counter
				pf = True
				counter += 1

			for o in range(0, frameQueue.getSize()):  # For update the gui to show whats in the queue
				queue = frameQueue.getQ()
				try:
					element = str(queue[o])
				except IndexError:
					element = ""

				if element == str(entries[i].get()):  # If the element we are going to display is the one entered, check if there was a page fault
					if pf:  # If there was a pagefault then set the color to red
						color = "#ff1100"
					else:  # If there wasnt set the color to green
						color = "#40de02"
				else:  # Else set color to black
					color = "#030303"

				#  Display all elements in the queue at this given time
				elementLabel = Label(upperFrame, text=element, borderwidth=1, relief="solid", font=("inconsolata", 20), bg="#FAFAFA", fg=color, anchor=CENTER)
				if frameQueue.getSize() == 3:
					elementLabel.place(relx=0.14 + (0.1*i), rely=0.3 + (0.14*o), relwidth=0.09, relheight=0.15, anchor=E)
				else:
					elementLabel.place(relx=0.14 + (0.1 * i), rely=0.3 + (0.1 * o), relwidth=0.09, relheight=0.101, anchor=E)
				elements.append(elementLabel)

		# Display page faults when done
		pageFaultLabel = Label(root, text="Page Faults: " + str(frameQueue.getPF()), bg="#FAFAFA", font=("inconsolata", 19))\
			.place(relx=0.77, rely=0.68, relwidth=0.2, relheight=0.07)
	else:  # LRU algorithm
		print()


algoList = ["FIFO","LRU"]
algo = StringVar(root)
algo.set(algoList[0])

numProccessesLabel = Label(lowerFrame, text="# Of Pages ", font=("inconsolata", 20), bg="#FAFAFA", anchor=W)\
	.place(relx=0.05, rely=0.76, relwidth=0.25, relheight=0.1)

numProccessesEntry = Entry(lowerFrame, bg="#FAFAFA", borderwidth=1, font=("inconsolata", 20),  relief="solid", justify=CENTER)
numProccessesEntry.place(relx=0.3, rely=0.775, relwidth=0.15, relheight=0.07)

numFramesLabel = Label(lowerFrame, text="# Of Frames ", font=("inconsolata", 20), bg="#FAFAFA", anchor=W)\
	.place(relx=0.05, rely=0.86, relwidth=0.2, relheight=0.1)

numFramesEntry = Entry(lowerFrame, bg="#FAFAFA", borderwidth=1, relief="solid", font=("inconsolata", 20), justify=CENTER)
numFramesEntry.place(relx=0.3, rely=0.87, relwidth=0.15, relheight=0.07)

algoEntry = OptionMenu(lowerFrame, algo, *algoList)
algoEntry.place(relx=0.6, rely=0.87, relwidth=0.15, relheight=0.075)

addBtn = Button(lowerFrame, text="Add Pages", font=("inconsolata",13), command=add)\
	.place(relx=0.6, rely=0.77, relwidth=0.15, relheight=0.075)

clearBtn = Button(lowerFrame, text="Clear", font=("inconsolata",13), command=clear)\
	.place(relx=0.78, rely=0.77, relwidth=0.15, relheight=0.075)

executeBtn = Button(lowerFrame, text="Execute", font=("inconsolata",13), command=execute)\
	.place(relx=0.78, rely=0.87, relwidth=0.15, relheight=0.075)

root.mainloop()