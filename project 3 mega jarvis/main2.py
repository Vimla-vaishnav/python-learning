import speech_recognition as sr
import webbrowser
import pyttsx3

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def processCommand(command):
    if "open google" in command.lower():
        webbrowser.open("http://google.com")
    elif "open facebook" in command.lower():
        webbrowser.open("http://facebook.com")
    elif "open youtube" in command.lower():
        webbrowser.open("http://youtube.com")
    elif "open linkedin" in command.lower():
        webbrowser.open("http://linkedin.com")
    else:
        speak("Sorry, I didn't understand the command.")

if __name__ == "__main__":
    speak("Initializing Jarvis...")
    while True:
        r = sr.Recognizer()
        try:
            with sr.Microphone() as source:
                print("Listening for wake word...")
                audio = r.listen(source,phrase_time_limit=10)
                r.adjust_for_ambient_noise(source, duration=1)

                word = r.recognize_google(audio)
                print("Heard:", word)

                if "jarvis" in word.lower():
                    speak("Yes, how can I help?")
                    with sr.Microphone() as source:
                        print("Jarvis Active...")
                        audio = r.listen(source, timeout=5, phrase_time_limit=10)
                        command = r.recognize_google(audio)
                        print("Command received:", command)
                        processCommand(command)

        except Exception as e:
            print("Error:", e)
