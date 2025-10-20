from tkinter import *
from tkinter import ttk

# from knowledge import *
from utilities import *

class visualiser_interface:

	def __init__(self, Root, **kwargs):
		self.wantedColumns = kwargs['columns'] if 'columns' in kwargs else {1: 48, 2: 26, 3: 20, 4: 12}
		width = kwargs['width'] if 'width' in kwargs else 1010
		self.height = kwargs['height'] if 'height' in kwargs else 500

		#setup of the visualiser interface
		self.mainWin = Frame(Root, bg = 'black')

		self.interfaceWin = Frame(self.mainWin, bg = 'cyan')
		self.interfaceFrame = Frame(self.interfaceWin, bg = '#000000')

		self.displayWin = Frame(self.interfaceFrame, bg = '#000000', width = width, height = self.height)
	
		self.displayCanvas = Canvas(self.displayWin, bg = '#000000', width = width, height = self.height,
									bd = 0, highlightthickness = 0, relief = RIDGE)

		self.displayFrame = Frame(self.displayCanvas, bg = '#000000')

		self.scrollWin = Frame(self.interfaceFrame, bg = 'blue', height = self.height, width = 20)
		self.scrollbar = ttk.Scrollbar(self.scrollWin, orient = VERTICAL, command = self.displayCanvas.yview)

		self.displayCanvas.configure(yscrollcommand = self.scrollbar.set)
		self.displayCanvas.bind('<Configure>', lambda e: self.displayCanvas.configure(scrollregion = self.displayCanvas.bbox('all')))
		self.displayCanvas.create_window((0, 0), window = self.displayFrame, anchor = 'nw')

		#sorting interface
		self.sortType = StringVar(value = 'date')

		#searching interface
		self.searchType = StringVar(value = 'english')

		self.searchVar = StringVar(name = 'searching')
		self.searchVar.trace_add('write', lambda *args: self.search_for(self.searchType.get()))

		if not ('entry' in kwargs):
			self.searchEntry = Entry(self.searchingInterface, width = 10, font = ('arial', 14),
									 textvariable = self.searchVar)
		else:
			self.searchEntry = kwargs['entry']
			self.searchEntry.config(textvariable = self.searchVar)


	def load(self, **kwargs):
		row = kwargs['row'] if 'row' in kwargs else 0
		column = kwargs['column'] if 'column' in kwargs else 0
		self.interfaceWin.pack(side = TOP, pady = 5)
		self.interfaceFrame.grid(row = 0, column = 0, padx = 3, pady = 3)
		self.displayWin.grid(row = 0, column = 0)
		self.displayWin.grid_propagate(0)
		self.displayCanvas.grid(row = 0, column = 0, sticky = 'w')
		self.scrollbar.grid(row = 0, column = 0, ipady = int(self.height / 2) - 23, sticky = 'n', pady = 1)
		self.scrollWin.grid(row = 0, column = 1)

		self.mainWin.grid(row = row, column = column)

	def unload(self):
		self.interfaceWin.pack_forget()		
		self.interfaceFrame.grid_forget()
		self.displayWin.grid_forget()
		self.displayCanvas.grid_forget()
		self.scrollbar.grid_forget()
		self.scrollWin.grid_forget()

		self.mainWin.grid_forget()

	def setup_data(self, kanjidata, hiragana_data, katakana_data, **kwargs):
		self.enterLabel_cmd = kwargs['enterLabel'] if 'enterLabel' in kwargs else None
		self.leaveLabel_cmd = kwargs['leaveLabel'] if 'leaveLabel' in kwargs else None
		self.leftClick_cmd = kwargs['leftclick'] if 'leftclick' in kwargs else None
		#this function must be called to create all the kanji labels and allocate each of their filters.

		#dictionary of {kanji: kanji filters}
		self.allKanjiFilters = {}
		for kanji in kanjidata:

			kanaCharacters = ','.join([kana for kana in kanjidata[kanji]['words']])
			englishWords = ','.join([eng for engList in [kanjidata[kanji]['words'][kana] for kana in kanjidata[kanji]['words']] for eng in engList])

			self.allKanjiFilters[kanji] = {'kana': kanaCharacters,
										   'english': englishWords,
										   'grade': kanjidata[kanji]['grade'],
										   'jlpt': kanjidata[kanji]['jlpt'],
										   'date': kanjidata[kanji]['date']}

		self.allHiragana = {data[0]: (data[1].split(','), data[2]) for data in hiragana_data}
		self.allKatakana = {data[0]: data[1].split(',') for data in katakana_data}

		widthMaintainer = Frame(self.displayFrame, bg = '#000000', width = 1006)
		widthMaintainer.grid(row = 0, column = 0)

		highestKanjiLength = max([len(kanji) for kanji in kanjidata])
		self.setup_frames(highestKanjiLength)
		self.load_kanji_length_frames()

		#configured by searching for something
		self.currentSearchText = ''

		#configured whenever a sorting button is selected, and will change size if a search condition is applied
		self.sortedSearchResults = [kanji for kanji in kanjidata]

		#creation of frames
		lengthCounters = {1: 0, 2: 0, 3: 0, 4: 0}
		self.allKanjiLabels = {}
		for kanji in self.sortedSearchResults:
			kanjiLength = len(kanji)

			row, column = self.get_coordinates(lengthCounters[kanjiLength], self.wantedColumns[kanjiLength])
			self.allKanjiLabels[kanji] = self.create_label(kanji, self.kanjiLengthFrames[kanjiLength - 1], row, column)

			lengthCounters[kanjiLength] += 1

		self.hiraganaLabels = {kana: self.create_hiragana_label(num, kana, *self.allHiragana[kana]) for (num, kana) in enumerate(self.allHiragana)}
		self.katakanaLabels = {kana: self.create_katakana_label(num, kana, self.allKatakana[kana]) for (num, kana) in enumerate(self.allKatakana)}

		self.resize_display()

	def create_katakana_label(self, pos, kana, english):
		row, column = self.get_coordinates(pos, 4, startleft = True)
		kanaLabel, englishLabel, winborder = self.get_new_label(row + column, self.katakanaFrame)

		kanaLabel.config(text = kana)
		englishText = self.format_english_text(english)
		englishLabel.config(text = englishText)

		self.display_kana_label(winborder, row, column)

		return winborder

	def create_hiragana_label(self, pos, kana, english, kanji):
		row, column = self.get_coordinates(pos, 4, startleft = True)
		kanaLabel, englishLabel, winborder = self.get_new_label(row + column, self.hiraganaFrame)

		text = kana if (kanji == '-') else f'{kana} ({kanji})'
		kanaLabel.config(text = text)

		englishText = self.format_english_text(english)
		englishLabel.config(text = englishText)

		self.display_kana_label(winborder, row, column)

		return winborder

	def get_new_label(self, pos, frame):
		bg = '#000000' if (frame == self.hiraganaFrame and pos % 2 == 0) or (frame == self.katakanaFrame and pos % 2 == 1) else '#1a1a1a'
		winborder = Frame(frame, width = 245, height = 110, bg = '#808080')
		window = Frame(winborder, width = 243, height = 108, bg = bg)
		window.grid(row = 0, column = 0, padx = 1, pady = 1)
		window.grid_propagate(0)
		frame = Frame(window, bg = bg)
		frame.grid(row = 0, column = 0)

		kanaLabel = Label(frame, font = ('arial', 18), bg = bg, fg = '#ffff00', width = 17)
		kanaLabel.grid(row = 0, column = 0)

		englishLabel = Label(frame, font = ('arial', 14), bg = bg, fg = '#ffff00', anchor = 'w', justify = 'left')
		englishLabel.grid(row = 1, column = 0, padx = 2, sticky = 'w')

		return (kanaLabel, englishLabel, winborder)

	def format_english_text(self, engs):
		engtext = ''
		for num, eng in enumerate(engs, start = 1):
			if num == len(engs):
				engtext += eng
			elif num % 2 == 1:
				engtext += f'{eng}, '
			else:
				engtext += f'{eng},\n'
		return engtext

	def display_kana_label(self, win, row, column):
		win.grid(row = row, column = column, padx = 3, pady = 3)
		win.grid_propagate(0)

	def setup_frames(self, kanjinum):
		self.kanjiLengthFrames = [Frame(self.displayFrame, bg = '#000000') for _ in range(kanjinum)]
		self.hiraganaFrame = Frame(self.displayFrame, bg = '#000000')
		self.katakanaFrame = Frame(self.displayFrame, bg = '#000000')

	def resize_display(self):
		self.mainWin.update_idletasks()
		self.displayCanvas.configure(scrollregion = self.displayCanvas.bbox('all'))

	def get_sorted_list(self, category, *args):
		usedList = args[0] if len(args) > 0 else self.sortedSearchResults
		if category == 'date':
			return [kanji for kanji in self.allKanjiFilters if kanji in usedList]

		else:
			sortedList = []
			indexTuple = {
						  'grade': ('1', '2', '3', '4', '5', '6', 'JH', '-'),
						  'jlpt': ('N5', 'N4', 'N3', 'N2', 'N1', '-')
						  }[category]

			indexCounters = {key: 0 for key in indexTuple}
			for kanji in usedList:
				categoryKey = self.allKanjiFilters[kanji][category]
				sortedList.insert(indexCounters[categoryKey], kanji)
				for key in indexTuple[indexTuple.index(categoryKey):]:
					indexCounters[key] += 1

			return sortedList

	def sort_by(self, category):
		self.sortType.set(category)
		self.sortedSearchResults = self.get_sorted_list(category)
		self.display_sorted_results(self.sortedSearchResults)

	def search_for(self, searchingFor, *args):
		searchText = self.searchVar.get()
		if len(searchText) > len(self.currentSearchText):
			compareList = [kanji for kanji in self.sortedSearchResults]
			self.sortedSearchResults = self.reduce_results(searchText, self.sortedSearchResults)
			narrower = True

		else:
			compareList = [kanji for kanji in self.sortedSearchResults]
			self.sortedSearchResults = self.lengthen_results(searchText, self.sortedSearchResults)
			narrower = False

		self.currentSearchText = searchText
		self.display_searched_results(self.sortedSearchResults, compareList, narrower)
		self.resize_display()

	def reduce_results(self, searchText, currentSearchResults):
		searchType = self.searchType.get()
		results = []

		for kanji in currentSearchResults:
			searchFor = kanji if searchType == 'kanji' else self.allKanjiFilters[kanji][searchType]


			if searchText in searchFor:
				results.append(kanji)

		return results

	def lengthen_results(self, searchText, currentSearchResults):
		searchType = self.searchType.get()
		results = []
		for kanji in self.get_sorted_list(self.sortType.get(), self.allKanjiFilters):
			searchFor = kanji if searchType == 'kanji' else self.allKanjiFilters[kanji][searchType]
			if (searchText in searchFor):
				results.append(kanji)

		return results

	def select_search_type(self, type_, *args):
		self.searchEntry.delete(0, END)
		self.searchType.set(type_)
		self.searchVar.trace_remove('write', self.searchVar.trace_info()[0][1])
		self.searchVar.trace_add('write', lambda *args: self.search_for(self.searchType.get()))

	def display_searched_results(self, newList, comparrisonList, isNarrower):
		lengthCounters = {1: 0, 2: 0, 3: 0, 4: 0}
		if isNarrower is True:
			for kanji in comparrisonList:
				if kanji in newList:
					kanjiLength = len(kanji)
					row, column = self.get_coordinates(lengthCounters[kanjiLength], self.wantedColumns[kanjiLength])
					self.allKanjiLabels[kanji].grid_configure(row = row, column = column)
					lengthCounters[kanjiLength] += 1
				else:
					self.allKanjiLabels[kanji].grid_forget()

		else:
			for kanji in newList:
				kanjiLength = len(kanji)
				row, column = self.get_coordinates(lengthCounters[kanjiLength], self.wantedColumns[kanjiLength])
				if kanji in comparrisonList:
					self.allKanjiLabels[kanji].grid_configure(row = row, column = column)
				else:
					self.allKanjiLabels[kanji].grid(row = row, column = column, ipadx = 1, ipady = 1)

				lengthCounters[kanjiLength] += 1

		for frame in self.kanjiLengthFrames:
			frame.grid_configure(sticky = 'ne')

	def display_sorted_results(self, sortedList):
		lengthCounters = {1: 0, 2: 0, 3: 0, 4: 0}
		for kanji in sortedList:
			kanjiLength = len(kanji)
			row, column = self.get_coordinates(lengthCounters[kanjiLength], self.wantedColumns[kanjiLength])
			self.allKanjiLabels[kanji].grid_configure(row = row, column = column)
			lengthCounters[kanjiLength] += 1

	def get_coordinates(self, counter, columns, startleft = False):
		row = counter // columns
		column = columns - counter % columns - 1 if (startleft is False) else counter % columns
		return (row, column)

	def create_label(self, kanji, frame, row, column):
		fgs = {1: '#ffffff', 2: '#80ff80', 3: '#80ffff', 4: '#ff80ff'}
		newLabel = Label(frame, text = kanji, font = ('helvatica', 14), bg = '#000000', fg = fgs[len(kanji)])
		self.enable_hover_interaction(kanji, newLabel)

		newLabel.grid(row = row, column = column, ipadx = 1, ipady = 1)
		return newLabel

	def enable_hover_interaction(self, kanji, label, **kwargs):
		commands = kwargs['commands'] if 'commands' in kwargs else (self.enterLabel_cmd, self.leaveLabel_cmd, self.leftClick_cmd)
		interactions = kwargs['interactions'] if 'interactions' in kwargs else ('Enter', 'Leave', 'Button 1')
		for command, interaction in zip(commands, interactions):
			if command != '':
				label.bind(f"<{interaction}>", lambda *args, kanji = kanji, command = command: command(kanji))

	def highlight_label_fg(self, kanji, fg):
		self.allKanjiLabels[kanji].config(fg = fg)

	def preview_new_label(self, kanji, data):
		#called when a new kanji is added and the position is to be determined, based on current sorting type.

		currentSort = self.sortType.get()
		newLength = len(kanji)

		if currentSort == 'date':
			newPosition = len([0 for sortedKanji in self.sortedSearchResults if len(sortedKanji) == newLength])
			row, column = self.get_coordinates(newPosition, self.wantedColumns[newLength])
			newLabel = self.create_label(kanji, self.kanjiLengthFrames[newLength - 1], row, column)
			labelsToShift = ()

		else:
			newKey = data[currentSort]
			orderDict = {'1': 1, 'N5': 1,
						 '2': 2, 'N4': 2,
						 '3': 3, 'N3': 3,
						 '4': 4, 'N2': 4,
						 '5': 5, 'N1': 5,
						 '6': 6, '-': 8,
						 'JH': 7}

			newPosition = 0
			labelsToShift = []
			for sortedKanji in self.sortedSearchResults:
				newKeyOrder = orderDict[newKey]
				currentKeyOrder = orderDict[self.allKanjiFilters[sortedKanji][currentSort]]

				if (len(sortedKanji) == newLength) and (newKeyOrder >= currentKeyOrder):
					newPosition += 1

				elif (len(sortedKanji) == newLength):
					labelsToShift.append(self.allKanjiLabels[sortedKanji])

			self.shift_labels(labelslist = labelsToShift, shiftamount = 1, startposition = newPosition, length = newLength)

			row, column = self.get_coordinates(newPosition, self.wantedColumns[newLength])
			newLabel = self.create_label(kanji, self.kanjiLengthFrames[newLength - 1], row, column)

		self.allKanjiLabels[kanji] = newLabel

		allEngs = []
		for engcommas in data['words'][1]:
			for eng in engcommas.split(','):
				if eng != '':
					allEngs.append(eng)
		filterEngs = ','.join(allEngs)

		self.allKanjiFilters[kanji] = {'kana': ','.join(data['words'][0]),
									   'english': filterEngs, 
									   'grade': data['grade'], 
									   'jlpt': data['jlpt'], 
									   'date': len(self.allKanjiLabels)}

		self.sortedSearchResults.append(kanji)

		self.resize_display()
		return (newLabel, labelsToShift, newPosition)

	def shift_labels(self, labelslist, shiftamount, startposition, length):
		for pos, label in enumerate(labelslist):
			shiftedRow, shiftedColumn = self.get_coordinates(startposition + shiftamount + pos, self.wantedColumns[length])
			label.grid_configure(row = shiftedRow, column = shiftedColumn)

	def cancel_new_label_preview(self, cancelkanji, label, shiftedlabels, startposition):
		#get the new kanji and save it (cancelkanji)
		length = len(cancelkanji)

		#remove saved kanji from visualiser allkanjilabels
		del self.allKanjiLabels[cancelkanji]
		del self.allKanjiFilters[cancelkanji]
		self.sortedSearchResults.remove(cancelkanji)

		#grid forget the saved kanji label
		label.grid_forget()

		#shift back all the kanji that were previously shifted forward
		self.shift_labels(shiftedlabels, -1, startposition + 1, length)

		#BUG: IF THE USER CHANGES THE SORTING TYPE WHILE IN PREVIEW MODE, THEN THE SORTING GETS MESSED UP. PROBABLY DUE TO CHANGING START POSITION.

	def shift_after_deleting(self, kanjis):
		lengthPositions = {1: [], 2: [], 3: [], 4: []}
		for kanji in kanjis:
			lengthPositions[len(kanji)].append(kanji)

		lengthCounters = {1: 0, 2: 0, 3: 0, 4: 0}
		lengthJumps = {1: 1, 2: 1, 3: 1, 4: 1}
		for sortedKanji in self.sortedSearchResults:
			length = len(sortedKanji)
			lengthCounters[length] += 1

			if lengthJumps[length] > 1: #jump back positions
				row, column = self.get_coordinates(lengthCounters[length] - lengthJumps[length], self.wantedColumns[length])
				self.allKanjiLabels[sortedKanji].grid_configure(row = row, column = column)

			if sortedKanji in lengthPositions[length]:
				lengthJumps[length] += 1
				self.allKanjiLabels[sortedKanji].destroy()

		#erase the data
		for kanji in kanjis:
			self.sortedSearchResults.remove(kanji)
			del self.allKanjiFilters[kanji]

	def swap_visualisers(self, pendingvisualiser):
		#first unload all frames in the displayframe
		for frame in self.displayFrame.winfo_children():
			frame.grid_forget()

		if pendingvisualiser == 'hiragana':
			self.hiraganaFrame.grid(row = 0, column = 0)

		elif pendingvisualiser == 'katakana':
			self.katakanaFrame.grid(row = 0, column = 0)

		else:
			self.load_kanji_length_frames()

		self.resize_display()

	def load_kanji_length_frames(self):
		for num, frame in enumerate(self.kanjiLengthFrames):
			frame.grid(row = num, column = 0, sticky = 'ne')

	def create_new_label(self, scripture):
		wordsStorage = {'hiragana': self.allHiragana, 'katakana': self.allKatakana}[scripture]
		frame = {'hiragana': self.hiraganaFrame, 'katakana': self.katakanaFrame}[scripture]
		position = len(wordsStorage)
		row, column = self.get_coordinates(position, 4, startleft = True)

		self.newKanaLabel, self.newEnglishLabel, self.newWin = self.get_new_label(row + column, frame)
		self.display_kana_label(self.newWin, row, column)

		self.newMeaningsList = ['' for _ in range(6)]

		self.resize_display()

	def update_new_katakana_label(self, entry):

		def wait_to_update():
			self.newKanaLabel.config(text = entry.get())

		entry.after(1, wait_to_update)

	def update_new_hiragana_label(self, entry, kanji):

		def wait_to_update():
			self.newKanaLabel.config(text = entry.get() if kanji.get() == '' else f'{entry.get()} ({kanji.get()})')

		entry.after(1, wait_to_update)

	def collate_new_meanings(self, num, entry):
		self.newMeaningsList[num] = entry.get()

		engText = self.format_english_text([text for text in self.newMeaningsList if text != ''])
		self.newEnglishLabel.config(text = engText)

	def add_new_hiragana(self, newkana, newmeaning, newkanji):
		self.update_hiragana_dict(newkana, newmeaning, newkanji)
		self.create_new_label(scripture = 'hiragana')

	def add_new_katakana(self, newkana, newmeaning):
		self.update_katakana_dict(newkana, newmeaning)
		self.create_new_label(scripture = 'katakana')

	def cancel_new_kana(self, *variables):
		self.unbind_tracers(variables)
		self.destroy_new_label()
		self.resize_display()

	def unbind_hiragana_tracers(self, kanavar, engvars, kanjivar):
		kanavar.trace_remove('write', kanavar.trace_info()[0][1])
		kanjivar.trace_remove('write', kanjivar.trace_info()[0][1])
		for engvar in engvars:
			engvar.trace_remove('write', engvar.trace_info()[0][1])

	def unbind_tracers(self, *variables):
		for var in variables[0]:
			var.trace_remove('write', var.trace_info()[0][1])

	def destroy_new_label(self):

		def wait_to_destroy():
			self.newWin.destroy()

		self.newWin.after(1, wait_to_destroy)
		del self.newMeaningsList

	def update_hiragana_dict(self, newkana, newmeaning, newkanji):
		self.allHiragana[newkana] = (newmeaning.split(','), newkanji)
		self.hiraganaLabels[newkana] = self.newWin

	def update_katakana_dict(self, newkana, newmeaning):
		self.allKatakana[newkana] = newmeaning.split(',')
		self.katakanaLabels[newkana] = self.newWin


if __name__ == '__main__':
	pass



	# root = Tk()
	# root.title('Sorting stuffs')
	# root.geometry('1400x800')

	# interface = visualiser_interface(root, columns = {1: 36, 2: 21, 3: 14, 4: 9})

	# data = {data[0]: {'words': utilities.decode(data[1]), 'grade': data[2], 'jlpt': data[3], 'date': num} for (num, data) in enumerate(data_list, start = 1)}

	# interface.setup_data(data)
	# interface.load()

	# root.mainloop()