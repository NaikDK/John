# from tkinter import *
import Greetings
import datetime
import os
import pywhatkit
import pyttsx3
import datetime
import windowsapps
import speech_recognition as sr
import threading
import winsound


engine = pyttsx3.init()
wishings = ["good morning", "good noon", "good afternoon", "good evening", "good night"]
r = sr.Recognizer()
Intents = {'hello':'Hello, tell me what can I do for you?',
           'wish me luck': 'Best of Luck',
           'thank you': 'Anytime',
           'thanks': 'Anytime!!',
           'f*** off': 'No, You Fuck off!!'}

def talk(text):
    engine.say(text)
    engine.runAndWait()
def wish_user():
    hour = int(datetime.datetime.now().strftime("%H"))
    print(hour)
    if hour>=0 and hour<6:
        print(hour)
        talk("You should consider going to sleep early..")
    elif hour>=6 and hour<12:
        print(hour)
        talk("Good Morning!")
    elif hour>=12 and hour<14:
        print(hour)
        talk("Good Noon")
    elif hour>=14 and hour<16:
        print(hour)
        talk("Good Afternoon")
    elif hour>=16 and hour<20:
        print(hour)
        talk("Good Evening")
    elif hour>=20:
        print(hour)
        talk("Good Night")
def listen():
    try:
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source)
            command = ""
            # r.pause_threshold = 0.3
            command = r.recognize_google(audio)
            # print(command)
            command = command.lower()
            print(command)
            # if command in Intents.keys:
            #     print('Here...')
            #     talk(Intents[command])
            #     return command
            # el
            if 'hey john' in command:
                command = command.replace('hey john', '')
                return command
            else:
                return command
    except sr.UnknownValueError:
        talk("Sorry, I was not able to hear you.")
    except Exception:
        talk("Try that again")
def alarm(time):
    # Function to set an alarm at given time
    if time[1] == ' ':  #remove space and add ':' between hour and minute
        time[1] = ':'
    if time[2] == ' ':  #remove space and add ':' between hour and minute
        time[2] = ':'
    if time.endswith("p.m."):   #put p.m. as pm to format the time
        time = time.replace("p.m.", "pm")
    if time.endswith("a.m."):   #put a.m. as am to format the time
        time = time.replace("a.m.", "am")
    print(time)
    oDateTime = datetime.datetime.strptime(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "%Y-%m-%d %H:%M:%S")
    date = oDateTime.date().strftime("%Y-%m-%d")
    day = oDateTime.date()
    # time = '8 pm'
    datetime_time = datetime.datetime.strptime(time, "%I:%M %p").time().strftime("%H:%M:%S")
    
    datetime_time = date + ' ' + datetime_time
    alarm_time = datetime.datetime.strptime(datetime_time, "%Y-%m-%d %H:%M:%S")
    if alarm_time < oDateTime:
        alarm_time += datetime.timedelta(days=1)
        print(alarm_time)
    talk("Alarm is set for " + datetime.datetime.strftime(alarm_time, "%I:%M %p"))
    # print(datetime_time)
    while(True):
        oDateTime = datetime.datetime.strptime(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "%Y-%m-%d %H:%M:%S")
        if(alarm_time == oDateTime):
            print("Its time for your alarm!!!!")
            winsound.MessageBeep(type=winsound.MB_OK)
            break
def run_john():
    # wish_user()
    print("Listening...")
    command = listen()
    print(command)
    if command == 'john':
        talk('Yes Sir!')
    elif 'play' in command:
        command = command.replace('play', '')
        talk("playing" + command)
        pywhatkit.playonyt(command)
    elif 'time' in command:
        time = datetime.datetime.now().strftime("%I:%M %p")
        talk(time)
    elif command in wishings:
        talk("Take care!!")
    elif 'start excel' in command:
        os.system("start excel")
    elif 'start word' in command:
        os.system("start winword")
    elif 'start outlook' in command:
        os.system("start outlook")
    elif 'set an alarm for' in command:
        time = command
        time = time.replace('set an alarm for ', "")
        t1 = threading.Thread(target = alarm, args=(time, ))
        t1.start()
    elif command == 'quit' or 'shut up' in command or command == 'close':
        talk("Shutting it Down!")
        exit()
    else:
        talk("Sorry Can you repeat that?")
    
if __name__ == "__main__":
    # wish_user()
    talk(Greetings.greet_user())
    while(True):
        run_john()