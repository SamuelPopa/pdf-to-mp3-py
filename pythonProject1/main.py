import PyPDF2
import pyttsx3

with open('CursEIVAC-VP1.pdf', 'rb') as pdf_file:
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    text = ''
    for i in range(len(pdf_reader.pages)):
        text += pdf_reader.pages[i].extract_text()

engine = pyttsx3.init()
engine.save_to_file(text, 'output.mp3')
engine.runAndWait()