import pyttsx3 
import speech_recognition as sr 
import datetime   
import wikipedia 
import webbrowser
import os
import smtplib
import wolframalpha
import pyjokes
import operator
import cv2
import pyautogui
import time
import json
import requests 
from bs4 import BeautifulSoup
import pywhatkit as kit
import ctypes
import winshell

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
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

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

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
            speak("Opening chrome")
            codePath = r"C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(codePath)


        elif 'open notepad' in query:
            speak("Opening notepad++")
            codePath = "C:\\Program Files\\Notepad++\\notepad++.exe"
            os.startfile(codePath)


        # Play Offline Music
        elif 'play offline music' in query.lower():
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
            print(f"The time is {strTime}")
            speak(f"The time is {strTime}")


        # Tell Jokes
        elif 'joke' in query:
            a=pyjokes.get_joke()
            print(a)
            speak(a)


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
                strTime = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
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
            print(f"I will remaind you in {timing} seconds")
            speak(f"I will remaind you in {timing} seconds")
            time.sleep(timing)
            print("Your time has been finish")
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
                speak("What should I send?")
                content=takeCommand()
                #while content!="stop" in query:
                    #c=c+content
                   # content = takeCommand()
                sendEmail(to, content)
                print("Email has been sent!")
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend . I am not able to send this email")


        # Change window
        elif 'change window' in query:
            pyautogui.keyDown("alt")
            pyautogui.press("tab")
            time.sleep(10)
            pyautogui.keyUp("alt")


        # change background
        elif 'change background' in query:
            ctypes.windll.user32.SystemParametersInfoW(20,0,"location of wallpaper",0)
            speak("Background Change Successfully")


        # Empty Recycle Bin
        elif "empty recycle bin" in query:
            try:
                winshell.recycle_bin().empty(confirm=False,show_progress=False,sound=True)
                print("Recycle Bin Has Been Empty")
                speak("Recycle Bin Has Been Empty")
            except:
                print("Recycle Bin has already empty")
                speak("Recycle Bin has already empty")

        
        # Sleep the System
        elif 'sleep the system' in query:
            os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")

        
        # Restart the System
        elif "restart the system" in query:
            os.system("shutdown /r /t 5")


        # Shut Down
        elif "shutdown the system" in query:
            os.system("shutdown /s /t 5")

        elif 'thank you' in query.lower():
            print("Its my pleasure to always help you")
            speak("Its my pleasure to always help you")


        elif 'sorry' in query.lower():
            print("well if you really are then say it to my master")
            speak("well if you really are then say it to my master") 

        elif 'please' in query.lower():
            print("Don't say please !!!... I'm always here to help you")
            speak("Don't say please !!!... I'm always here to help you")       
                
        elif 'what can you do' in query.lower():
            print("its better if you ask what kind of assistant you are")
            speak("its better if you ask what kind of assistant you are")

        elif'what kind of assistant are you' in query.lower():
            print("kind of helpful")
            speak("kind of helpful")

        elif'help me'in query.lower():
            print("always ready to help you")
            speak("always ready to help you")

        elif 'what is your name' in query.lower():
            print("My Name is David")
            speak("My Name is David")
            
        elif 'who made you' in query.lower():
            print("GPK Students - Pratiksha,Sakshi,Bhagyashri")
            speak("GPK Students - Pratiksha,Sakshi,Bhagyashri")

        elif 'ok google' in query.lower():
            print("thats not me my friend....i am david")
            speak("thats not me my friend....i am david")

        elif 'hey siri' in query.lower():
            print("i am david ,how can you forget something which is created by you sir")
            speak("i am david ,how can you forget something which is created by you sir") 

        elif 'exit' in query:
            print("Thanks for giving me your time")
            speak("Thanks for giving me your time")
            exit(0)

