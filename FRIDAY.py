import pyttsx3
import datetime
import speech_recognition as sr
import sounddevice as sd
import numpy as np
import wikipedia
import webbrowser
import os
import smtplib
import time

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    time.sleep(0.8)

def WishMe():
    hour = int(datetime.datetime.now().hour)
    speak("initialising data and resources.....friday activated")
    if hour >= 0 and hour <= 12:
        speak("Good morning A.K")
    
    elif hour > 12 and hour <= 16:
        speak("Good afternoon A.K")
    
    elif hour >= 17 and hour <= 19:
        speak("Good evening A.K")
    
    else:
        speak("Hey A.K still woke up, how may i help you right now?")

def Email(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('ashishchaudhary8a@gmail.com', 'dysk uqjw xpoo zivl')
    server.sendmail('ashishchaudhary8a@gmail.com', to, content)
    server.close()

def take_Command():
    r = sr.Recognizer()
    fs = 16000       # sample rate
    duration = 5     # seconds

    print("Listening...")
    recording = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='int16')
    sd.wait()

    audio = sr.AudioData(recording.tobytes(), fs, 2)
    
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language = 'en-in')
        print("User said: ", query)

    except Exception as e:
        print(e)
        print("Say that again please 🤔...")
        return "None"   
    return query

if __name__ == '__main__':
    WishMe()
    # take_Command()

    # making the system run on our commands
    if 1:
        query = take_Command().lower()
        
        # query = query.lower()
        if "wikipedia" in query:
            print("Searching Wikipeidia...")
            query = query.replace('wikipedia', "")
            results = wikipedia.summary(query, sentences = 2)
            speak("According to wikipedia")
            speak(results)
            print(results)

        elif "open youtube" in query:
            webbrowser.open("youtube.com")

        elif "play music" in query:
            music_dir = 'C:\\Users\\DELL\\Music'
            songs = os.listdir(music_dir)
            print (songs)
            os.startfile(os.path.join(music_dir, songs[1]))
        
        elif "time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Well the time right now is {strTime}")
            print(strTime)
       
        elif "open code" in query:
            codePath = r"C:\Users\DELL\OneDrive\Desktop\Visual Studio Code.lnk"
            os.startfile(codePath)
        
        elif "send email" in query:

            try:
                speak("what should i say?")               
                content = take_Command()
                to = 'ashishchaudhary8a@gmail.com'
                Email(to, content)
                speak("Email sent")
                print("Email sent")
            except Exception as e:
                print(e)
                speak("sorry boss cant send the email😥")
                print("sorry boss cant send the email😥")
       
        # elif "quit" in query:
                # exit()