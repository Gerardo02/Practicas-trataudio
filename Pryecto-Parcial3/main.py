import speech_recognition as sr
import time
import webbrowser
from time import ctime

r = sr.Recognizer()

def record_audio(ask = False):
    with sr.Microphone() as source:
        if ask:
            print(ask)
        audio = r.listen(source)
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)

        except sr.UnknownValueError:
            print('lo siento, no te entendi')
        except sr.RequestError:
            print('Lo siento, error de conexion')
        return voice_data

def respond(voice_data):
    traduccion= 'Traduccion: '
    if 'what is your name' in voice_data:
        print(traduccion + 'Cual es tu nombre?')
    if 'what time is it' in voice_data:
        print(traduccion + 'Que hora es?')
    if 'Near Food' in voice_data:
        print(traduccion + 'Restaurantes cerca?')
    if 'Near hospital' in voice_data:
        print(traduccion + 'Hospital cerca?')
    

time.sleep(1)
print('Di lo que quieras preguntar.')
while 1:
    voice_data = record_audio()
    respond(voice_data)
    
