#PYTHON MODULES
from tkinter import *

#module for handling translation of typable text from english to japanese and reverse.

hiragana_dict = {
                 '':'',
                 'a': 'あ', 'i': 'い', 'u': 'う', 'e':'え', 'o': 'お', 'ka': 'か', 'ki': 'き', 'ku': 'く', 'ke': 'け', 'ko': 'こ', 'ga': 'が', 'gi': 'ぎ', 'gu': 'ぐ', 'ge': 'げ', 'go': 'ご',
                 'sa': 'さ','shi': 'し', 'si': 'し', 'su': 'す', 'se': 'せ', 'so': 'そ', 'za': 'ざ', 'zi': 'じ', 'ji': 'じ', 'zu': 'ず', 'ze': 'ぜ', 'zo': 'ぞ', 'ta': 'た', 'chi': 'ち', 'ci': 'ち', 'tsu': 'つ',
                 'tu': 'つ', 'te': 'て', 'to': 'と', 'da': 'だ', 'di': 'ぢ', 'du': 'づ', 'de': 'で', 'do': 'ど', 'na': 'な', 'ni': 'に', 'nu': 'ぬ', 'ne': 'ね', 'no': 'の', 'ha': 'は', 'hi': 'ひ',
                 'hu': 'ふ', 'fu': 'ふ', 'he': 'へ', 'ho': 'ほ', 'ba': 'ば', 'bi': 'び', 'bu': 'ぶ', 'be': 'べ', 'bo': 'ぼ', 'pa': 'ぱ', 'pi': 'ぴ', 'pu': 'ぷ', 'pe': 'ぺ', 'po': 'ぽ', 'ma': 'ま',
                 'mi': 'み', 'mu': 'む', 'me': 'め', 'mo': 'も', 'ya': 'や', 'yu': 'ゆ', 'yo': 'よ', 'ra': 'ら', 'ri': 'り', 'ru': 'る', 're': 'れ', 'ro': 'ろ', 'wa': 'わ', 'wo': 'を', 'nn': 'ん',
                 'kya': 'きゃ', 'kyu': 'きゅ', 'kyo': 'きょ', 'gya': 'ぎゃ', 'gyu': 'ぎゅ', 'gyo': 'ぎょ', 'sha': 'しゃ', 'shu': 'しゅ', 'sho': 'しょ', 'ja': 'じゃ', 'ju': 'じゅ', 'jo': 'じょ',
                 'cha': 'ちゃ', 'chu': 'ちゅ','cho': 'ちょ', 'hya': 'ひゃ', 'hyu': 'ひゅ', 'hyo': 'ひょ', 'bya': 'びゃ', 'byu': 'びゅ', 'byo': 'びょ', 'pya': 'ぴゃ', 'pyu': 'ぴゅ',
                 'pyo': 'ぴょ', 'nya': 'にゃ', 'nyu': 'にゅ', 'nyo': 'にょ', 'mya': 'みゃ', 'myu': 'みゅ', 'myo': 'みょ', 'rya': 'りゃ', 'ryu': 'りゅ', 'ryo': 'りょ'
                }

