from ebooklib import epub
from bs4 import BeautifulSoup
import os
import ebooklib
import io
import re

class ConvertEpubToText:
    def __init__(self,listBooks, pathEpubs, pathSave = "EpubsConvert" ):
        self.listBooks = listBooks
        self.pathSave = pathSave
        self.pathEpubs = pathEpubs
        
    def ChapterToStr(self, chapter):
        Soup = BeautifulSoup(chapter.get_body_content())
        TextChapter = [text.get_text() for text in Soup.find_all('p')]
        return ' '.join(TextChapter)
    
    def Cleanofstring(self, stringbyClean):
        Translate = stringbyClean.maketrans('“”èÃêâçàîüïìôö', '""éAeacáiuiioo')
        TextbyFile = stringbyClean.translate(Translate).replace("…", "...")
        TextbyFile = re.sub(r"[^a-zA-Z0-9 ñÑ()¡!¿?.,ÁÉÍÓÚáéíóú\[\]:;]","",TextbyFile)
        return TextbyFile
    
    def Convert(self):
        for bookname in self.listBooks:
            Book = epub.read_epub(self.pathEpubs+bookname)
            ItemsDocument = list(Book.get_items_of_type(ebooklib.ITEM_DOCUMENT))
            TextofEpub = ""
            for item in ItemsDocument:
                TextofEpub += self.ChapterToStr(item)
                
            NameFile = bookname.replace('.epub', '')
            TextComplet = "".join(TextofEpub.splitlines())
            TextbyFile = self.Cleanofstring(TextComplet)
            if(not os.path.isdir("./" + self.pathSave)):
                os.mkdir("./" + self.pathSave) 
            with io.open(f"{self.pathSave}/{NameFile}.txt", mode='a', encoding='utf-8') as file:
                file.write(TextbyFile)
                file.close()
                
    def SplitTextToWords(self, string, lenString):
        words = string.split()
        grouped_words = [' '.join(words[i: i + lenString]) for i in range(0, len(words), lenString)]
        return grouped_words
    
    def ConvertOneFile(self):
        for bookname in self.listBooks:
            Book = epub.read_epub(self.pathEpubs+bookname)
            ItemsDocument = list(Book.get_items_of_type(ebooklib.ITEM_DOCUMENT))
            TextofEpub = ""
            for item in ItemsDocument:
                TextofEpub += self.ChapterToStr(item)
            NameFile = bookname.replace('.epub', '')    
            TextComplet = "".join(TextofEpub.splitlines())
            TextbyFile = self.Cleanofstring(TextComplet)
            TextbyFile = TextbyFile.replace("...","$Tres")
            ListCsv = self.SplitTextToWords(TextbyFile,100)
            if(not os.path.isdir("./" + self.pathSave)):
                os.mkdir("./" + self.pathSave) 
            print(NameFile)
            for prhase in ListCsv:
                with io.open(f"{self.pathSave}/AllPrhase.txt", mode='a', encoding='utf-8') as file:
                    file.write(prhase.replace('$Tres','...').rstrip()+".\n")
                    file.close()