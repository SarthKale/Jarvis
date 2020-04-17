import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import smtplib
import os
import random

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
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

# def dir_parser():
#     counter = True
#     location = ""
#     print("Sir, C Drive or D Drive?")
#     speak("Sir, C Drive or D Drive?")
#     name = takeCommand().lower()
#     if "d" in name: location.__add__("D:\\")
#     elif "c" in name: location.__add__("C:\\Users\\SarthK")
#     while counter:
#         print(os.listdir(location))
#         print("Sir, which directory next?")
#         speak("Sir, which directory next?")
#         name = takeCommand()
#         print(name)
#         if "open" in name: 
#             os.chdir(location)
#         else:
#             location = "\\".join([name])
#     return location
                    
def takeCommand():
    # It takes microphone input from user and returns string.
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
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login("sarthak.kale12@gmail.com", "shajapur38312")
    server.sendmail("sarthak.kale12@gmail.com", to, content)
    server.close()

def execution():
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
            webbrowser.open("youtube.com")

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

        elif "music playlist" in query:
            music_dir = "D:\\Sarthak\\Music"
            playlist = os.listdir(music_dir)
            print(playlist)
            for track in playlist:
                print(track)
                os.startfile(os.path.join(music_dir, track))

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

        # elif "open folder" or "open directory" in query:
        #     loc = dir_parser()
        #     print(loc)

        # elif "document" or "ms word" or "word file" in query:
        #     print("Sir, do you want to read the file or write a file or append in a file?")
        #     speak("Sir, do you want to read the file or write a file or append in a file?")
        #     print("set mode")
        #     mode = takeCommand().lower()
        #     print(mode)

        #     # paragraph(array), run(same formatted text)
        #     doc_dir = "C:\\Users\\SarthK\\Desktop"
        #     os.chdir(doc_dir)
        #     if "read" or "r" in mode:
        #         print("read mode selected")
        #         print("Sir, what is the name of the document?")
        #         speak("Sir, what is the name of the document?")
        #         name = takeCommand().lower()
        #         print(name)
        #         f = open("a.docx")
        #         content = f.read()
        #         print(content)
        #         speak(content)
        #         f.close()

        #     elif "write" or "w" in mode:
        #         print("write mode selected")
        #         counter = True
        #         print("What should I name the file?")
        #         speak("What should I name the file?")
        #         name = takeCommand().lower()
        #         print(name)
        #         f = open(".".join([name, "docx"]), "w")
        #         while counter:
        #             print("What should I add? Or say 'E' to save and exit.")
        #             speak("What should I add? Or say 'E' to save and exit.")
        #             phrase = takeCommand().lower()
        #             if phrase == "e": 
        #                 counter = False
        #             else:
        #                 print(phrase)
        #                 phrase.replace("new line", "\n")
        #                 f.write(phrase)
        #         f.close()

        #     elif "append" or "add" or "a" in mode:
        #         print("write mode selected")
        #         counter = True
        #         print("Sir, what is the name of the document?")
        #         speak("Sir, what is the name of the document?")
        #         name = takeCommand().lower()
        #         print(name)
        #         f = open(".".join([name, "docx"]), "a")
        #         content = f.read()
        #         while counter:
        #             print("What should I add? Or say 'E' to save and exit.")
        #             speak("What should I add? Or say 'E' to save and exit.")
        #             phrase = takeCommand().lower()
        #             if phrase == "e": 
        #                 counter = False
        #             else:
        #                 phrase.replace("new line", "\n")
        #                 print(phrase)
        #                 f.write(phrase)
        #         f.close()

        elif "mail" or "email" in query:
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



