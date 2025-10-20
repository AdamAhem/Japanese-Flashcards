from tkinter import *
from tkinter import ttk
import visualiser

#module handling all the front-end classes and functions (eventually...)

class Window:

   '''
   parent window class that can load and unload subclasses of this class.
   '''

   def __init__(self, root, **kwargs):
      self.shift_x = kwargs['shift_x'] if 'shift_x' in kwargs else 0.5
      self.shift_y = kwargs['shift_y'] if 'shift_y' in kwargs else 0.5

      self.root = root
      self.col = {'main': kwargs['bg'] if 'bg' in kwargs else '#000000'}

      self.mainWin = Frame(self.root, bg = self.col['main'])

      self.widgets = []
      self.specialWidgets = {}

   def save_colours(self, *colours):
      for col_pair in colours:
         self.col[col_pair[0]] = col_pair[1]

   def new_Label(self, In, geom, **kwargs):
      newLabel = Label(In, 
                       text = kwargs['text'] if 'text' in kwargs else '',
                       font = kwargs['font'] if 'font' in kwargs else ('arial', 10),
                       width = kwargs['width'] if 'width' in kwargs else 0,
                       height = kwargs['height'] if 'height' in kwargs else 0,
                       bg = kwargs['bg'] if 'bg' in kwargs else '#f0f0f0',
                       fg = kwargs['fg'] if 'fg' in kwargs else '#000000',
                       anchor = kwargs['anchor'] if 'anchor' in kwargs else None)

      labelPair = {'widget': newLabel, 'geometry': geom}
      self.widgets.append(labelPair)

      return newLabel

   def new_Button(self, In, geom, **kwargs):      
      newButton = Button(In, text = kwargs['text'] if 'text' in kwargs else '',
                             font = kwargs['font'] if 'font' in kwargs else ('arial', 10),
                             width = kwargs['width'] if 'width' in kwargs else 0,
                             height = kwargs['height'] if 'height' in kwargs else 0,
                             bg = kwargs['bg'] if 'bg' in kwargs else '#f0f0f0',
                             fg = kwargs['fg'] if 'fg' in kwargs else '#000000',
                             command = kwargs['command'] if 'command' in kwargs else None,
                             anchor = kwargs['anchor'] if 'anchor' in kwargs else None,
                             state = kwargs['state'] if 'state' in kwargs else NORMAL)

      buttonPair = {'widget': newButton, 'geometry': geom}
      self.widgets.append(buttonPair)

      return newButton

   def new_Frame(self, In, geom, **kwargs):
      newFrame = Frame(In, width = kwargs['width'] if 'width' in kwargs else 0,
                           height = kwargs['height'] if 'height' in kwargs else 0,
                           bg = kwargs['bg'] if 'bg' in kwargs else '#f0f0f0')

      framePair = {'widget': newFrame, 'geometry': geom}
      self.widgets.append(framePair)

      return newFrame

   def new_Entry(self, In, geom, **kwargs):
      newEntry = Entry(In, font = kwargs['font'] if 'font' in kwargs else ('arial', 10),
                           width = kwargs['width'] if 'width' in kwargs else 0,
                           bg = kwargs['bg'] if 'bg' in kwargs else '#ffffff',
                           fg = kwargs['fg'] if 'fg' in kwargs else '#000000',
                           justify = kwargs['justify'] if 'justify' in kwargs else CENTER,
                           textvariable = kwargs['textvariable'] if 'textvariable' in kwargs else None,
                           state = kwargs['state'] if 'state' in kwargs else NORMAL)

      entryPair = {'widget': newEntry, 'geometry': geom}
      self.widgets.append(entryPair)

      return newEntry

   def new_Canvas(self, In, geom, **kwargs):
      newCanvas = Canvas(In, width = kwargs['width'] if 'width' in kwargs else 10,
                             height = kwargs['height'] if 'height' in kwargs else 10,
                             bg = kwargs['bg'] if 'bg' in kwargs else '#ffffff',
                             bd = kwargs['bd'] if 'bd' in kwargs else 1,
                             highlightthickness = kwargs['highlightthickness'] if 'highlightthickness' in kwargs else 1,
                             relief = kwargs['relief'] if 'relief' in kwargs else SOLID)


      canvasPair = {'widget': newCanvas, 'geometry': geom}
      self.widgets.append(canvasPair)

      return newCanvas

   def new_Scale(self, In, geom, **kwargs):
      newScale = Scale(In, from_ = kwargs['from_'] if 'from_' in kwargs else 1,
                           to = kwargs['to'] if 'to' in kwargs else 20,
                           length = kwargs['length'] if 'length' in kwargs else 10,
                           showvalue = kwargs['showvalue'] if 'showvalue' in kwargs else 1,
                           orient = kwargs['orient'] if 'orient' in kwargs else HORIZONTAL,
                           command = kwargs['command'] if 'command' in kwargs else None)

      scalePair = {'widget': newScale, 'geometry': geom}
      self.widgets.append(scalePair)

      return newScale

   def new_visualiser(self, In, geom, **kwargs):
      newVisualiser = visualiser.visualiser_interface(In, **kwargs)

      geom['loader'] = newVisualiser.load
      geom['unloader'] = newVisualiser.unload
      visualiserPair = {'widget': newVisualiser, 'geometry': geom}
      self.widgets.append(visualiserPair)

      return newVisualiser

   def new_radiobutton(self, In, geom, **kwargs):
      newRadiobutton = Radiobutton(In, text = kwargs['text'] if 'text' in kwargs else None,
                                       font = kwargs['font'] if 'font' in kwargs else None,
                                       bg = kwargs['bg'] if 'bg' in kwargs else '#ffffff',
                                       variable = kwargs['variable'] if 'variable' in kwargs else None,
                                       value = kwargs['value'] if 'value' in kwargs else None,
                                       command = kwargs['command'] if 'command' in kwargs else None)

      radioPair = {'widget': newRadiobutton, 'geometry': geom}
      self.widgets.append(radioPair)

      return newRadiobutton

   def set_geom(self, **kwargs):

      geometry_manager = {
                           'padx': kwargs['padx'] if 'padx' in kwargs else 0,
                           'pady': kwargs['pady'] if 'pady' in kwargs else 0,
                           'ipadx': kwargs['ipadx'] if 'ipadx' in kwargs else 0,
                           'ipady': kwargs['ipady'] if 'ipady' in kwargs else 0,
                           'sticky': kwargs['sticky'] if 'sticky' in kwargs else None,
                           'rowspan': kwargs['rowspan'] if 'rowspan' in kwargs else 1,
                           'columnspan': kwargs['columnspan'] if 'columnspan' in kwargs else 1,
                           'freeze': kwargs['freeze'] if 'freeze' in kwargs else 0,
                           'hidden': kwargs['hidden'] if 'hidden' in kwargs else 0,
                           'manager': kwargs['manager'] if 'manager' in kwargs else 'grid',
                           'side': kwargs['side'] if 'side' in kwargs else 'top', # top, bottom, left, right
                           'anchor': kwargs['anchor'] if 'anchor' in kwargs else 'center', #NSEW
                           'expand': kwargs['expand'] if 'expand' in kwargs else 0, #expand = 0 will place the widget in the center of it's parent widget
                           'fill': kwargs['fill'] if 'fill' in kwargs else None,
                           'loader': kwargs['loader'] if 'loader' in kwargs else None,
                           'unloader': kwargs['unloader'] if 'unloader' in kwargs else None
                           }

      if ('row' in kwargs) and ('column' in kwargs):
        geometry_manager['row'] = kwargs['row']
        geometry_manager['column'] = kwargs['column']

      return geometry_manager

   def moveto_window(self, destination, **kwargs):

      if isinstance(destination, Window):

         self.unload_window()
         loadscreen = initiate_loading(self.root, message = kwargs['loading_message'] if 'loading_message' in kwargs else 'Loading...')

         if 'exec_' in kwargs:
            kwargs['exec_']() if 'args' not in kwargs else kwargs['exec_'](kwargs['args'])

         destination.load_window(loading = loadscreen)

      else:
         print(f'Error: {destination} is not a Window Subclass.')

   def load_window(self, **kwargs):

      for pair in self.widgets:
         geom = pair['geometry']

         if pair['geometry'] != {} and pair['geometry']['hidden'] == 0:

            if geom['freeze'] == 1 and geom['manager'] == 'grid':
               pair['widget'].grid_propagate(0)

            elif geom['freeze'] == 1 and geom['manager'] == 'pack':
              pair['widget'].pack_propagate(0)


            if pair['geometry']['loader'] != None:
               pair['geometry']['loader']()


            elif 'scrollframe' in pair['geometry']: #LOADER WILL EVENTUALLY REPLACE THIS
               pair['widget'].load(**geom)


            elif geom['manager'] == 'grid':
               pair['widget'].grid(row = geom['row'], column = geom['column'], 
                                   padx = geom['padx'],
                                   pady = geom['pady'],
                                   ipadx = geom['ipadx'],
                                   ipady = geom['ipady'],
                                   sticky = geom['sticky'],
                                   rowspan = geom['rowspan'],
                                   columnspan = geom['columnspan'])

            elif geom['manager'] == 'pack':
              pair['widget'].pack(padx = geom['padx'],
                                  pady = geom['pady'],
                                  ipadx = geom['ipadx'],
                                  ipady = geom['ipady'],
                                  side = geom['side'],
                                  anchor = geom['anchor'],
                                  expand = geom['expand'],
                                  fill = geom['fill'])

      if 'exec_' in kwargs:
         kwargs['exec_']()


      if 'loading' in kwargs:

         end_loading(self.root, kwargs['loading'], message = 'Loaded')

      self.mainWin.place(relx = self.shift_x, rely = self.shift_y, anchor = CENTER)

   def unload_window(self, **kwargs):

      for pair in self.widgets:

         if 'scrollframe' in pair['geometry']:
            pair['widget'].unload()

         elif pair['geometry']['unloader'] != None:
            pair['geometry']['unloader']()

         elif pair['geometry']['manager'] == 'grid':
            pair['widget'].grid_forget()

         elif pair['geometry']['manager'] == 'pack':
            pair['widget'].pack_forget()

      if 'exec_' in kwargs:
         kwargs['exec_']()

      self.mainWin.place_forget()

   def load_widgets(self, *widgets):
      for widget in widgets:

        for Dict in self.widgets:
          if widget == Dict['widget']:
            info = Dict
            break

        geom = info['geometry']
        if geom['hidden'] == 1:
          geom['hidden'] = 0

          if 'scrollframe' in geom:
            info['widget'].load(**geom) 

          elif geom['manager'] == 'pack':
            if geom['freeze'] == 1:
              info['widge'].pack_propagate(0)
            info['widget'].pack(padx = geom['padx'],
                                  pady = geom['pady'],
                                  ipadx = geom['ipadx'],
                                  ipady = geom['ipady'],
                                  side = geom['side'],
                                  anchor = geom['anchor'],
                                  expand = geom['expand'],
                                  fill = geom['fill'])

          else:
            if geom['freeze'] == 1:
              info['widget'].grid_propagate(0)
            info['widget'].grid(row = geom['row'], column = geom['column'],
                                   padx = geom['padx'],
                                   pady = geom['pady'],
                                   ipadx = geom['ipadx'],
                                   ipady = geom['ipady'],
                                   sticky = geom['sticky'],
                                   rowspan = geom['rowspan'],
                                   columnspan = geom['columnspan'])

   def unload_widgets(self, *widgets):
      for widget in widgets:

         for Dict in self.widgets:
            if widget == Dict['widget']:
               info = Dict
               break

         if info['geometry']['hidden'] == 0:
            info['geometry']['hidden'] = 1

            if 'scrollframe' in info['geometry']:
               info['widget'].unload()

            elif info['geometry']['manager'] == 'pack':
              info['widget'].pack_forget()

            else:
               info['widget'].grid_forget()

   def null(self):
      print('window null called.')


