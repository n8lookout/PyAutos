import pyttsx3, PyPDF2

# Unfortunately doesn't produce a working mp3

with open('Blumenfeld.pdf', 'rb') as pdf_file:
    pdfreader = PyPDF2.PdfReader(pdf_file)
    speaker = pyttsx3.init()

    for page_num in range(len(pdfreader.pages)):
        text = pdfreader.pages[page_num].extract_text()
        clean_text = text.strip().replace('\n', ' ')
        print(clean_text)

    speaker.save_to_file(clean_text, 'Blumenfeld.mp3')
    speaker.runAndWait()

    speaker.stop()
