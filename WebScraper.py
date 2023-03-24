from bs4 import BeautifulSoup
import re
from googletrans import Translator
import os
from fnmatch import fnmatch


#This function retrives the word/content then translates it to the language you choose.
def TranslateWord(word):
    translator = Translator()
    new_word = translator.translate(word, dest='hi')
    return new_word.text


def openWebPage(currentPageUrl):
    # read the HTML file
    with open(currentPageUrl, encoding="utf8") as fp:
        soup = BeautifulSoup(fp, "html.parser")

    # regex - to filter out html tags/scripts that might seen like content
    regex = re.compile('[@_!#$^*<>?/\|}{]')

    # find all occurrences of the text ' data '
    for x in range(len(soup.find_all())) :
        # Extract only content value
        data = soup.find_all()[x].string

        # Validate data value before parsing and replacing the new value
        if regex.search(str(data)) == None and data!=None and data!="None" and data is not None and data != "\n":        
            translated_word = TranslateWord(str(data))
            newd = translated_word
            print(data,newd)

            # replace the text with "new_data"
            data.replace_with(TranslateWord(newd))

    # write the modified HTML back to the file
    with open(currentPageUrl, "w", encoding="utf8") as fp:
        fp.write(str(soup))

folder = '' # the root folder location containing all your source code eg. 'MyWebsite SourceCode'
fileName = '' # The html page location that is first loaded eg. 'MyWebsite SourceCode/index.html

with open(fileName, encoding="utf8") as fp:
    soup = BeautifulSoup(fp, "html.parser")

for link in soup.find_all('a', href=True):
    if ".htm" in link['href'][-5:]: # check if the link extention is an html file
        url = folder + link['href']
        print(url)
        openWebPage(url)
    else:
        print("Unable to find .html file(s).")
