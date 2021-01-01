import smtplib
import speech_recognition as ar
import pyttsx3
from email.message import EmailMessage

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

def send_email(reciver, subject, meesage):
    server = smtplib.SMTP('smtp.gmail.com',587)

    server.starttls()
    server.login('fresh.grandma21@gmail.com','GrandmaDatingSantaOnChristmas')
    email = EmailMessage()
    email['From'] = 'fresh.grandma21@gmail.com'
    email['To'] = reciver
    email['Subject'] = subject
    email.set_content()
    server.send_message(email)

def email_list = {
    'dude': 'jhomnv@gmail.com',
    'programming': 'supportflo@gmail.com',
    'bts': 'diagrammouning@gmail.com',
    'pink': 'jenniferloper@gmail.com',
    'liza': 'lizapooming@gmail.com'
}


def get_email_info():
    talk('To whom you want to send email')
    name = get_info()
    reciver = email_list[name]
    print(reciver)
    talk('what is the subject of your email')
    subject = get_info()
    talk('Tell me the text in your email ')
    message = get_info()

    send_email(reciver, subject , message)
    talk('hey lazy ass , your email is sent')
    talk('You want to send more email ')
    send_more= get_info()
    if 'yes' in send_more:
        get_email_info()
    

get_email_info()    
