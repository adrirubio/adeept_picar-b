
import speech_recognition as sr

recorder = sr.Recognizer()


def loop():
    while True:
        try:
            with sr.Microphone() as source:                                                                       
                print("Speak:")                                                                                   
                audio = recorder.listen(source)
                print("Recognizing:")
                text = recorder.recognize_google(audio)
                print(text)
                
        except sr.UnknownValueError:
            print("UnknownValueError")
            pass
        except sr.RequestError:
            print("RequestError")    
        

loop()