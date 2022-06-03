import pyttsx3
import speech_recognition as sr
import wikipedia
import webbrowser

#import os


engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")

engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...... :)")
        r.pause_threshold = 1
        audio = r.listen(source)
        try:
            print("Recognizing.....")
            query = r.recognize_google(audio, language='en-in')
            print("user said:" + query + "\n")
        except Exception as e:
            print(e)
            speak("I didn't get you")
            return "0"
        return query


if __name__ == '__main__':
    speak("Uran assist activated")
    speak("Hi boss how can i help you")
    while True:
        query = take_command().lower()
        if "wikipedia" in query:
            speak("searching wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            speak(results)

        elif "are you" in query:
            speak("i am uran developed by Sahith")

        elif "open browser" in query:
            speak("opening Brave")
            webbrowser.open(r"C:\Users\Public\Desktop\Brave.lnk")

        elif "open youtube" in query:
            speak("opening youtube")
            webbrowser.open("youtube.com")
        elif "open photos" in query:
            speak("opening photos")
            webbrowser.open(r"C:\Users\sahit\OneDrive\Pictures")
        elif "music" in query:
            speak("it's on me")
            webbrowser.open("https://youtu.be/cml8Qo74zNQ")
        elif "sleep" in query:
            speak("see you again")
            exit(0)
