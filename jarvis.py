import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import smtplib
import os
import random

"""
This program is a self managing personal assistance bot for a windows PC, that operates on voice commands and responds verbally.
This program refers to itself as Jarvis and automate the following tasks:
1. It can open Google, WhatsApp and StackOverflow websites in the browser.
2. It can directly search and read from the Wikipedia page for the subject asked.
3. It can play any random music to surprise you and can also play the entire playlist.
4. It can tell/show current Date and Time.
5. It can Shutdown or Restart the Computer on itself.
6. It can autosend a dictated email to any email-id if you have a gmail id.
7. It can also open VS Code on it's own when commanded accordingly.
"""
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(audio):
    """
    This function provides the bot with the ability of speech or makes bot speak.
    Variables:
        1. engine - It is an pyttsx3 object that allows the features of narrating a string
        2. audio - The string that the Jarvis bot narrates during the execution of various tasks.
    """
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    """
    This function allows us recognize that bot has began functioning as via this function it greets us.
    Variables:
        1. hour - It holds the value of current time in hours.
    """
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 6:
        speak("It's sleep time sir, please go to bed")
    elif hour >= 6 and hour < 12:
        speak("Good morning Sir ")
    elif hour >= 12 and hour < 16:
        speak("Good Afternoon Sir ")
    elif hour >=16 and hour < 20:
        speak("Good Evening Sir ")
    else:
        speak("Good Night Sir ")

    speak("I am Jarvis. How may I help you?")

def takeCommand():
    # This function takes microphone input from user and returns a string.
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.... ")
        r.pause_threshold = 1
        r.energy_threshold = 200
        audio = r.listen(source)
    
    try:
        print("Recognizing.... ")
        query = r.recognize_google(audio, language="en-in")
        print("User command: ", query)
    except Exception:
        # print(e)
        print("Pardon me Sir, please repeat")
        return "None"
    return query

def sentMail(to, content):
    """
    This function provides our personal assistance bot with the mail sending details and facility.
    """
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login("abc@gmail.com", "#####")
    server.sendmail("abc@gmail.com", to, content)
    server.close()

def execution():
    """
    This function provides operates the automation of Jarvis and is used to perform all the above mentioned jobs.
    Variables:
        query(String) - It holds the command given by the user.
    """
    while True:
        query = takeCommand().lower()

        # Logic for executing the tasks based on query
        if "wikipedia" in query:
            speak("searching Wikipedia.... ")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=5)
            speak("According to Wikipedia.... ")
            print(results)
            speak(results)
            
        elif "open youtube" in query:
            webbrowser.open("https://www.youtube.com/")

        elif "open google" in query:
            webbrowser.open("https://www.google.com/")

        elif "open stack overflow" in query:
            webbrowser.open("https://stackoverflow.com/")

        elif "open whatsapp" in query:
            webbrowser.open("https://web.whatsapp.com/")

        elif "play music" or "play random track" or "play random song" in query:
            music_dir = "D:\\Sarthak\\Music"
            songs = os.listdir(music_dir)
            num = random.randint(0,len(songs)-1)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[num]))

        elif "time" in query:
            ctime = datetime.datetime.now().strftime(" %H : %M : %S ")
            print(ctime)
            speak(f"Sir, the time is {ctime}")

        elif "date" in query:
            cdate = datetime.date.today()
            print(str(cdate))
            speak(f"Sir, Today is {cdate}")
        
        elif "shutdown" in query:
            check = input("Want to shutdown your computer ? (y/n): ");
            if check == 'y' or check == "Y":
                os.system("shutdown /s /t 1");

        elif "restart" in query:
            check = input("Want to restart your computer ? (y/n): ");
            if check == 'y' or check == "Y":
                os.system("shutdown /r /t 1");

        elif "open code" in query:
            codePath = "D:\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)


        elif "mail" or "email" or "e-mail" in query:
            try:
                print("Sir, what should I send?")
                speak("Sir, what should I send?")
                content = takeCommand()
                print("Sir, the email Id please.... ")
                speak("Sir, the emial Id please")
                to = takeCommand()
                sentMail(to, content)
                print("Email has been sent")
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Pardon me Sir, I am unable to send this email.")
                continue

if __name__ == "__main__":
    wishMe()
    execution()



