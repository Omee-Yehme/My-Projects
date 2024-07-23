import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib

# Initialize the speech engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # Use the second voice

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning Everyone!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon Everyone!")
    else:
        speak("Good Evening Everyone!")

    speak("I am Zaenith, developed by team Somy. Please tell me how may I help you")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print(e)
        print("Please, say that again!")
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('your-email@gmail.com', 'your-password')  # Replace with your email and password
    server.sendmail('your-email@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        if "wikipedia" in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("Boss, according to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("https://youtube.com")

        elif 'open google' in query:
            webbrowser.open("https://google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("https://stackoverflow.com")

        elif 'play music' in query:
            music_dir = "C:\\Users\\91880\\Music"  # Update with your music directory
            songs = os.listdir(music_dir)
            if songs:
                os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strtime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Boss, the time is {strtime}")
            print(strtime)

        elif 'open code' in query:
            codePath = "C:\\Users\\91880\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'send email to yashodeep' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "yashmeshram689@gmail.com"
                sendEmail(to, content)
                speak('Boss, the email has been sent')
            except Exception as e:
                print(e)
                speak("Sorry Boss, I am not able to send the email at this moment")

        elif 'search' in query:
            webbrowser.open("https://openai.com")
            speak('I did not have more inputs from my team so visit this website!')

        elif 'quit' in query:
            exit()
