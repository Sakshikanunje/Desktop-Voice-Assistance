import pyttsx3
import wikipedia
import datetime
import os
import webbrowser
import speech_recognition as sr
import smtplib
import wolframalpha
import pywhatkit as kit 
import pyjokes
import operator
import cv2
import pyautogui
import time
import json
import requests
from bs4 import BeautifulSoup

import requests
from tkinter import *
from PIL import ImageTk
from PIL import Image

print("INITIALIZING DAVID....")


master = "Sir"

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)


def speak(text):
    engine.say(text)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I am David. Please tell me how may I help you")       

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('davidassistant123@gmail.com', 'david@123')
    server.sendmail('davidassistant123@gmail.com',to, content)
    server.close()

class Widget:
    def __init__(self):
       root = Tk()
       root.title('Voice Assistant')
       root.config(background='Red')
       root.geometry('1200x580')
       root.resizable(0, 0)
       img = ImageTk.PhotoImage(Image.open(r"C:\Users\Pratiksha\Desktop\Myproject\GUI.JPG"))
       panel = Label(root, image = img)
       panel.pack(side='right', fill='both',expand = "no")

       

       self.compText = StringVar()
       self.userText = StringVar()

       self.userText.set('Click \'Run David \' to Give commands')

       userFrame = LabelFrame(root, text="User", font=('Black ops one',14, 'bold'))
       userFrame.pack(fill="both", expand="yes")
         
       left2 = Message(userFrame, textvariable=self.userText, bg='#3B3B98', fg='white')
       left2.config(font=("Century Gothic", 24, 'bold'))
       left2.pack(fill='both', expand='yes')

       compFrame = LabelFrame(root, text="David", font=('Black ops one',14, 'bold'))
       compFrame.pack(fill="both", expand="yes")
         
       left1 = Message(compFrame, textvariable=self.compText, bg='#3B3B98',fg='white')
       left1.config(font=("Century Gothic", 24, 'bold'))
       left1.pack(fill='both', expand='yes')
       
       btn = Button(root, text='Run David', font=('Black ops one', 22, 'bold'), bg='#4b4b4b', fg='white',command=self.clicked).pack(fill='x', expand='no')
       btn2 = Button(root, text='Close!', font=('Black Ops One', 22, 'bold'), bg='#4b4b4b', fg='white',command=root.destroy).pack(fill='x', expand='no')

       
       
       self.compText.set('Hello, I am David! Please tell me How may I help you ??')

       root.bind("<Return>",self.clicked) # handle the enter key event of your keyboard
       root.mainloop()

    def clicked(self):
        print('Working')
        query = takeCommand()
        self.userText.set('Listening...')
        self.userText.set(query)
        query = query.lower()

     # Wikipedia
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)


        elif 'open youtube' in query:
            speak("Opening youtube")
            webbrowser.open("youtube.com")
            

        elif 'open google' in query:
            speak("Opening google")
            webbrowser.open("google.com")


        elif 'open gmail' in query:
            speak("Opening gmail")
            webbrowser.open("gmail.com")

         #Open Chrome 
        elif 'open chrome' in query:
            codePath = r"C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(codePath)


        elif 'open notepad' in query:
            codePath = "C:\\Program Files\\Notepad++\\notepad++.exe"
            os.startfile(codePath)


        # Play Offline Music
        elif 'play music' in query.lower():
           speak("Alright playing music")
           songs_dir="C:\\Users\\Pratiksha\\Music" 
           songs=os.listdir(songs_dir)
           print(songs)
           os.startfile(os.path.join(songs_dir,songs[0]))


        # Play online music
        elif ' song' in query:
            query=query.replace(' song','')
            results=kit.playonyt(query,'')


        #you tube search
        elif "on youtube" in query:
            query=query.replace(" On youtube","")
            results=kit.playonyt(query,"")


        # Time
        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"The time is {strTime}")


        # Tell Jokes
        elif 'joke' in query:
            a=pyjokes.get_joke()
            speak(a)
            print(a)


        # News
        elif 'news' in query:
            news = webbrowser.open_new_tab("https://timesofindia.indiatimes.com/home/headlines")
            speak('Here are some headlines from the Times of India,Happy reading')


        # Calculator
        elif "calculate" in query:  
           # write your wolframalpha app_id here 
            app_id = "A4VE3K-Y4UK6TEQQ3" 
            client = wolframalpha.Client("A4VE3K-Y4UK6TEQQ3") 
            indx = query.lower().split().index('calculate') 
            query = query.split()[indx + 1:] 
            res = client.query(' '.join(query)) 
            answer = next(res.results).text 
            print("The answer is " + answer)
            speak("The answer is " + answer)

        
         # Notes
        elif "write note" in query:
            speak("What should i write, sir")
            note = takeCommand()+"\n"
            file = open('david.txt', 'a')
            speak("Madam, Should i include date and time")
            snfm = takeCommand()
            if 'yes' in snfm:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                file.write(strTime)
                file.write(" :- ")
                file.writelines(note)
                print("Note Write Successfully")
            else:
                file.write(note)
            print("Note Write Successfully")


        #show notes
        elif 'show note' in query:
            speak("showing notes")
            file=open('david.txt','r')
            print(file.read())
            speak(file.read())


        #Timer
        elif 'stopwatch' in query:
            speak("For how many minutes ? ")
            timing=takeCommand()
            timing=timing.replace("minute"," ")
            timing=timing.replace("minutes"," ")
            timing=timing.replace("for"," ")
            timing=float(timing)
            timing=timing*60
            speak(f"I will remaind you in {timing} seconds")
            time.sleep(timing)
            speak("Your time has been finish")

        # Location
        elif 'location' in query:
            speak('Searching location')
            query = query.replace(" "," ")
            results =webbrowser.open(query)
            speak("here is your result")


        #weather
        elif "weather" in query:
            search="temperature in "
            search = query.replace(" weather", "")
            url = f"https://www.google.com/search?q={search}"
            r = requests.get(url)
            data = BeautifulSoup(r.text,"html.parser")
            temp =data.find("div",class_="BNeawe").text
            speak(f"current{search} is {temp}")
            print("temperature is" + temp )


        # Camera
        elif 'open camera' in query:
            cam=cv2.VideoCapture(0)
            img_counter=0
            while True:
                ret,frame=cam.read()
                if not ret:
                    print("Failed to Grab Frame")
                    break
                cv2.imshow("WebCam",frame)
                k=cv2.waitKey(1)
                if k%256==27:
                    break
                elif k%256==32:
                    img_name="Photo_{}.png".format(img_counter)
                    cv2.imwrite(img_name,frame)
                    print("Photo Captured")
                    speak("Photo Captured")
                    img_counter+=1
            cam.release()
            cv2.destroyAllWindows()


        # send email
        elif 'send email' in query:
            try:
                speak("Whome should I send?please enter Email id")
                to = input()
                speak("What should I say?")
                content = takeCommand()
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend . I am not able to send this email")


        # Change window
        elif 'change window' in query:
            pyautogui.keyDown("alt")
            pyautogui.press("tab")
            time.sleep(5)
            pyautogui.keyUp("alt")


        # change background
        elif 'change background' in query:
            ctypes.windll.user32.SystemParametersInfoW(20,0,"location of wallpaper",0)
            speak("Background Change Successfully")

            
        elif 'thank you' in query.lower():
            speak("Its my pleasure to always help you")


        elif 'sorry' in query.lower():
            speak("well if you really are then say it to my master") 

        elif 'please' in query.lower():
            speak("Don't say please !!!... I'm always here to help you")       
                
        elif 'what can you do' in query.lower():
            speak("its better if you ask what kind of assistant you are")

        elif'what kind of assistant are you' in query.lower():
            speak("kind of helpful")

        elif'help me'in query.lower():
            speak("always ready to help you")

        elif 'what is your name' in query.lower():
            speak("David")
            
        elif 'who made you' in query.lower():
            speak("GPK Students")

        elif 'ok google' in query.lower():
            speak("thats not me my friend....i am david")

        elif 'hey siri' in query.lower():
            speak("i am david ,how can you forget something which is created by you sir") 

        elif 'i want to be rich' in query.lower():
            speak("so do i") 


        # Empty Recycle Bin
        elif "empty recycle bin" in query:
            winshell.recycle_bin().empty(confirm=False,show_progress=False,sound=True)
            speak("Recycle Bin Empty")

        
        # Sleep the System
        elif 'sleep the system' in query:
            os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")

        
        # Restart the System
        elif "restart the system" in query:
            os.system("shutdown /r /t 5")


        # Shut Down
        elif "shutdown the system" in query:
            os.system("shutdown /s /t 5")


        elif 'exit' in query:
            speak("Thanks for giving me your time")
            exit()

if __name__ == "__main__":
    wishMe()
    Widget()