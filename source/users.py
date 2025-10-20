import sys
import os
from pathlib import Path

#This module focuses on getting and setting information for users of the kanji flashcard game.
#information may include filters set for which grade or JLPT to use in the flashcard game, among other things.

parentPath = Path(sys._MEIPASS) if getattr(sys, "frozen", False) is True else Path(__file__).resolve().parent.parent

usersFile = parentPath / "users"
files = [user for user in os.listdir(usersFile)]

UTF8 = "utf-8"

def get_default_values():

    #dictionary which will contain all the default values extracted from the users' file.
    default = {}

    #tuple containing the data keys that will only ever have one element. data under this category need not be appended to a list.
    singleVariableDataKeys = ('time', 'lives', 'recover', 'language', 'repetition', 'gradelogic', 'jlptlogic', 'lengthlogic', 'tagslogic')

    #loops through the .txt files in the 'users' folder
    for user in os.listdir(usersFile): # <--- Opens the file named 'users' if it is in the same directory as the script file
        
        #opens the .txt file
        with open(f"{usersFile}/{user}", 'r', encoding = UTF8) as profile:

            #reads the FIRST line and gets the name written on that user.
            default_name = profile.readline().strip()

            #reads the SECOND line and determines if this is the default user.
            if profile.readline().strip()[-1] != '1':
                pass

            else:
                for text in profile:
                    info = text.strip()
                    if info not in ('', 'DEFAULT GAME SETTINGS:'):

                        category = info[:info.index(':')]
                        data = info[info.index(':') + 1:]

                        if category in singleVariableDataKeys:
                            default[category] = data

                        elif data != 'none':
                            default[category] = data.split(',')

                        else:
                            default[category] = []

                default['user'] = default_name[default_name.index(':') + 2:]
                break

    return default

def set_default_values(data, user):

    textList = [f'{cat}:{data[cat]}' for cat in data]

    for standardText in [f'NAME: {user}', 'DEFAULT: 1', 'DEFAULT GAME SETTINGS:', ''][::-1]:
        textList.insert(0, standardText)

    with open(f"users/{user}.txt", 'w') as writing:
        for text in textList:
            writing.write(text + '\n')

    print('set as default.')
    return True

def get_all_users():
   #obtains all registered users and their default values
   users = {}
   for user in os.listdir(usersFile):
      with open(f"{usersFile}/{user}", 'r', encoding = UTF8) as profile:
         name = profile.readline().strip()[6:]
         default = profile.readline().strip()[9:]
         users[name] = default

   return users


# if __name__ == '__main__':
#     pass
# else:
#     default_values = get_default_values()