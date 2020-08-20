import pyttsx3
import os

pyttsx3.speak("Welcome to my Tools")

pyttsx3.speak("Here are all the application that you run")
print("********************************************************")
print("                       Chrome                            ")
print("                      YouTube                            ")
print("                         Paint                           ")
print("                      AnyDesk                            ")
print("                      Telegram                           ")
print("                      WordPad                            ")
print("                      Notepad++                          ")
print("                 Windows Media Player                    ")
print("                      MS Word                            ")
print("                    MS PowerPoint                        ")
print("                      MS Excel                           ")
print("********************************************************")

pyttsx3.speak("What application you want to run")

while True:
    print("Application you want to run",end= "")
    p = input()

    if ("not " in p) or ("donot" in p) or ("don't" in p):
        pyttsx3.speak("Can't open this Application. Try some thing another")
        print("can't open ",p)
    elif (("run" in p) or ("execute" in p)) and ("chrome" in p):
        pyttsx3.speak("Opening Chrome")
        os.system("chrome")
    elif (("run" in p) or ("execute" in p)) and ("youtube" in p):
        pyttsx3.speak("Opening youtube")
        os.system("chrome youtube.com")
    elif (("run" in p) or ("execute" in p)) and ("paint" in p):
        pyttsx3.speak("Opening Paint")
        os.system("mspaint")
    elif (("run" in p) or ("execute" in p)) and ("anydesk" in p):
        pyttsx3.speak("Opening AnyDesk")
        os.system("AnyDesk")
    elif (("run" in p) or ("execute" in p)) and ("telegram" in p):
        pyttsx3.speak("Opening Telegram")
        os.system("telegram")
    elif (("run" in p) or ("execute" in p)) and ("wordpad" in p):
        pyttsx3.speak("Opening word pad")
        os.system("wordpad")
    elif (("run" in p) or ("execute" in p)) and ("notepad++" in p):
        pyttsx3.speak("Opening notepad ++")
        os.system("notepad++")
    elif (("run" in p) or ("execute" in p)) and (("notepad" in p) or ("editor" in p)):
        pyttsx3.speak("Opening Notepad")
        os.system("notepad")
    elif (("run" in p) or ("execute" in p)) and ("player" in p) and ("media" in p):
        pyttsx3.speak("Opening Windows Media Player")
        os.system("wmplayer")
    elif (("run" in p) or ("execute" in p)) and ("microsoft" in p) and ("office" in p) and ("word" in p):
        pyttsx3.speak("Opening MS Word")
        os.system("winword")
    elif (("run" in p) or ("execute" in p)) and ("microsoft" in p) and ("office" in p) and ("powerpoint" in p):
        pyttsx3.speak("Opening MS Powerpoint")
        os.system("powerpnt")
    elif (("run" in p) or ("execute" in p)) and ("microsoft" in p) and ("office" in p) and ("excel" in p):
        pyttsx3.speak("Opening Excel")
        os.system("excel")
    elif ("exit" in p) or ("quit" in p):
        pyttsx3.speak("Exiting from the Software")
        break
    else:
        print("don't support...Please install that Application")

