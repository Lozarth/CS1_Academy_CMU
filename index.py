from subprocess import Popen

import inquirer
import os
from clear import clear

clear()


directories = []

for folder in os.listdir('.'):
    if ((os.path.isdir(folder)) and (not folder.startswith('.'))):
        directories.append(folder)

def chooseFolder():
    folderAnswer = inquirer.prompt([
        inquirer.List('directory', message = 'Select a unit', choices = directories),
    ])

    global chosenFolder
    chosenFolder = folderAnswer['directory']

    clear()
    chooseFile()

def chooseFile():
    global chosenFolder

    if (chosenFolder != None):
        files = []

        for file in os.listdir(chosenFolder):
            if (file.endswith('.py')):
                files.append(file)
            
        files.append('Go back')

        fileAnswer = inquirer.prompt([
            inquirer.List('file', message = 'Select an exercise', choices = files)
        ])

        fileAnswer = fileAnswer['file']

        if (fileAnswer == 'Go back'):
            clear()
            chosenFolder = None
            chooseFolder()

        else:
            with open(os.devnull, 'w') as devnull:
                Popen(['python3', f'{chosenFolder}/{fileAnswer}'], stdout = devnull, stderr = devnull)

            clear()
            chooseFile()
    else:
        print('No folder was selected.')

chooseFolder()