katakana_dict = {
                 '':'',
                 'a': 'ア', 'i': 'イ', 'u': 'ウ', 'e':'エ', 'o': 'オ', 'ka': 'カ', 'ki': 'キ', 'ku': 'ク', 'ke': 'ケ', 'ko': 'コ', 'ga': 'ガ', 'gi': 'ギ', 'gu': 'グ', 'ge': 'ゲ', 'go': 'ゴ',
                 'sa': 'サ','shi': 'シ', 'si': 'シ', 'su': 'ス', 'se': 'セ', 'so': 'ソ', 'za': 'ザ', 'zi': 'ジ', 'ji': 'ジ', 'zu': 'ズ', 'ze': 'ゼ', 'zo': 'ゾ', 'ta': 'タ', 'chi': 'チ', 'ci': 'チ', 'tsu': 'ツ',
                 'tu': 'ツ', 'te': 'テ', 'to': 'ト', 'da': 'ダ', 'di': 'ヂ', 'du': 'ヅ', 'de': 'デ', 'do': 'ド', 'na': 'ナ', 'ni': 'ニ', 'nu': 'ヌ', 'ne': 'ネ', 'no': 'ノ', 'ha': 'ハ', 'hi': 'ヒ',
                 'hu': 'フ', 'fu': 'フ', 'he': 'ヘ', 'ho': 'ホ', 'ba': 'バ', 'bi': 'ビ', 'bu': 'ブ', 'be': 'ベ', 'bo': 'ボ', 'pa': 'パ', 'pi': 'ピ', 'pu': 'プ', 'pe': 'ペ', 'po': 'ポ', 'ma': 'マ',
                 'mi': 'ミ', 'mu': 'ム', 'me': 'メ', 'mo': 'モ', 'ya': 'ヤ', 'yu': 'ユ', 'yo': 'ヨ', 'ra': 'ラ', 'ri': 'リ', 'ru': 'ル', 're': 'レ', 'ro': 'ロ', 'wa': 'ワ', 'wo': 'ヲ', 'nn': 'ン',
                 'kya': 'キャ', 'kyu': 'キュ', 'kyo': 'キョ', 'gya': 'ギャ', 'gyu': 'ギュ', 'gyo': 'ギョ', 'sha': 'シャ', 'shu': 'シュ', 'sho': 'ショ', 'ja': 'ジャ', 'ju': 'ジュ', 'jo': 'ジョ',
                 'cha': 'チャ', 'chu': 'チュ','cho': 'チョ', 'hya': 'ヒャ', 'hyu': 'ヒュ', 'hyo': 'ヒョ', 'bya': 'ビャ', 'byu': 'ビュ', 'byo': 'ビョ', 'pya': 'ピャ', 'pyu': 'ピュ',
                 'pyo': 'ピョ', 'nya': 'ニャ', 'nyu': 'ニュ', 'nyo': 'ニョ', 'mya': 'ミャ', 'myu': 'ミュ', 'myo': 'ミョ', 'rya': 'リャ', 'ryu': 'リュ', 'ryo': 'リョ',
                 'wi': 'ウィ', 'we': 'ウェ', 'wo': 'ウォ', 'she': 'シェ', 'che': 'チェ', 'tsa': 'ツァ', 'tse': 'ツェ', 'tso': 'ツォ', 'ti': 'ティ', 'tu': 'トゥ',
                 'fa': 'ファ', 'fi': 'フィ', 'fe': 'フェ', 'fo': 'フォ', 'je': 'ジェ', 'di': 'ディ', 'du': 'ドゥ', 'dyu': 'ヂュ'
                }

hiraganaToKatakanaDict = {
                         '':'',
                         'あ': 'ア', 'い': 'イ', 'う': 'ウ', 'え':'エ', 'お': 'オ', 'か': 'カ', 'き': 'キ', 'く': 'ク', 'け': 'ケ', 'こ': 'コ', 'が': 'ガ', 'ぎ': 'ギ', 'ぐ': 'グ', 'げ': 'ゲ', 'ご': 'ゴ',
                         'さ': 'サ', 'し': 'シ', 'す': 'ス', 'せ': 'セ', 'そ': 'ソ', 'ざ': 'ザ', 'じ': 'ジ', 'じ': 'ジ', 'ず': 'ズ', 'ぜ': 'ゼ', 'ぞ': 'ゾ', 'た': 'タ', 'ち': 'チ',
                         'つ': 'ツ', 'て': 'テ', 'と': 'ト', 'だ': 'ダ', 'ぢ': 'ヂ', 'づ': 'ヅ', 'で': 'デ', 'ど': 'ド', 'な': 'ナ', 'に': 'ニ', 'ぬ': 'ヌ', 'ね': 'ネ', 'の': 'ノ', 'は': 'ハ', 'ひ': 'ヒ',
                         'ふ': 'フ', 'ふ': 'フ', 'へ': 'ヘ', 'ほ': 'ホ', 'ば': 'バ', 'び': 'ビ', 'ぶ': 'ブ', 'べ': 'ベ', 'ぼ': 'ボ', 'ぱ': 'パ', 'ぴ': 'ピ', 'ぷ': 'プ', 'ぺ': 'ペ', 'ぽ': 'ポ', 'ま': 'マ',
                         'み': 'ミ', 'む': 'ム', 'め': 'メ', 'も': 'モ', 'や': 'ヤ', 'ゆ': 'ユ', 'よ': 'ヨ', 'ら': 'ラ', 'り': 'リ', 'る': 'ル', 'れ': 'レ', 'ろ': 'ロ', 'わ': 'ワ', 'を': 'ヲ', 'ん': 'ン',
                         'ゃ': 'ャ', 'ゅ': 'ュ', 'ょ': 'ョ', 'っ': 'ッ',
                         }

