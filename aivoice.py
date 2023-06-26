import pyttsx3
import speech_recognition as sr
import os

engine = pyttsx3.init()


def arjun_speak(text):
    engine.setProperty('rate', 160)
    engine.setProperty('volume', 1.0)
    print(text)
    engine.say(text)
    engine.runAndWait()


def arjun_listen():
    re = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            os.system('cls')
            print("Listening...")
            re.adjust_for_ambient_noise(source)
            audio = re.listen(source, timeout=2, phrase_time_limit=5)
            os.system('cls')
            print("Recognizing...")
            query = re.recognize_google(audio)
            print(f"You: {query}")
            query = query.lower()
            return query

    except Exception:
        return ""
        pass
