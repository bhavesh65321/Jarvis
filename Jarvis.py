from time import strftime
import pyttsx3                             # A python library that is helpful to Convert a text to Speech So, it is Text-Speech-Convert Library.
import datetime   
import speech_recognition as sp
import wikipedia
import webbrowser
import os

from wikipedia.wikipedia import random
                                           #pyttsx3 is a text-to-speech conversion library in Python. ... it is a very easy to use tool
                                           # which converts the entered text into speech. The pyttsx3 module supports two voices first is female and the second is male 
                                            # which is provided by “sapi5” for windows. It supports three TTS engines : sapi5 – SAPI5 on Windows

engine = pyttsx3.init('sapi5')       # sapi5 it is a microsoft API that provide by windows, isse hum ek voice select kr sakte hai jo hamare 
                                     #assistance ke use hogi
voices= engine.getProperty('voices')      # voice ko lena 
engine.setProperty('voice', voices[1].id)    #voice ko set karna

def speak(audio):
    engine.say(audio) 
    engine.runAndWait()            #Without this command, speech will not be audible to us.

def wishme():
    hour = int(datetime.datetime.now().hour)
    if(hour>=0 and hour<=12):
        speak("Goooood morning!")
    elif(hour>12 and hour<16):
        speak("Gooood afternoon!")
    else:
        speak("Gooood evening!")
    speak("hellooo sir , I'm your Assistance!")

def takecommand():
    '''its take microphone input from user(jo user bolega vo input lega) 
    and convert into the string and return string output'''
    r=sp.Recognizer()
    with sp.Microphone(device_index=0) as source:
        print("listening........")
        r.pause_threshold=1
        audio=r.listen(source)
    
    try:
        print("Recognizing...")
        query=r.recognize_google(audio, language='en-in') 
        '''Using google for voice recognition(matlab user se voice lene ke liye google ka voice recognizer
         use ho raha hai )'''
        print(f"User said: {query}\n")

    except Exception as e:
        speak("please Say again....")
        return "None"
    return query

    
        
if __name__=="__main__":
    speak("Good morning ! Bhavesh Soni")
    while True:
        query=takecommand().lower()
        if("bye" in query):
            speak("okay sir ! we will meet Soon...")
            break

        elif 'wikipedia' in query:
            speak("searching on wikipedia .....")
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query,sentences=2)
            speak("according to wikipedia")
            print(results)
            speak(results)
        elif 'youtube' in query:
            speak("yaa we are try to open youtube")
            webbrowser.open_new("youtube.com")
        elif 'google' in query:
            speak("yaa we are try to open google")
            webbrowser.open_new_tab('google.com')
        elif 'open Linkedin' in query:
            speak("Name of person whose linkedin you want to open")
            a=input()
            webbrowser.open(f"{0}/Linkedin.com".format(a))
        elif 'stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
        elif 'play music' in query:
            music_dir='D:\\download'
            songs=os.listdir(music_dir)
            print(songs,end=" ")
            os.startfile(os.path.join(music_dir,songs[0]))
        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}") #commit

            