def initiate_loading(root, **kwargs):

   if 'message' in kwargs:
      print(kwargs['message'])

   loadscreen = Frame(root, bg = '#000000', width = 1440, height = 900)
   loadscreen.pack_propagate(0)
   loadscreen.place(relx = 0.5, rely = 0.5, anchor = CENTER)

   loadingtitle = Label(loadscreen, bg = '#000000', text = 'Loading...', font = ('arial', 50), fg = 'white', pady = 400)
   loadingtitle.pack()

   root.update_idletasks()

   return loadscreen

def end_loading(root, screen, **kwargs):

   if 'message' in kwargs:
      print(kwargs['message'])

   screen.destroy()
   del screen




class smart_Frame:

   '''
   A new and smarter scrollframe. Designed to cause much less lag and can handle virtually infinite kanji, since there won't be
   the frame height limit constraint.
   '''

   meterWidth = 20
   Hmax = (2**15) - 1

   def __init__(self, master, root, width, height, *args, **kwargs):
      self.master = master
      self.root = root
      self.width = width - self.meterWidth
      self.height = height

      self.placementManager = kwargs['placement'] if 'placement' in kwargs else None

      self.mainFrame = Frame(self.root, bg = kwargs['bg'] if 'bg' in kwargs else '#aa33ff')
      self.scrollFrame = Frame(self.mainFrame, width = self.meterWidth, height = self.meterWidth, bg = '#8a1f93')

      self.viewingCanvas = Canvas(self.mainFrame, width = self.width, height = self.height, bg = '#936c6c',
                                  bd = 0, highlightthickness = 0, relief = RIDGE)

      self.scrollbar = ttk.Scrollbar(self.scrollFrame, orient = VERTICAL, command = self.viewingCanvas.yview)

      self.canvasFrame = Frame(self.viewingCanvas, bg = '#937ab8')
      self.heightSustainerFrame = Frame(self.canvasFrame, height = self.Hmax, bg = 'black', width = 5) #2**15 - 1 = 32767: maximum height

      self.viewingCanvas.bind('<Configure>', lambda e: self.viewingCanvas.configure(scrollregion = self.viewingCanvas.bbox('all')))
      self.viewingCanvas.create_window((0, 0), window = self.canvasFrame, anchor = 'nw')

      self.staticFrame = Frame(self.viewingCanvas, width = self.width, height = self.height, bg = 'black')

      self.upperBound = 0
      self.lowerBound = self.height + 150

   def setup(self, allHeights):
      self.midpoints = {}
      for num, height in enumerate(allHeights, start = 1):
         frameUpperBound = self.upperBound + sum(allHeights[:num])
         frameLowerBound = frameUpperBound + height
         midpoint = int(0.5 * (frameLowerBound + frameUpperBound))

         self.midpoints[midpoint] = num

      self.totalHeight = frameUpperBound

      self.visibleFrames = []
      self.revList = [p for p in self.midpoints]

      self.viewingCanvas.configure(yscrollcommand = self.get_relative_height)

   def load(self, row, column, **kwargs):

      self.heightSustainerFrame.grid(row = 0, column = 0, sticky = 'nw')
      self.heightSustainerFrame.grid_propagate(0)

      self.viewingCanvas.grid(row = 0, column = 0)

      self.staticFrame.grid(row = 0, column = 0, sticky = 'n', ipadx = 150, ipady = 50)
      self.staticFrame.grid_propagate(0)

      self.scrollFrame.grid(row = 0, column = 1, sticky = 'n')
      self.scrollbar.grid(row = 0, column = 0, ipady = 325, sticky = N)

      self.mainFrame.grid(row = row, column = column, padx = kwargs['padx'] if 'padx' in kwargs else 0,
                                                      pady = kwargs['pady'] if 'pady' in kwargs else 0)

   def new_layer(self):

      self.newLimit = len(self.midpoints) + 1
      self.revList.append(self.revList[-1] + 70)
      self.midpoints[self.revList[-1]] = self.newLimit

      self.totalHeight += 70

      oldVis = self.visibleFrames
      self.visibleFrames.append(self.visibleFrames[-1] + 1)

      if self.scrollbar.get()[1] > 0.9:
         self.get_relative_height(*self.scrollbar.get())

      self.shuffle(self.visibleFrames, oldVis)

   def cancel_new_layer(self):

      self.totalHeight -= 70

      del self.midpoints[self.revList[-1]]
      self.revList.remove(self.revList[-1])

      self.visibleFrames.remove(self.visibleFrames[-1])

      del self.newLimit
      

   def unload(self):

      self.heightSustainerFrame.grid_forget()
      self.viewingCanvas.grid_forget()
      self.staticFrame.grid_forget()
      self.scrollFrame.grid_forget()
      self.scrollbar.grid_forget()
      self.mainFrame.grid_forget()

   def get_relative_height(self, *args):

      self.scrollbar.set(*args)
      relativeHeight = ((float(args[0]) - (0.005 if float(args[0]) > 0.005 else 0))/ 0.9826044495986817) 
      depth = int(self.totalHeight * relativeHeight)
      screenBounds = (depth + self.upperBound, depth + self.lowerBound)

      for start in range(*screenBounds):
         if start in self.midpoints:
            break

      prevVis = self.visibleFrames
      self.visibleFrames = []
      for end in self.revList[self.revList.index(start):]:
         if end in range(*screenBounds):
            self.visibleFrames.append(self.midpoints[end])
         else:
            break

      self.shuffle(self.visibleFrames, prevVis)

   def shuffle(self, new, old):
      for num, vis in enumerate(new):
         self.config_display(vis - 1, num)

      for prev in old:
         if not prev in new:
            self.config_display(prev - 1)

   def config_display(self, num, *args):

      if self.placementManager != None:
         self.placementManager(num, *args)




