import tkinter
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import *
from tkinter import Text
import speech_recognition as sr
from playsound import playsound
import time
import os

root = tk.Tk()
root.title("Application")
listener = sr.Recognizer()

history_page = 1
rule_page = 1
description_page = 1
font = 11
sound = 0

#Change Page Function
def LEFT_RULE():
    global rule_page
    rule_page = rule_page - 1
    if(rule_page < 1):
        rule_page = 3
    RULES()
def RIGHT_RULE():
    global rule_page
    rule_page = rule_page  + 1
    if(rule_page > 3):
        rule_page = 1
    RULES()

#Sounds
def SOUNDS_RULE():
    global rule_page
    if (rule_page == 1):
        print("Rule page 1")
        playsound("output - Αντιγραφή (3).mp3")
    elif(rule_page == 2):
        print("Rule page 2")
        playsound("output - Αντιγραφή.mp3")
    elif(rule_page == 3):
        print("Rule page 3")
        playsound("output - Αντιγραφή (2).mp3")



#Page's Functions
def HISTORY():
    for widget in frame.winfo_children():
        widget.destroy()
    label = tk.Label(frame, text="History")
    label.pack()
    History=("Ειμαστε μια ομαδα εφηβων που φτιαχνουμε παιχνιδια για τυφλους και αυτο ειναι μια συντομη περιληψη για εμας. μπλα μπλα μπλα μπλα μπλα μπλα")
    text = tk.Text(frame, height = 50, width = 70)
    text.config(font=('Helvatical bold',font))
    text.insert(tk.END, History)
    text.configure(state='disabled')
    text.pack()
    

def RULES():
    history_page = 1
    description_page = 1
    
    for widget in frame.winfo_children():
        widget.destroy()
        
    #Buttons
    left = tk.Button(frame, text="<", padx = 5, pady = 5, fg="gray", bg="white", command = LEFT_RULE)
    left.pack(side=tk.LEFT)
    right = tk.Button(frame, text=">", padx = 5, pady = 5, fg="gray", bg="white", command = RIGHT_RULE)
    right.pack(side=tk.RIGHT)
    s = tk.Button(frame, text="Ακουσε τους κανόνες", padx = 100, pady = 10, fg="gray", bg="white", command = SOUNDS_RULE)
    s.pack(side=tk.BOTTOM)

    #Create title label
    label = tk.Label(frame, text="Κανόνες", font="arial")
    label.pack()

    #create text
    text = tk.Text(frame, height = 50, width = 70)
    text.config(font=('Helvatical bold',font))
    if(rule_page == 1):
        Rule=("Κανόνες παιχνιδιού\n\n1)Πρωτος κανόνας\n2)Δευτερος Κανόνας")
        text.insert(tk.END, Rule)
        text.pack()
    elif(rule_page == 2):
        Rule = ("Κανόνες παιχνιδιού\n\n3)Τρίτος κανόνας\n4)Τέταρτος Κανόνας")
        text.insert(tk.END, Rule)
        text.pack()
    elif(rule_page == 3):
        Rule = ("Κανόνες παιχνιδιού\n\n5)Πέμπτος κανόνας\n6)Έκτος Κανόνας")
        text.insert(tk.END, Rule)
        text.pack()


def DISCRIPTION():
    for widget in frame.winfo_children():
        widget.destroy()
    label = tk.Label(frame, text="Description")
    label.pack()
    

def VOICE():
    status = 1
    while(status==1):
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            print(command)
            if 'historia' in command:
                status = 0
                HISTORY()
            elif 'astoria' in command:
                status = 0
                HISTORY()
            elif 'history' in command:
                status = 0
                HISTORY()
            elif 'rules' in command:
                status = 0
                RULES()
            elif 'colones' in command:
                status = 0
                RULES()
            elif 'cananas' in command:
                status = 0
                RULES()
            elif 'gun known as' in command:
                status = 0
                RULES()
            elif 'canalis' in command:
                status = 0
                RULES()
            elif 'gonzales' in command:
                status = 0
                RULES()
            elif 'canoness' in command:
                status = 0
                RULES()
            elif 'facebook' in command:
                status = 0
                RULES()
            elif 'basketball' in command:
                status = 0
                RULES()
            elif 'bush' in command:
                status = 0
                RULES()
            elif 'benjamin' in command:
                status = 0
                RULES()
            elif 'belmont' in command:
                status = 0
                RULES()
            elif 'post' in command:
                status = 0
                RULES()

def AUTORULE():
    global rule_page
    while(rule_page <= 3):
        SOUNDS_RULE()
        rule_page = rule_page + 1
    rule_page = 1

def size():
    global font
    font = slider.get()
    HOMEPAGE()
    
def HOMEPAGE():
    global font
    for widget in frame.winfo_children():
        widget.destroy()
    title = tk.Label(frame, text="LUDO ERGO SUM", anchor=CENTER,)
    title.config(font=('Helvatical bold',font))
    title.pack()

    #Set up button for setting up font
    setfont = tk.Button(frame, padx = 400, pady = 10,
                        fg="gray", bg="white",text="Set Font", command = size)
    setfont.pack(side=tk.BOTTOM)

    #Set up slider for setting up font
    global slider
    slider = Scale(frame, bg='white', length = 300, from_=11, to=40,tickinterval=10, orient=HORIZONTAL)
    slider.set(font)
    slider.pack(side=tk.BOTTOM)
    
    

#Window's Base
canvas = tk.Canvas(root, height = 800, width = 1020, bg = "#263D42")
canvas.pack()

frame = tk.Frame(root, bg="white")
frame.place(relwidth = 0.8, relheight = 0.8, relx = 0.1, rely = 0.1)

#Set up Home page
HOMEPAGE()

#menu buttons
history = tk.Button(root, text="Ιστορία", padx = 68,
                    pady = 5, fg="white", bg="#263D42", command=HISTORY)
history.pack(side=tk.LEFT)

rules = tk.Button(root, text="Κανόνες", padx = 67.1,
                    pady = 5, fg="white", bg="#263D42", command=RULES)
rules.pack(side=tk.LEFT)

discription = tk.Button(root, text="Περιγραφή", padx = 67.1,
                    pady = 5, fg="white", bg="#263D42", command=DISCRIPTION)
discription.pack(side=tk.LEFT)

voice = tk.Button(root, text="Φωνή", padx = 67.1,
                    pady = 5, fg="white", bg="#263D42", command=VOICE)
voice.pack(side=tk.LEFT)

autorule = tk.Button(root, text="Ηχογράφιση", padx = 68,
                     pady = 5, fg="white", bg="#263D42", command = AUTORULE)
autorule.pack(side=tk.LEFT)

return_home = tk.Button(root, text="Home", padx = 10, pady = 5,
                        fg="white", bg="#263D42", command = HOMEPAGE)
return_home.pack(side=tk.LEFT)

root.mainloop()
