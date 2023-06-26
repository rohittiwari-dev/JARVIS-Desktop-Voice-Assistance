from datetime import datetime
from aivoice import *
import datetime
import wikipedia
import pywhatkit
import webbrowser
import os


def greatings():
    print("Initializing.....")
    os.system("cls")
    arjun_speak("Initialized Successfuly...")
    os.system("cls")
    hour = int(datetime.datetime.now().hour)
    greet = ""
    text = ""
    if 0 <= hour < 12:
        greet = "Good morning"
        text = "Hi Sir I am Arjun, Semi AI Assistance Created By Mister Rohit Tiwari"
    elif 12 <= hour < 17:
        greet = "Good Afternoon"
        text = "Hi Sir I am Arjun, How Was Your Morning"
    elif hour >= 17:
        greet = "Good evening"
        text = "Hi Sir I am Arjun, Hope Your Day Was Good"
    arjun_speak(greet)
    arjun_speak(text)
    os.system("cls")


def ar_wiki(text):
    query = text
    query = query.replace("wikipedia", "")
    query = query.replace("arjun", "")
    result = wikipedia.summary(query, sentences=2)
    arjun_speak("According to wikipedia")
    arjun_speak(result)


def goosearch(query):
    if query == "google":
        query = query.replace("google", "")
    if "google" in query:
        query = query.replace(" google ", " ")
        query = query.replace("google ", " ")
        query = query.replace(" google", " ")
    if "search" in query:
        query = query.replace(" search ", " ")
        query = query.replace(" search", " ")
        query = query.replace("search ", " ")
    if "on" in query:
        query = query.replace(" on ", " ")
    " "
    if query == "":
        arjun_speak("Please say \'Yes\' if you want to Open Google and \'No\' if want to search Anything")
        cmd = arjun_listen()
        if cmd == "yes":
            arjun_speak("Opening Google Sir")
            webbrowser.open("https://www.google.com")
        else:
            arjun_speak("What to search sir?")
            while True:
                search = arjun_listen()
                if search is None or search == "":
                    continue
                else:
                    arjun_speak(f"searching {search} on google sir")
                    pywhatkit.search(search)
                    break
    else:
        search = query
        arjun_speak(f"searching {search} on google sir")
        pywhatkit.search(search)


def youtube(query):
    if query == "youtube":
        query = query.replace("youtube", "")
    if "youtube" in query:
        query = query.replace(" youtube", " ")
        query = query.replace(" youtube ", " ")
        query = query.replace(" on ", " ")
    " "
    if query == "":
        arjun_speak("Please say \'Yes\' if you want to Open Youtube and \'No\' if want to search Anything")
        cmd = arjun_listen()
        if cmd == "yes":
            arjun_speak("Opening Youtube Sir")
            webbrowser.open("https://www.youtube.com")
        else:
            arjun_speak("Sir do you want to Search or Play Something on Youtube")
            text = arjun_listen()

            if "search" in text:
                arjun_speak("What to search sir?")
                while True:
                    search = arjun_listen()
                    if search is None or search == "":
                        continue
                    else:
                        if "search" in search:
                            search = search.replace(" search ", " ")
                            search = search.replace("search ", " ")
                        webbrowser.open(f"https://www.youtube.com/results?search_query={search}")
                        arjun_speak(f"searching {search} on youtube sir")
                        break
            else:
                arjun_speak("What to play sir?")
                while True:
                    search = arjun_listen()
                    if search is None or search == "":
                        continue
                    else:
                        if " play " in search:
                            search = search.replace("play ", " ")
                            search = search.replace(" play ", " ")
                        pywhatkit.playonyt(search)
                        arjun_speak(f"Playing {search} on youtube sir")
                        break
    elif "play" in query:
        query = query.replace("play ", " ")
        query = query.replace(" play ", " ")
        pywhatkit.playonyt(query)
        arjun_speak(f"Playing {query} on youtube sir")

    elif "search" in query:
        query = query.replace(" search ", " ")
        query = query.replace("search ", " ")
        webbrowser.open(f"https://www.youtube.com/results?search_query={query}")
        arjun_speak(f"Searching {query} on youtube sir")
