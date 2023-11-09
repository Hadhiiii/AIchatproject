import datetime
import sys
import pyfirmata
import pyttsx3
import speech_recognition as sr
import webbrowser
import os
import wikipedia
import cv2
import winsound
from pyfirmata import Arduino, SERVO,PWM
from time import sleep
import pyautogui

assistant = pyttsx3.init()
voices = assistant.getProperty('voices')
assistant.setProperty('voice', voices[1].id)
voicespeed = 170
assistant.setProperty('rate', voicespeed)

port = ''
board = Arduino('COM4')

spin = 6
relay1_pin = 2
relay2_pin = 3
relay3_pin = 4
relay4_pin = 5
led_pin = 8
board.digital[spin].mode = SERVO
board.digital[led_pin].mode = pyfirmata.OUTPUT
board.digital[relay1_pin].mode = pyfirmata.OUTPUT
board.digital[relay2_pin].mode = pyfirmata.OUTPUT
board.digital[relay3_pin].mode = pyfirmata.OUTPUT
board.digital[relay4_pin].mode = pyfirmata.OUTPUT
def time():
    time = datetime.datetime.now().strftime("%H:%M")
    speak("the time is "+ time)
    print(time)
def current_date():
    td = datetime.datetime.now().date()
    speak('todays date is '+ str(td))
    print(td)


def relay1_on():
    board.digital[relay1_pin].write(0)
def relay1_off():
    board.digital[relay1_pin].write(1)
def relay2_on():
    board.digital[relay2_pin].write(0)
def relay2_off():
    board.digital[relay2_pin].write(1)
def relay3_on():
    board.digital[relay3_pin].write(0)
def relay3_off():
    board.digital[relay3_pin].write(1)
def relay4_on():
    board.digital[relay4_pin].write(0)
def relay4_off():
    board.digital[relay4_pin].write(1)
def rotateservo(spin , angle):
    board.digital[spin].write(angle)
    sleep(0.015)
def speak(audio):
    board.digital[led_pin].write(1)
    assistant.say(audio)
    assistant.runAndWait()
    board.digital[led_pin].write(0)


def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print('listening....')
        r.pause_threshold = 1
        audio = r.listen(source)
        winsound.Beep(2000, 100)

    try:
        print('recognising...')
        query = r.recognize_google(audio, language='en-in')
    except Exception as e:
        print('')
        return '_______________________________________'
    return query

def wishme():

    hour = datetime.datetime.now().hour
    if hour >= 6 and hour <= 12:
        speak('Good morning  sir. how can i help you today ')
    elif hour >= 12 and hour <= 18:
        speak('Good afternoon sir. what do you want me to do')
    elif hour >= 18 and hour <= 24:
        speak('Good evening sir.')
    else:
        speak('good night, sweet dreams')
