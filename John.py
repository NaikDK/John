import datetime
import os
import pywhatkit
import pyttsx3
import datetime
import windowsapps
import speech_recognition as sr

engine = pyttsx3.init()
wishings = ["good morning", "good noon", "good afternoon", "good evening", "good night"]
r = sr.Recognizer()

def talk(text):
    engine.say(text)
    engine.runAndWait()
def wish_user():
    hour = int(datetime.datetime.now().strftime("%H"))
    if 0>=hour>6:
        talk("You should cnsider going to sleep early..")
    elif 6>=hour>12:
        talk("Good Morning!")
    elif 12>=hour>14:
        talk("Good Noon")
    elif 14>=hour>16:
        talk("Good Afternoon")
    elif 16>=hour>20:
        talk("Good Evening")
    else:
        talk("Good Night")
def listen():
    try:
        with sr.Microphone() as source:
            print("Listening...")
            audio = r.listen(source)
            r.pause_threshold = 0.3
            command = r.recognize_google(audio)
            # print(command)
            command = command.lower()
            if 'hey josh' in command:
                command = command.replace('hey josh', '')
                return command
            else:
                return command
    except sr.UnknownValueError:
        talk("Sorry, I was not able to hear you.")
    except Exception:
        talk("Try that again")

def run_john():
    wish_user()
    command = listen()
    print(command)
    if 'play' in command:
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
    elif command == 'quit':
        talk("Shutting it Down!")
        exit()
    else:
        talk("Sorry Can you repeat that?")

if __name__ == "__main__":
    while(true):
        run_john()