import smtplib
import speech_recognition as ar
import pyttsx3

listeer = sr.Recognizer()
engine = pyttsx3.init()


def talk(text):
    engine.say(text)
    engine.runAndWait()

def get_info():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            info = listener.recognize_google(voice)
            print(info)
            return info.lower()
    except :  
        pass       

def send_email():
    server = smtplib.SMTP('smtp.gmail.com',587)

    server.starttls('fresh.grandma21@gmail.com','GrandmaDatingSantaOnChristmas')

    server.sendmail('fresh.grandma21@gmail.com',
    'medkh6699@gmail.com',
    'hi dude'
    )

def get_email_info():
    talk('To whom you want to send email')

get_email_info()    
