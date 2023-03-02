import pyttsx3 
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser as wb
import os
import smtplib
import pyautogui
import psutil
import pyjokes
engine = pyttsx3.init()



def speak(audio):
    
    engine.say(audio)
    engine.runAndWait()

# speak("Hello sanket, I am jarvis, your personal assistant. How can I help you?")

def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    
    speak("The current time is")
    speak(Time)

def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak("The current date is")
    speak(date)
    speak(month)
    speak(year)

def wishme():
    speak("Welcome back sir!")
    hour = datetime.datetime.now().hour
    if(hour >= 6 and hour < 12):
        speak("Good morning sir!")
    elif(hour >= 12 and hour <18):
        speak("Good afternoon sir!")
    elif(hour >= 18 and hour <24):
        speak("Good evening sir!")  
    else:
        speak("Good night sir!")
    speak("Jarvis at your service. Please tell me how can I help you?")

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('aipracticalimplementation@gmail.com', 'aipractice@2992')
    server.sendmail('aipracticalimplementation@gmail.com', to, content)
    server.close()
def screenshot():
    img = pyautogui.screenshot()
    img.save("C:\\Users\\sanke\\OneDrive\\Pictures\\Screenshots\\ss.png")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(query)
    except Exception as e:
        print(e)
        speak("Say that again please...")
        return "None"
    return query
if(__name__ == "__main__"):
    wishme()
    while True:
        query = takeCommand().lower()
        if 'time' in query:
            time()
        elif 'date' in query:
            date()
      
        
        elif 'wikipedia' in query:
            speak("Searching...")
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences=2)
            print(result)
            speak(result)
        elif 'search' in query:
            speak("What should I search?")
            chromepath = '"C:\Program Files\Google\Chrome\Application\chrome.exe" %s'
            search = takeCommand().lower()
            wb.get(chromepath).open_new_tab(search + '.com')
    
        elif 'logout' in query:
            os.system("shutdown /s")

        elif 'shutdown' in query:
            os.system("shutdown /s /t 1")

        elif 'restart' in query:
            os.system("shutdown /r /t 1")

        elif 'play song' in query:
            songs_dir = "X:\songs"
            songs = os.listdir(songs_dir)
          
            os.startfile(os.path.join(songs_dir, songs[0]))
            
        # elif 'play next song' in query:
        #     songs_dir = "X:\songs"
        #     songs = os.listdir(songs_dir)
        #     count = 0
        #     count = count + 1
        #     os.startfile(os.path.join(songs_dir, songs[count]))
        elif   'remember that' in query:
            speak("What should I remember?")
            data = takeCommand()
            speak("You said me to remember that" + data)
            remember = open('data.txt', 'w')
            remember.write(data)
            remember.close()

        elif 'do you know anything' in query:
            remember = open('data.txt', 'r')
            speak("You said me to remember that" + remember.read())

        
        elif 'send email' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                speak("Whom should I send?")
                to = input()
                # to = "vetaledurvesh06@gmail.com"
                sendEmail(to, content)
                speak("Email sent successfully!")
            except Exception as e:
                print(e)
                speak("Unable to send the email")
     
        elif'take screenshot' in query:
                screenshot()
                speak("Done!")
        elif'battery' in query:
            battery = psutil.sensors_battery()
            percent = battery.percent
            speak("Battery is at")
            speak(percent)
            speak("percent")
        elif'cpu' in query:
            usage = str(psutil.cpu_percent())
            speak("CPU is at" + usage)
            speak("percent")
        elif 'notepad' in query:
            npath = "C:\\Program Files (x86)\\Notepad++\\notepad++.exe"
            os.startfile(npath)
        elif 'brave' in query:
            npath ="C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"
            os.startfile(npath)
        elif 'file manager' in query:
            npath ="C:\\Windows\\explorer.exe"
            os.startfile(npath)
        elif 'code' in query:
            npath="C:\\Windows.old\\Users\\sanke\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(npath)
        # elif 'close code' in query:
        #     os.system("taskkill /f /im Code.exe")
        # elif 'close brave' in query:
        #     os.system("taskkill /f /im brave.exe")
        elif 'joke' in query:
            speak(pyjokes.get_joke())

        elif 'bye' in query:
            quit()
     
        


        
   