katakanaToHiraganaDict = {hiraganaToKatakanaDict[kana]: kana for kana in hiraganaToKatakanaDict}

#FROM MAIN KANJI MODULE:

#1) create the entry widget and the converter button (if any)
#2) create a translator object, with the entry set to the above created entry.
#arguments: entry, cycle, togglebutton

class Translator:

  def __init__(self, entry, cycle, togglebutton = None):

    #entry widget
    self.entry = entry
    self.entry.bind('<Button-1>', self.move_cursor)

    #cycle list - order of languages to cycle through whenever translator is toggled
    self.cycle = cycle

    #translator toggle button. can be set to the boolean None if no toggle button is available.
    self.toggleButton = togglebutton

    #the current language used. initial setting is always the 0th index in self.cycle
    self.activeLanguage = self.cycle[0]
    self.activeDictionary = {'あ': hiragana_dict, 'ア': katakana_dict, 'ABC': None}[self.activeLanguage]

    self.textVar = StringVar()
    self.entry.config(textvariable = self.textVar)
    self.textVar.trace('w', self.Translate)

    if self.toggleButton != None:
      self.toggleButton.config(command = lambda: self.change_language(self.cycle[1]))

    self.entryPosition = 0
    self.text = ''

    self.specialCharacters = '1234567890!@#$%^&*()-=_+'

  def move_cursor(self, *args):
    self.entryPosition = self.entry.index(INSERT)

  def Translate(self, *args):

    #new character typed in by the user
    newChar = self.textVar.get()[self.entryPosition:]
    print(newChar, self.entryPosition)

    if self.activeLanguage in ('あ', 'ア'):

      if len(newChar) > 1:
        c1 = newChar[0]

        #special translation (n)
        if c1 == 'n' and newChar[1] not in ('a', 'i', 'u', 'e', 'o', 'y', 'n'):
          self.entry.delete(self.entryPosition, END)
          self.entry.insert(self.entryPosition, f"{'ん' if self.activeLanguage == 'あ' else 'ン'}{newChar[1]}")
          self.entryPosition = len(self.textVar.get()) - 1

      if len(newChar) > 2:
        c2 = newChar[1]

        #special translation
        if c1 == c2 and newChar[1:] in self.activeDictionary:
          self.entry.delete(self.entryPosition, END)
          self.entry.insert(self.entryPosition, f"{'っ' if self.activeLanguage == 'あ' else 'ー'}{self.activeDictionary[newChar[1:]]}")
          self.entryPosition = len(self.textVar.get())

      #normal translation
      if newChar in self.activeDictionary and len(newChar) > 0:
        self.entry.delete(self.entryPosition, END)
        self.entry.insert(self.entryPosition, self.activeDictionary[newChar])
        self.entryPosition = len(self.textVar.get())

      elif newChar in self.specialCharacters:
        self.entryPosition = len(self.textVar.get())

      #deleting
      if len(newChar) == 0:
        self.entryPosition = len(self.textVar.get())

    self.text = self.entry.get()

  def change_language(self, next_):

    self.entry.delete(0, END)
    self.activeLanguage = next_

    #this moves index 0 to index -1 (first to last), resulting in evey other index being reduced by 1, shifting the order of the list 1 left.
    cycle_first = self.cycle[0]
    self.cycle.remove(cycle_first)
    self.cycle.append(cycle_first)

    if self.toggleButton != None:
      self.toggleButton.config(text = self.activeLanguage, command = lambda: self.change_language(self.cycle[1]))

    if self.activeLanguage in ['あ', 'ア']:
      self.activeDictionary = hiragana_dict if self.activeLanguage == 'あ' else katakana_dict

    else:
      self.activeLanguage = None

