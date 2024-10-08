import speech_recognition as sr
import pyttsx3

r = sr.Recognizer()

def SpeakText(command):
    
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()

while True:    
    try:
       
        with sr.Microphone() as source2:
            
            r.adjust_for_ambient_noise(source2, duration=0.2)
            
           
            audio2 = r.listen(source2)
            
            
            MyText = r.recognize_google(audio2)
            MyText = MyText.lower()

            print("Did you say:", MyText)
            SpeakText(MyText)
            
    except sr.RequestError as e:
        print(f"Could not request results; {e}")
        
    except sr.UnknownValueError:
        print("Unknown error occurred")