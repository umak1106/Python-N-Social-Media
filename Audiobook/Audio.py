import PyPDF2
import pyttsx3
book_read= PyPDF2.PdfFileReader(open('C:/Pypro/Audiobook/D.C.-10.pdf', 'rb'))
audio = pyttsx3.init()
for pg in range(book_read.numPages):
    text =  book_read.getPage(pg).extractText()
    audio.say(text)
    audio.runAndWait()
audio.stop()
engine.save(text, 'audio.mp3')
engine.runAndWait()
