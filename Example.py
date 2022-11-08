import convertEpubToText
from os import listdir
from os.path import isfile, join
mypath = "./Epub/"
onlyfiles = [file for file in listdir(mypath) if isfile(join(mypath, file))]   
     
convertEpubToText.ConvertEpubToText(onlyfiles,mypath).Convert()