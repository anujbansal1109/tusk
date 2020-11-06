import pyttsx3 
import webbrowser as wb
import datetime
import pyaudio
import speech_recognition as sr
import wikipedia
import smtplib
import os
import random
import psutil
import pyautogui
import pyjokes
engine=pyttsx3.init()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def time():
    time = datetime.datetime.now().strftime("%H:%M:%S")
    speak("Current Time Is:-")
    speak(time)

def date():
    year= int(datetime.datetime.now().year)
    month= datetime.datetime.now().strftime('%B')
    day= int(datetime.datetime.now().day)
    speak("The Current Date Is")
    speak(day)
    speak(month)
    speak(year)

def wishme():
    speak("Welcome Back Anuj Bansal!")
    #time()
    #date()
    hour = datetime.datetime.now().hour
    if hour>=6 and hour<=12:
        speak("Good Morning")
    elif hour>=12 and hour<=18:
        speak("Good Afternoon")
    elif hour>=18 and hour<=24:
        speak("Good Evening")
    else:
        speak("Good Night")

    speak("Assistant At Your Service. How Can I Help You?")

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source :
        print("Listening..")
        r.pause_threshold=1
        audio=r.listen(source)
    try:
        print("Recognizing..")
        query = r.recognize_google(audio, language='en-in')
        #print(query)
    except Exception as e :
        print(e)
        speak("Say that again please")
        return "None"
    return query

#speak("This Is Friday AI Assistant")
#wishme()
#takeCommand()
def sendemail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login("anujbansal1107@gmail.com","Bansalji7")
    server.sendmail("anujbansal1107@gmail.com",to,content)
    server.close()

def screenshot():
    img=pyautogui.screenshot()
    img.save("C://Users//acer//Desktop//AI Assitant//ss.png")

def cpu():
    usage=str(psutil.cpu_percent())
    speak("CPU is at"+usage)

    battery=psutil.sensors_battery()
    speak("battery is at")
    speak(battery.percent)
    #speak(battery.power_plugged)
    if battery.power_plugged == "True":
        print("And The Charger is connected")
        speak("And The Charger is connected")
    else:
        print("And The Charger is not  connected")
        speak("And The Charger Is not Connected")

def jokes():
    speak(pyjokes.get_joke())

if __name__ == "__main__":
    wishme()
    while True:
        query=takeCommand().lower()
        print(query)

        if "time" in query:
            time()
        elif "date" in query:
            date()
        elif (("open" in query) or ("execute" in query))  and ("rocket" in query) and ("league" in query):
            os.system("RocketLeague")
        elif (("open" in query) or ("execute" in query)) and (("notepad" in query) or ("editor" in query)):
            os.system("notepad")
        elif (("open" in query) or ("execute" in query))  and ("vlc" in query):
            os.system("vlc")
        elif (("open" in query) or ("execute" in query))  and ("media" in query) and ("player" in query):
            os.system("wmplayer")
        elif ("google" in query) and ("open" in query):
	        wb.open("https://www.google.com/webhp?hl=en&sa=X&ved=0ahUKEwiE467iq9nrAhXC8XMBHcXIC_YQPAgI")
        elif ("youtube" in query) and ("open" in query):
	        wb.open("https://www.youtube.com/")
        elif "offline" in query:
            speak("Thanks Sir For Using Me..")
            quit()
        elif ("wikipedia" in query) and ("open" in query):
	        wb.open("https://www.wikipedia.org/")
        elif "send email" in query:
            try:
                speak("What Should I Say?")
                content= takeCommand()
                to= "boatrockers400@gmail.com"
                #sendemail(to,content)
                speak(content)
            except Exception as e:
                speak(e)
                speak("Unable To Send The Mail")
    
        elif ("wikipedia" in query):
            speak("Searching.....")
            query=query.replace("wikipedia","")
            print(query)
            try:
                result = wikipedia.summary(query,sentences=2, auto_suggest=False)
            except wikipedia.exceptions.PageError:
            #if a "PageError" was raised, ignore it and continue to next link
                continue
            speak(result)
        elif "search in chrome" in query:
            speak("What Should I Search?")
            search = takeCommand().lower()
            chromepath ="C://Program Files (x86)//Google//Chrome//Application//chrome.exe %s" 
            wb.get(chromepath).open_new_tab(search+ ".com")
        elif "logout" in query:
            os.system("shutdown -l")
        elif "shutdown" in query:
            os.system("shutdown /s /t 1")
        elif "restart" in query:
            os.system("shutdown /r /t 1")
        elif "play" and  ("songs" or "song") in query:
            songs_dir = "F://MU$iC//UC DOWNLOAds"
            songs=os.listdir(songs_dir)
            os.startfile(os.path.join(songs_dir,songs[random.randint(0,68)]))
        elif "remember that" in query:
            speak("What Should I Remember?")
            data=takeCommand()
            speak("You Said Me To Remember"+ data)
            remember= open("data.txt", "w")
            remember.write(data)
            remember.close()
        elif "do you know anything" in query:
            remember=open("data.txt","r")
            speak("You said me to remember that"+remember.read())

        elif "screenshot" in query:
            screenshot()
            speak("Done!")

        elif "battery" in query:
            cpu()

        elif "joke" in query:
            jokes()