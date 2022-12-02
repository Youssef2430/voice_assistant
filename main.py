import speech_recognition as sr
import webbrowser
import time
import playsound
import os
import random
from gtts import gTTS
from time import ctime

r = sr.Recognizer()

def record_audio(ask = False):
    with sr.Microphone() as source:
        if ask:
            speak(ask)
        audio = r.listen(source)
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)
        except sr.UnknownValueError:
            speak("Sorry, I did not get that")
        except sr.RequestError:
            speak("Sorry, my speech service is down")
        return voice_data

def speak(audio_string):
    tts = gTTS(text=audio_string, lang='en')
    r = random.randint(1, 1000000)
    audio_file = 'audio-' + str(r) + '.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)

def respond(voice_data):
    if 'what is your name' in voice_data:
        speak('My name is Alfred')
    if 'what time is it' in voice_data:
        speak(ctime())
    if 'find' in voice_data:
        search = record_audio('What do you want to search for?')
        url = 'https://google.com/search?q=' + search
        webbrowser.get().open(url)
        speak('Here is what I found for ' + search)
    if 'location' in voice_data:
        location = record_audio('What is the location?')
        url = 'https://google.nl/maps/place/' + location + '/&amp;'
        webbrowser.get().open(url)
        speak('Here is the location of ' + location)
    if 'exit' in voice_data or 'bye' in voice_data or 'thank you' in voice_data or 'thanks' in voice_data:
        speak('Always a pleasure')
        exit()
    if 'hello' in voice_data:
        speak('Hello, how can I help you?')
    if 'how are you' in voice_data:
        speak('I am fine, thank you')
    if 'what is your favorite color' in voice_data:
        speak('My favorite color is blue')
    if 'what is your favorite food' in voice_data:
        speak('My favorite food is pizza')
    if 'what is your favorite movie' in voice_data:
        speak('My favorite movie is Hunger Games')
    if 'what is your favorite game' in voice_data:
        speak('My favorite game is NBA 2K')
    if 'what is your favorite sport' in voice_data:
        speak('My favorite sport is basketball')
    if 'what is your favorite animal' in voice_data:
        speak('My favorite animal is a dog')
    

speak("How can I help you?")
while 1:
    voice_data = record_audio()
    respond(voice_data)
