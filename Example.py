import convertEpubToText
from os import listdir
from os.path import isfile, join
mypath = "C:/Users/kevin.pineda/OneDrive - FINAC S.A.S/Desktop/Python/EpubOne/"
onlyfiles = [file for file in listdir(mypath) if isfile(join(mypath, file))]   
     
convertEpubToText.ConvertEpubToText(onlyfiles,mypath, ".").ConvertOneFile()