class open_preset_window:

   '''
   This class is called whenever the user want's to configure their profile's saved kanji presets.
   The class interface allows the user to pick, delete, update, set as default, and create new kanji presets and save them in their profile.
   '''

   def __init__(self, user, presets, currentPreset, new, **kwargs):

      self.user = user

      self.root = Toplevel(bg = '#111822')
      self.root.title(f"{self.user}'s presets")
      self.root.geometry('460x900+0+50')

      self.activeSet = kwargs['activeSet'] if 'activeSet' in kwargs else {}
      self.exitFunc = kwargs['exit'] if 'exit' in kwargs else None   
      self.update_user_default_preset = kwargs['updateConfig'] if 'updateConfig' in kwargs else None
      self.update_user_preset_values = kwargs['updateValues'] if 'updateValues' in kwargs else None
      self.append_preset = kwargs['newPreset'] if 'newPreset' in kwargs else None

      self.presetWindow = Frame(self.root, width = 410, height = 510, bg = '#bcd4f5')
      self.presetFrame = Frame(self.presetWindow, width = 400, height = 460, bg = '#0a0a10')

      self.presetFrame.grid_propagate(0)
      self.presetFrame.grid(row = 0, column = 0, padx = 5, pady = 5)

      self.presets = {}
      self.presetVar = StringVar()
      for num, preset in enumerate(presets):

         if presets[preset] == currentPreset:
            self.presetVar.set(preset)
            self.currentPreset = preset
            current = True
         else:
            current = False

         if presets[preset]['default']:
            self.defaultPreset = preset
            default = True
         else:
            default = False

         bg = {(True, True): '#0000cc', (True, False): '#363663', (False, True): '#1b1b50', (False, False): '#000000'}[(current, default)]

         self.presets[preset] = self.display_preset(num, preset, presets[preset], bg)

      self.buttonsWindow = Frame(self.root, width = 410, height = 60, bg = '#bcd4f5')
      self.buttonsFrame = Frame(self.buttonsWindow, width = 400, height = 50, bg = '#0a0a10')

      if new:
         self.open_with_new_preset()
      else:
         self.open_without_new_preset()

      self.buttonsFrame.grid_propagate(0)
      self.buttonsFrame.grid(row = 0, column = 0, padx = 5, pady = 5)

      self.presetWindow.pack(pady = 15)
      self.buttonsWindow.pack()

      self.root.mainloop()

   def open_without_new_preset(self):

      self.selectButton = Button(self.buttonsFrame, text = 'Select', font = ('arial', 16), bg = '#b8e0be', width = 7,
                                  command = self.return_selected_preset)
      self.deleteButton = Button(self.buttonsFrame, text = 'Delete', font = ('arial', 16), bg = '#e0b8be', width = 7,
                                 command = self.delete_preset)
      self.defaultButton = Button(self.buttonsFrame, text = 'Default', font = ('arial', 16), bg = '#b8b8e0', width = 7,
                                  command = self.update_default_preset)
      self.updateButton = Button(self.buttonsFrame, text = 'Save', font = ('arial', 16), bg = '#e0b8e0', width = 7, 
                                 command = self.save_active_preset)

      self.selectButton.grid(row = 0, column = 0, padx = 5, pady = 5)
      self.deleteButton.grid(row = 0, column = 1)
      self.defaultButton.grid(row = 0, column = 2, padx = 5)
      self.updateButton.grid(row = 0, column = 3)

   def open_with_new_preset(self):

      self.newPresetName = Label(self.buttonsFrame, text = 'Preset name:', font = ('arial', 16), bg = '#0a0a10', fg = '#80eaff')
      self.newPresetEntry = Entry(self.buttonsFrame, font = ('arial', 16), width = 14)
      self.savePresetButton = Button(self.buttonsFrame, text = 'Save', font = ('arial', 16), bg = '#a6f2a6', fg = '#000000',
                                     command = self.save_new_preset)

      self.newPresetEntry.focus_set()

      self.newPresetName.grid(row = 0, column = 0, padx = 5, pady = 11)
      self.newPresetEntry.grid(row = 0, column = 1)
      self.savePresetButton.grid(row = 0, column = 2, padx = 11)

   def display_preset(self, num, name, values, bg):

      defaultWindow = Frame(self.presetFrame, width = 197, height = 64, bg = 'white')
      defaultFrame = Frame(defaultWindow, width = 193, height = 60, bg = bg)

      radioButton = Radiobutton(defaultFrame, text = name, variable = self.presetVar, value = name,
                                bg = bg, fg = 'white',
                                selectcolor = 'black', font = ('arial', 14),
                                command = lambda name = name: self.select_preset(name))

      radioButton.grid(row = 0, column = 0, padx = 10, pady = 12)

      defaultFrame.grid_propagate(0)
      defaultFrame.grid(row = 0, column = 0, padx = 2, pady = 2)
      row, column = num % 5, num // 5
      defaultWindow.grid(row = row, column = column, padx = 2 if num % 2 == 0 else 0, pady = 2)

      return (values, radioButton, defaultFrame)

   def select_preset(self, presetName):

      #(current, default)
      bgs = {(True, True): '#0000cc', (True, False): '#363663', (False, True): '#1b1b50', (False, False): '#000000'}

      prevBg = bgs[(False, self.presets[self.currentPreset][0]['default'])]
      nextBg = bgs[(True, self.presets[presetName][0]['default'])]

      self.presets[self.currentPreset][1].config(bg = prevBg)
      self.presets[self.currentPreset][2].config(bg = prevBg)

      self.presets[presetName][1].config(bg = nextBg)
      self.presets[presetName][2].config(bg = nextBg)

      self.presetVar.set(presetName)
      self.currentPreset = presetName

   def return_selected_preset(self):
      if self.exitFunc != None:
         self.exitFunc(self.currentPreset, self.presets[self.currentPreset][0])
         self.root.destroy()

   def delete_preset(self):
      print('WIP')

   def update_default_preset(self):
      self.presets[self.defaultPreset][0]['default'] = False
      self.presets[self.defaultPreset][1].config(bg = '#000000')
      self.presets[self.defaultPreset][2].config(bg = '#000000')

      self.presets[self.currentPreset][0]['default'] = True
      self.presets[self.currentPreset][1].config(bg = '#0000cc')
      self.presets[self.currentPreset][2].config(bg = '#0000cc')

      if (self.update_user_default_preset != None) and (self.defaultPreset != self.currentPreset):
         self.update_user_default_preset(self.user, self.defaultPreset, self.currentPreset)

      self.defaultPreset = self.currentPreset

   def save_active_preset(self):
      if self.update_user_preset_values != None:
         self.update_user_preset_values(self.user, self.currentPreset, self.activeSet)

   def save_new_preset(self):
      newName = self.newPresetEntry.get()
      if newName != '' and self.append_preset != None:
         self.append_preset(self.user, newName, self.activeSet, len(self.presets))
         if self.exitFunc != None:
            self.exitFunc()
         self.root.destroy()

if __name__ == '__main__':
   pass