import os
import sys
from episodeTitles import getEpisodeTitle

def numberStringGenerator(prefix, number):
    stringPrefix = prefix
    if int(number) <= 9:
        returnString = stringPrefix + '0' + number
    else:
        returnString = stringPrefix + number
    return returnString

if len(sys.argv) != 4:
    print('Usage: python main.py [directory] [series name] [season]')
    sys.exit()

path =  sys.argv[1]
filenames = os.listdir(path)

episodeNumber = 1
for filename in filenames:

    name, fileExtension = os.path.splitext(filename)

    showTitle = sys.argv[2]
    seasonString = numberStringGenerator('S', sys.argv[3])
    episodeString = numberStringGenerator('E', str(episodeNumber))
    episodeTitle = getEpisodeTitle(showTitle, sys.argv[3], episodeNumber)

    newFilename = (showTitle + ' ' + seasonString + episodeString + ' - ' + episodeTitle + fileExtension)

    print('Renaming: ' + '\033[31m' + filename + '\033[0m' + ' to ' + '\033[1;32m' + newFilename + '\033[0m')
    os.rename((path + filename), (path + newFilename))

    episodeNumber = episodeNumber + 1