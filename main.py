from aivoice import *
import os
import commands
import datetime


def run():
    commands.greatings()
    while True:
        os.system("cls")
        query = arjun_listen()

        if "wikipedia" in query:
            arjun_speak("Searching on wikipedia")
            commands.ar_wiki(query)

        elif "google" in query:
            commands.goosearch(query)

        elif "youtube" in query:
            commands.youtube(query)

        elif "fine" in query:
            arjun_speak("Good to hear sir!")

        elif "goodbye" in query or "good by" in query:
            hour = int(datetime.datetime.now().hour)
            if hour >= 20:
                arjun_speak("As you Wish Sir! but May I know your next plan :")
                tik = arjun_listen()
                if "sleep" in tik:
                    arjun_speak("OK OK")
                    arjun_speak("Well Good Night and Dream for your dream girl miss Khushi")
                    tik = arjun_listen()
                    if "shut up" in tik or "shutup" in tik:
                        arjun_speak("Sorry sir! but i know you feel for her")
                        tik = arjun_listen()
                        if "hmm hmm" in tik or "that's true" in tik or "ok" in tik:
                            arjun_speak("well i know, sleep well sir bye bye!")
                else:
                    arjun_speak("Well Wish You Good Luck for Your Next Work")
                    tik = arjun_listen()
                    if "thanks" in tik or "thank you" in tik:
                        arjun_speak("Your Welcome sir , see you bye bye")
            else:
                arjun_speak("As you Wish Sir! , well see you  Again bye bye")
                os.system(exit(1))


if __name__ == "__main__":
    run()
