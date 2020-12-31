import smtplib
import speech_recognition as ar

listeer = sr.Recognizer()

try:
    with sr.Microphone() as source:
        print('listening...')
        voice = listener.listen(source)
        info = listener.recognize_google(voice)
        print(info)
except :  
    pass       

def send_email():
    server = smtplib.SMTP('smtp.gmail.com',587)

    server.starttls('fresh.grandma21@gmail.com','GrandmaDatingSantaOnChristmas')

    server.sendmail('fresh.grandma21@gmail.com',
    'medkh6699@gmail.com',
    'hi dude'
    )