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
    # wish_user()
    print("Listening...")
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
    elif command == 'quit' or 'shut up' in command or command == 'close':
        talk("Shutting it Down!")
        exit()
    else:
        talk("Sorry Can you repeat that?")
    

if __name__ == "__main__":
    wish_user()
    while(True):
        run_john()