import pyttsx3 as p
import pyaudio
import datetime
from selenium_web import *
import speech_recognition as sr
from  audio_example import  *
from jokes import *
import randfacts



engine = p.init()
rate = engine.getProperty('rate')
engine.setProperty('rate',150)
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()


r = sr.Recognizer()

hours = int(datetime.datetime.now().hour)

if hours>8 and hours<12:
    print("good morning")
    speak("Good Morning Sir")
elif hours>=12 and hours<15:
    print("good afternoon")
    speak("Good Afternoon Sir")
else:
    print("good evening")
    speak("Good evening sir")

speak("i am you assistant how are you sir")

#catch audio through microphone store in audio variable
with sr.Microphone() as source:
    r.energy_threshold=100000
    r.adjust_for_ambient_noise(source, 1.2)
    print("listening")
    audio = r.listen(source)
    text = r.recognize_google(audio)
    print(text)

if 'what' and 'about' and 'you' in text:
    speak("I am also having a good day sir")
speak("what can i do for you")


# speech to text
with sr.Microphone() as source:
    r.energy_threshold=10000
    r.adjust_for_ambient_noise(source, 1.2)
    print("listening....")
    audio = r.listen(source)
    text3 = r.recognize_google(audio)

if "information"  in text3:
    speak("you need information related to which topic")
    with sr.Microphone() as source:
        r.energy_threshold = 10000000
        r.adjust_for_ambient_noise(source, 1.2)
        print("listening")
        audio = r.listen(source)
        text3 = r.recognize_google(audio)
    speak(f"searching {text3} in wikipedia")
    assist = info()
    assist.get_info(text3)


elif "play" and "video" in text3:
    speak("you want me to play which video")
    with sr.Microphone() as source:
        r.energy_threshold = 10000000
        r.adjust_for_ambient_noise(source, 1.2)
        print("listening..")
        audio = r.listen(source)
        text4 = r.recognize_google(audio)
        speak(f"Searching {text4} on youtube")
        assist = music_one()
        assist.play(text4)




elif "fact" or "facts" in text3:
    speak("sure")
    x = randfacts.get_fact()
    print(x)
    speak("did you know that" +x)



elif "joke" in text3:
    speak("Sure. here is my best on")
    speak(joke())
    speak()


elif "who" and "created" or "creater" in text3:
    speak("My creater is Omkar Kshirsagar")
    speak("I was born on 12 april 2023")




