from tkinter import *
from tkinter import colorchooser

class Tags:

	#opens a tags window that allows the user to choose and manipulate tags.

	def __init__(self, availableTags, **kwargs):
		#availableTags argument is a list of any length, containing sub-lists of length 2. these sub-lists need to contain
		#a 'tag name' as index 0 and a hex colour as index 1. EXAMPLE:
			#availbleTags = [['tag 1', '#ff0000'], ['tag 2', '#00ffff'], ['cheese', '#ffff80']]

		self.btnFg = '#cbcbcb'
		self.mainBg = kwargs['bg'] if 'bg' in kwargs else '#000000'

		#if user wants a group of tags to be active upon creating the Tags object, user can pass it as a kwarg of 'default'
		self.defaultActiveTags = kwargs['default'] if 'default' in kwargs else []

		#if the user wants to invoke a function upon pressing confirm to exit the Tags() window, user can pass that function as a kwarg as 'exit'
		self.confirmExitInvoke = kwargs['exit'] if 'exit' in kwargs else self.null

		#if the user adds or modifies a tag and wants to invoke a function upon modification, user can pass that function as a kwarg as 'update'
		self.updateInvoke = kwargs['update'] if 'update' in kwargs else self.null

		#if the user delets an existing tag and wants to invoke a function upon deletion, user can pass that function as a kwarg as 'delete'
		self.deleteInvoke = kwargs['delete'] if 'delete' in kwargs else self.null

		#sotrage variable for all tags.
		self.tagsStored = availableTags

		#default new tag colour if user wants to create a new tag.
		self.newTagColour = '#ff0000'

		self.root = Toplevel(bg = self.mainBg)
		self.root.title('Tags chooser')
		self.root.geometry('460x700+0+50')

		self.showTagsWindow = Frame(self.root, bg = '#ffffff')
		self.showTagsWindow.pack(pady = 5)

		self.showTagsFrame = Frame(self.showTagsWindow, width = 401, height = 450, bg = '#131313')
		self.showTagsFrame.grid_propagate(0)
		self.showTagsFrame.grid(row = 0, column = 0, padx = 3, pady = 3)

		self.tagsDict = {}
		self.selectedTags = []

		#variable to check if there are no tags being shown on screen
		self.displayNone = False
		self.noTagsLabel = Label(self.showTagsFrame, text = 'No such tags \n exist.', font = ('arial', 30), bg = '#131313', fg = '#4f4f4f')

		for num, tag in enumerate(availableTags):
			text, hexColour = tag[0], tag[1]
			self.tagsDict[text] = self.setup_tag(text, hexColour)
			self.newTagPosition = self.display_tag(text, self.tagsDict[text], num)

		self.newTagsFrame = Frame(self.root, bg = '#1f2e1f')
		self.newTagButton = Button(self.newTagsFrame, text = 'New Tag', font = ('arial', 18), width = 8, bg = '#004d00', fg = self.btnFg, state = DISABLED)
		self.tagColourButton = Button(self.newTagsFrame, width = 2, bg = self.newTagColour, command = self.load_colour_chooser)
		self.deleteTagButton = Button(self.newTagsFrame, text = u'\u274c', font = ('arial', 10), width = 2,
		                              bg = self.btnFg, fg = '#6f0000', state = DISABLED)

		self.searchTagsLabel = Label(self.newTagsFrame, text = 'Search Tag(s):', font = ('arial', 16), bg = '#1f2e1f', fg = self.btnFg)
		self.searchTracker = StringVar(name = 'serachTracker')
		self.searchTracker.trace_add('write', self.display_searched_tags)
		self.searchTagEntry = Entry(self.newTagsFrame, font = ('arial', 22), width = 10, textvariable = self.searchTracker)
		self.searchTagEntry.focus_set()

		self.textTracker = StringVar(name = 'textTracker')
		self.textTracker.trace_add('write', self.update_new_tag)
		self.newTagEntry = Entry(self.newTagsFrame, width = 10, font = ('arial', 22), textvariable = self.textTracker)

		self.newTagButton.grid(row = 0, column = 0, pady = 10, padx = 20)
		self.newTagEntry.grid(row = 0, column = 1)
		self.tagColourButton.grid(row = 0, column = 2, padx = 20)
		self.deleteTagButton.grid(row = 1, column = 2)
		self.searchTagsLabel.grid(row = 1, column = 0, pady = 10)
		self.searchTagEntry.grid(row = 1, column = 1)
		self.newTagsFrame.pack(pady = 5)

		self.returnFrame = Frame(self.root, bg = '#2b1f2e')
		self.confirmButton = Button(self.returnFrame, text = 'Confirm', font = ('arial', 18), bg = '#2d2d53', fg = self.btnFg, width = 8,
		                           command = lambda: self.exit('confirm'))
		self.cancelButton = Button(self.returnFrame, text = 'Cancel', font = ('arial', 18), bg = '#532d2d', fg = self.btnFg, width = 8,
		                           command = lambda: self.exit('cancel'))

		self.confirmButton.grid(row = 0, column = 0, padx = 20, pady = 20)
		self.cancelButton.grid(row = 0, column = 1, padx = 20)
		self.returnFrame.pack()

		self.root.protocol('WM_DELETE_WINDOW', lambda: self.exit('cancel'))
		self.root.mainloop()

	def setup_tag(self, text, hexColour):

		rgb = tuple([int(hexColour[1:][2*i:2*(i+1)], 16) for i in range(3)])
		inactiveSelect = f"#{int(rgb[0] / 4):02x}{int(rgb[1] / 4):02x}{int(rgb[2] / 4):02x}"

		window = Frame(self.showTagsFrame, bg = hexColour)
		frame = Frame(window, width = 88, height = 22)
		button = Checkbutton(frame, text = text, font = ('arial', 9 - (len(text) // 8)), bg = '#1f1f1f', fg = '#ffffff', anchor = W, width = 10, 
		                     selectcolor = inactiveSelect, variable = StringVar(name = text))
		button.config(command = lambda text = text, colour = hexColour, button = button: self.select_tags(text, colour, button))

		return (hexColour, window, frame, button)

	def display_tag(self, tag, tagTuple, position):
		rgb = tuple([int(tagTuple[0][1:][2*i:2*(i+1)], 16) for i in range(3)])

		if tag in self.defaultActiveTags:
			tagTuple[3].select()
			tagTuple[3].config(bg = f'#{int(rgb[0] / 2):02x}{int(rgb[1] / 2):02x}{int(rgb[2] / 2):02x}',
			              selectcolor = '#ffffff')
			self.selectedTags.append((tag, tagTuple[0])) 

		row = position // 4
		column = position % 4

		tagTuple[2].pack_propagate(0)
		tagTuple[2].pack(padx = 1, pady = 1)
		tagTuple[3].pack(fill = BOTH, expand = 1)
		tagTuple[1].grid(row = row, column = column, padx = 5, pady = 5)

		return len(self.tagsDict)

	def update_tags(self, text, hexColour):
		#this function is called whenever the user creates and saves a new tag, or edits and updates an existing one.
		self.searchTagEntry.delete(0, END)

		if not (text in self.tagsDict): #new tag

			tagInfo = self.setup_tag(text, hexColour)
			self.tagsDict[text] = tagInfo
			self.select_tags(text, hexColour, tagInfo[3])
			tagInfo[3].select()

			row = self.newTagPosition // 4
			column = self.newTagPosition % 4

			tagInfo[2].pack_propagate(0)
			tagInfo[2].pack(padx = 1, pady = 1)
			tagInfo[3].pack(fill = BOTH, expand = 1)
			tagInfo[1].grid(row = row, column = column, padx = 5, pady = 5)

			self.tagsStored.append((text, hexColour))

			self.updateInvoke('new', text, hexColour)

		else:
			tagInfo = self.tagsDict[text]
			rgb = tuple([int(hexColour[1:][2*i:2*(i+1)], 16) for i in range(3)])
			tagInfo[1].config(bg = hexColour)
			tagInfo[3].config(selectcolor = f"#{int(rgb[0] / 4):02x}{int(rgb[1] / 4):02x}{int(rgb[2] / 4):02x}")

			for num, tag in enumerate(self.tagsStored):
				if text == tag[0]:
					self.tagsStored[num] = (text, hexColour)
					self.updateInvoke('edit', text, hexColour)
					break

		self.newTagPosition = len(self.tagsDict)
		self.newTagEntry.delete(0, END)

	def load_colour_chooser(self, *args):
		self.colorChoice = colorchooser.askcolor(title = 'Choose tag colour', initialcolor = self.newTagColour)
		self.newTagColour = self.colorChoice[1]
		self.tagColourButton.config(bg = self.colorChoice[1])

	def update_new_tag(self, *args):
		text = self.textTracker.get()
		self.newTagButton.config(command = lambda: self.update_tags(text, self.newTagColour))

		if text != '':
			if text not in self.tagsDict:
			   self.newTagButton.config(text = 'New Tag', state = NORMAL)
			   self.deleteTagButton.config(state = DISABLED, command = None)

			else:
				self.newTagButton.config(text = 'Edit Tag')
				self.newTagColour = self.tagsDict[text][0]
				self.tagColourButton.config(bg = self.newTagColour)
				self.deleteTagButton.config(state = NORMAL, command = lambda: self.delete_tag(text))

		else:
			 self.newTagButton.config(text = 'New Tag', state = DISABLED)
			 self.deleteTagButton.config(state = DISABLED, command = None)

	def delete_tag(self, text):

		self.tagsDict[text][1].destroy()

		tagList = [tag for tag in self.tagsDict]
		startIndex = tagList.index(text)

		counter = startIndex
		for tag in tagList[startIndex + 1:]:

			row = counter // 4
			column = counter % 4
			self.tagsDict[tag][1].grid_configure(row = row, column = column)

			counter += 1

		del self.tagsDict[text]
		self.deleteInvoke(text)

		self.newTagEntry.delete(0, END)
		self.newTagPosition -= 1

	def select_tags(self, tag, col, btn):
		rgb = tuple([int(col[1:][2*i:2*(i+1)], 16) for i in range(3)])
		pair = (tag, col)
		if not (pair in self.selectedTags):
			self.selectedTags.append(pair)
			btn.config(bg = f'#{int(rgb[0] / 2):02x}{int(rgb[1] / 2):02x}{int(rgb[2] / 2):02x}',
			           selectcolor = '#ffffff')

		else:
			self.selectedTags.remove(pair)
			btn.config(bg = '#1f1f1f',
			           selectcolor = f"#{int(rgb[0] / 4):02x}{int(rgb[1] / 4):02x}{int(rgb[2] / 4):02x}")

		self.searchTagEntry.delete(0, END)

	def display_searched_tags(self, *args):
		text = self.searchTagEntry.get()

		dispCounter = 0
		for tag in self.tagsDict:

			textExists = (text.lower() in tag.lower())

			row = dispCounter // 4
			column = dispCounter % 4

			if textExists and (self.tagsDict[tag][1].winfo_ismapped() == 1): #configure grid
				self.tagsDict[tag][1].grid_configure(row = row, column = column)
				dispCounter += 1

			elif (textExists and (self.tagsDict[tag][1].winfo_ismapped() == 0)) or (text == ''): #map
				self.tagsDict[tag][1].grid(row = row, column = column, padx = 5, pady = 5)
				dispCounter += 1

			elif not textExists and (self.tagsDict[tag][1].winfo_ismapped() == 1): #unmap
				self.tagsDict[tag][1].grid_forget()

			elif not textExists and (self.tagsDict[tag][1].winfo_ismapped() == 0): #do nothing
				pass

		if (dispCounter == 0) and (not self.displayNone):
			self.displayNone = True
			self.noTagsLabel.grid(row = 0, column = 0, padx = 79, pady = 149)

		elif (dispCounter > 0) and self.displayNone:
			self.displayNone = False
			self.noTagsLabel.grid_forget()

	def exit(self, keyword):

		self.searchTracker.trace_remove('write', self.searchTracker.trace_vinfo()[0][1])
		self.textTracker.trace_remove('write', self.textTracker.trace_vinfo()[0][1])
		self.searchTagEntry.delete(0, END)
		self.newTagEntry.delete(0, END)

		if keyword == 'confirm':
			#executes a function passed in the __init__ method, as long as it accepts at least one argument.
			self.confirmExitInvoke(self.selectedTags)

		elif keyword == 'cancel':
			pass

		self.root.destroy()
		del self

	def null(self, *args, **kwargs):
   	#this function is called only by class attributes which depend on functions as kwargs being passed into the __init__ method.
   	#if no kwarg is passed into these attributes, then this function will be called. else, the functon passed in __init__ will be called.
		pass
      