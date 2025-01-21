import speech_recognition as sr
import webbrowser
import pyttsx3

recogniser = sr.Recognizer()
engine  =pyttsx3.init()

def speak(text:str): 
    engine.say(text)
    engine.runAndWait()

if __name__ == "__main__": 
     speak("Initializing Jarvis....")
     # Listen for "Jarvis..."
     while True: 
         
       

        try: 
            with sr.Microphone() as source: 
                print("Say something...")
                audio = recogniser.listen(source, timeout=1, phrase_time_limit=1)
            command = recogniser.recognize_google(audio)
            if "jarvis" in command.lower(): 
                speak("Yes how may I help you ? ")
                with sr.Microphone() as source: 
                    print("Jarvis activated...")
                    audio = recogniser.listen(source, timeout=2, phrase_time_limit=2)
                print(command)
        except sr.UnknownValueError: 
            print("Sphinx could not understand audio")
        except sr.RequestError as e: 
            print("Sphinx error; {0}".format(e))
          