def assisstant(): 
    while True:
        query = takecommand().lower()
        print(query)

        if "good morning" in query:
            hour = datetime.datetime.now().hour
            if hour >= 6 and hour <= 12:
                speak('Good morning  sir. how can i help you today ')
            elif hour >= 12 and hour <= 18:
                speak("sorry sir, it's good afternoon not morning")
            elif hour >= 18 and hour <= 24:
                speak('no sir, it is Good evening sir.')

        elif "good afternoon" in query:
            hour = datetime.datetime.now().hour
            if hour >= 6 and hour <= 12:
                speak("sorry sir, it's good morning not good afternoon")
            elif hour >= 12 and hour <= 18:
                speak("Good afternoon sir. how can i help you today")
            elif hour >= 18 and hour <= 24:
                speak('no sir, it is Good evening sir.')

        elif 'bitch' in query or 'fuck' in query or 'bastard' in query or 'shit' in query:
            speak('damn that is bad language, try improving your fucking attitude')
            print('* ******** **** ******')

        elif "date" in query:
            current_date()
            time()

        elif "what's up" in query:
            speak('i am doing great, thanks for asking')
            print('i am doing great, thanks for asking')


        elif "hello" in query:
            speak('hey,whats up sir')
            print('hi, how you doing? sir')

        elif "i love you" in query:
            speak("aw, that's sweet ")
            print('sorry, my feeling are very personal i have to ask my creator ')

        elif "time" in  query:
            time()
            current_date()

        elif "hey jarvis" in query or "hi jarvis " in query:
            speak('at your service, sir')
            print('at your service, sir')

        elif "what's your name"  in query:
            print("hi! my name is J.A.R.V.I.S. Im an AI voice assistant, I can do everything that I am programmed to do ")
            speak('hi! my name is jarvis. I am  an AI voice assistant I can do everything that I am programmed to do ')

        elif "what's your name" in query:
            print("hi! my name is J.A.R.V.I.S. Im an AI voice assistant, I can do everything that I am programmed to do ")
            speak('hi! my name is jarvis. I am  an AI voice assistant I can do everything that I am programmed to do ')


        elif "what is your name"  in query:
            print("hi! my name is J.A.R.V.I.S. Im an AI voice assistant, I can do everything that I am programmed to do ")
            speak('hi! my name is jarvis. I am  an AI voice assistant I can do everything that I am programmed to do ')

        elif "introduce yourself"  in query:
            print("hi! my name is J.A.R.V.I.S. Im an AI voice assistant,i am created by a group of 4 members named ben, blessen, nizam, mahroof. I am capable of doing everything that I am programmed to do ")
            speak('hi! my name is jarvis. I am  an AI voice assistant ,i am created by a group of 4 members named ben, blessen, nizam, mahroof. I am capable of doing everything that I am programmed to do ')

        elif "how are you" in query:
            speak('i am fine thanks. how about you sir')
            print('i am fine thanks. how about you sir')

        elif "i'm good " in query:
            speak("that's good to hear")
            print("that's good to hear")

        elif "i'm doing great " in query:
            speak("that's good to hear")
            print("that's good to hear")

        elif "who made you" in query:
            print("i dont know his name but i am sure that he is extremely talented")
            speak("i dont know his name but i am sure that he is extremely talented")

        elif "who created you" in query:
            print("i dont know his name but i am sure that he is extremely talented")
            speak("i dont know his name but i am sure that he is extremely talented")

        elif "just open youtube" in query:
            speak('ok, sir. opening youtube')
            print('ok, sir. opening youtube')
            webbrowser.open_new('https://youtube.com')

        elif "open youtube" in query:
            speak("what would you like to watch? sir")
            qrry=takecommand().lower()
            webbrowser.open(f"https://www.youtube.com/results?search_query={qrry}")

        elif "search youtube about" in query:
            query = query.replace("search youtube about",'')
            webbrowser.open(f"https://www.youtube.com/results?search_query={query}")

        elif "search wikipedia about" in query:
            speak("searching wikipedia")
            query = query.replace("search wikipedia about",'')
            try:
                result = wikipedia.summary(query,sentences=1)
                speak('according to wikipedia')
                print(result)
                speak(result)
            except:
                speak('try searching something else')

        elif "just open google" in query:
            speak('opening google')
            print('opening google')
            webbrowser.open_new('https://www.google.com')

        elif "open google" in query:
            speak('what should i search sir')
            qry = takecommand().lower()
            speak('searching google about' + qry)
            webbrowser.open(f"https://www.google.com/search?q={qry}")
            try:
                result=wikipedia.summary(qry,sentences=1)
                print(result)
                speak(result)
            except:
                speak("i can't be bothered to read this for you, so read it yourself")

        elif "search google about" in query:
            query = query.replace("search google about","")
            speak('searching google about' + query )
            webbrowser.open(f"https://www.google.com/search?q={query}")
            try:
                result = wikipedia.summary(query, sentences=2)
                print(result)
                speak(result)
            except:
                speak("i can't be bothered to read this for you, so read it yourself")

        elif "search google on" in query:
            query = query.replace("search google on","")
            speak('searching google on' + query)
            webbrowser.open(f"https://www.google.com/search?q={query}")
            try:
                result = wikipedia.summary(query, sentences=2)
                print(result)
                speak(result)
            except:
                speak("i can't be bothered to read this for you, so read it yourself")

        elif "close browser" in query:
            speak('closing the browser sir')
            print('closing the browser sir')
            os.system("taskkill /f /im brave.exe")

        elif "open paint" in query:
            speak('ok sir, opening paint')
            npath = "C:\Windows\system32\\mspaint.exe"
            os.startfile(npath)

        elif "close paint" in query:
            speak('ok sir, closing paint')
            os.system("taskkill /f /im mspaint.exe")

        elif "open cmd" in query:
            speak('ok sir, initialising command prompt')
            os.system('start cmd')

        elif "open command prompt" in query:
            speak('ok sir, initialising command prompt')
            os.system('start cmd')

        elif "close command prompt" in query:
            speak('ok sir, terminating command prompt')
            os.system('taskkill /f /im cmd.exe')

        elif "close cmd" in query:
            speak('ok sir, terminating command prompt')
            os.system('taskkill /f /im cmd.exe')

        elif "open notepad" in query:
            speak('ok sir, opening notepad')
            npath = "C:\Windows\system32\\notepad.exe"
            os.startfile(npath)

        elif "sing a song" in query:
            speak(' ok sir i will sing a song ')
            print(' ok sir i will sing a song ')
            winsound.PlaySound('ashiq_song.wav', winsound.SND_FILENAME)

        elif 'thank you' in query:
            speak('it is my pleasure.')
            print('it is my pleasure.')

        elif 'thanks' in query:
            speak('you are welcome')
            print('you are welcome')

        elif "close notepad" in query:
            speak('ok sir, closing notepad')
            os.system('taskkill /f /im notepad.exe')

        elif "shutdown the system" in query:
            speak('shuting down the system')
            os.system('shutdown /s /t 5')

        elif 'restart the system' in query:
            speak('restarting the system')
            os.system('shutdown /r /t 5')

        elif "open camera" in query:
            cam = cv2.VideoCapture(0)
            while True:
                ret, img = cam.read()
                cv2.imshow('webcam', img)
                k = cv2.waitKey(50)
                if k==27:
                    break
                cam.release()
                cv2.destroyAllWindows()

        elif "go to sleep" in query:
            speak("alright then, i'm going to sleep")
            sys.exit()

        elif 'open the gate' in query:
            speak('okay sir,opening the gate')
            print('okay sir,opening the gate')
            for i in range(0, 90):
                rotateservo(spin, i)
                sleep(0)

        elif 'close the gate' in query:
            speak('okay sir,closing the gate')
            print('okay sir,closing the gate')
            for i in range(90,1,-1):
                rotateservo(spin,i)
                sleep(0)

        elif 'turn on the light' in query or "light's please" in query:
            speak('turning on the street light')
            print('turning on the street light')
            relay2_on()

        elif 'turn off the light' in query:
            speak('turning off the light')
            print('turning off the light')
            relay2_off()

        elif 'turn on the ambient light' in query:
            speak('turning on the ambient  light')
            print('turning on the street light')
            relay1_on()

        elif 'turn off the ambient light' in query:
            speak('turning off the ambient light')
            print('turning off the ambient light')
            relay1_off()

        elif 'turn on all the light' in query:
            speak('turning on all lights')
            print('turning on all the light')
            relay1_on()
            relay2_on()

        elif 'turn off all the light' in query or 'turn off all light' in query :
            speak('terminating all lights')
            print('terminating')
            relay1_off()
            relay2_off()

        elif 'turn up the volume' in query or "it's too quiet" in query:
            speak('okay slighty raising the volume')
            print('okay raising the volume')
            for i in range(10):
                pyautogui.press("volumeup")

        elif 'turn down the volume' in query or "it's too loud" in query:
            speak('alright sir, slightly lowering the volume by 20 percent')
            print('okay lowering the volume by 20 percent')
            for i in range(10):
                pyautogui.press("volumedown")

        elif 'what do you want me to do' in query:
            speak('t')

        elif '_______________________________________' in query:
            print('')

        else:
            speak('sorry sir i cant do that right now try asking something else')

speak('initialising automation')
relay1_off()
relay2_off()
relay3_off()
relay4_off()
wishme()

while (True):
    assisstant()