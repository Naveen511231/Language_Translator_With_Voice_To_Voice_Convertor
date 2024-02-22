import tkinter as tk
from tkinter import ttk

import speech_recognition as sr

from gtts import gTTS
import os
win=tk.Tk()

win.title("Translator")


from googletrans import LANGUAGES
t=[]
for  name in LANGUAGES.items():
    t.append(name)
t=tuple(t)


def main_translate(choosen,choosen1,text_entered):
    for i in range(len(t)):
        
        if(choosen==t[i][1]):
            choosen_store=t[i][0]
            break
    for i in range(len(t)):
        if(choosen1==t[i][1]):
            choosen_store1=t[i][0]
            break
    
    from googletrans import Translator
    translator = Translator()

    sentence=text_entered

    
    translated_sentence =translator.translate(sentence, src=choosen_store,dest=choosen_store1)
    text=translated_sentence.text
    input_text1=tk.Label(win,width=50,text=text,font='5px')
    input_text1.grid(row=2,column=4)
    
    print(text,choosen_store1)
    # Create a gTTS object
    tts = gTTS(text=text, lang=choosen_store1)
    # Save the speech as an audio file
    tts.save("example.mp3")

# # Play the audio file  
    os.system("start example.mp3")
    return text


 
def translate():
    first_language_choosen=Language_selector.get()

    first_language_choosen1=Language_selector1.get()

    text_entered=start_language.get()

    main_translate(first_language_choosen,first_language_choosen1,text_entered)

def translate1():
    first_language_choosen=Language_selector.get()

    first_language_choosen1=Language_selector1.get()

    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something:")
        audio = recognizer.listen(source)
        try:
            # Use Google Web Speech API to recognize the audio
            text = recognizer.recognize_google(audio)
            print("You said:", text)
        except sr.UnknownValueError:
            print("Could not understand audio.")

    text_entered=text
    # input_text=tk.Entry(win, width=50,textvariable=text).grid(row=2,column=0)
    start_language.set(text_entered)
    main_translate(first_language_choosen,first_language_choosen1,text_entered)
 
#Column 1 for first language
start_language=tk.StringVar()
start_language1=tk.StringVar()
Language_selector=ttk.Combobox(win,width=10, state="readonly",font='5px')#select language

first_selected_language=[]
for i in range(len(t)):
    first_selected_language.append(t[i][1])
first_selected_language_tuple=tuple(first_selected_language)
Language_selector["value"]=first_selected_language_tuple
    

Language_selector.grid(row=0,column=0)
Language_selector.current(21)


input_text=tk.Entry(win,width=40,textvariable=start_language,font='5px').grid(row=2,column=0)
speak=tk.Button(win,width=8,text="Speak", command=translate1,background='light blue',font='x-bold')
speak.grid(row=2, column=2,padx=10,pady=10)

#Column 2 for first language

Language_selector1=ttk.Combobox(win,width=10, state="readonly",font='5px')



Language_selector1['value']=first_selected_language_tuple



Language_selector1.grid(row=0,column=4, padx=50)
Language_selector1.current(38)

Trans_btn=tk.Button(win, text="Translate",command=translate,font='x-bold',background='light gray').grid(row=1,column=2)



win.mainloop()