def convert_to_hiragana(text):
  if text[0] not in katakanaToHiraganaDict:
    return text

  else:
    convertedText = ''
    for char in text:
      convertedText += katakanaToHiraganaDict[char]
    return convertedText

#FOR TESTING PURPOSES ONLY:

def create_test_window(main, name, cycle):

  if main:
    
    root = Tk()
    root.title('Translators testing')
    root.geometry('720x640+580+200')

    frame = Frame(root, width = 720, height = 640, bg = 'black')
    frame.pack_propagate(0)
    frame.pack()

    Title = Label(frame, text = f'translator testing window', font = ('arial', 20), fg = 'white', bg = 'black')
    Etr = Entry(frame, width = 18, font = ('arial', 30), justify = CENTER)
    Etr.focus_set()

    Title.pack(pady = 20)
    Etr.pack(pady = 20)

    if len(cycle) > 1:
      Btn = Button(frame, text = name, font = ('arial', 20), width = 4, fg = 'white', bg = 'black')
      Btn.pack(pady = 20)
    else:
      Btn = None

    TranslatorObject = Translator(entry = Etr, cycle = cycle, togglebutton = Btn)
    # translator_dict[name] = Translator(Etr, name, cycle, Btn)

    root.mainloop()

#initial language will be the entry with 0th index in language_list
language_list = ['あ']

create_test_window(__name__ == '__main__', language_list[0], language_list)

def supercode(text): #converts kana to a coded string. eg: supercode('い-adj') = '<hira:i>-adj'
  if text == '':
    return text
  
  kanaChars = []
  engs = []
  remainingText = text
  for num, char in enumerate(text):
    if (char in hiraganaToKatakanaDict) or (char in katakanaToHiraganaDict):
      splitText = remainingText.split(char)
      engs.append(splitText[0])
      remainingText = splitText[1]
      kanaChars.append(char)

  engs.append(remainingText)

  if kanaChars == []:
    return text

  else:
    wrappedText = ''
    for num, char in enumerate(kanaChars):

      if char in hiraganaToKatakanaDict:
        reverseDict = {hiragana_dict[eng]: eng for eng in hiragana_dict}
        wrapperText = f"<hira:{reverseDict[char]}>"

      elif char in katakanaToHiraganaDict:
        reverseDict = {katakana_dict[eng]: eng for eng in katakana_dict}
        wrapperText = f"<kata:{reverseDict[char]}>"

      wrappedText += engs[num] + wrapperText

    wrappedText += engs[num + 1]
    return wrappedText

def inverse_supercode(text): #inverse function of supercode
  scanning = False
  current = 0
  remainingText = text
  lockedTexts = []
  leftText = []
  for num, char in enumerate(text):

    if (char == '<') and (not scanning):
      scanning = True
      current = num + 1

    elif (char == '>') and (scanning):
      scanning = False

      lockedText = text[current:num]
      lockedTexts.append(lockedText)
      splitText = remainingText.split(f"<{lockedText}>")

      leftText.append(splitText[0])
      remainingText = splitText[1]

  if lockedTexts == []:
    return text

  else:
    leftText.append(remainingText)

    unwrappedText = ''
    for num, char in enumerate(lockedTexts):
      
      if char[:4] == 'hira':
        kanaChar = hiragana_dict[char[5:]]
        
      elif char[:4] == 'kata':
        kanaChar = katakana_dict[char[5:]]

      unwrappedText += leftText[num] + kanaChar

    unwrappedText += leftText[num + 1]
    return unwrappedText