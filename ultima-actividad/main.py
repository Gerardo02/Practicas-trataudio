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
    if 'what is your name' in voice_data:
        print('Mi nombre es alexis')
    if 'time' in voice_data:
        print(ctime())
    if 'search' in voice_data:
        buscar = record_audio('Que necesitas buscar?')
        url = 'https://google.com/search?q=' + buscar
        webbrowser.get().open(url)
        print('Es lo que encontre para: ' + buscar)
    if 'place' in voice_data:
        lugar = record_audio('Que lugar?')
        url = 'https://google.nl/maps/place/' + lugar + '/&amp;'
        webbrowser.get().open(url)
        print ('Es lo que encontre para ' + lugar)

time.sleep(1)
print('Como te puedo ayudar?')
while 1:
    voice_data = record_audio()
    respond(voice_data)
    
