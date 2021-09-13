# Importing Libraries
from email import message
from email.mime import text
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
import sys
from typing import Text
import pyttsx3
import requests
from requests.api import get
import speech_recognition as sr
import datetime
import wikipedia 
import webbrowser 
import os
import smtplib
import cv2
from wikipedia.wikipedia import random
import random 
import pywhatkit as kit
import time
import pyjokescli
import pyautogui
import instaloader 
import PyPDF2
from email.mime.multipart import MIMEMultipart
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QTimer, QTime, QDate, Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from form import Ui_Widget
from email import encoders
import operator




 




#Creating Engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0]].id)
engine.setProperty('voice', voices[0].id)

# Speech to Text
def speak(audio):
    engine.say(audio) 
    engine.runAndWait()

#To Wish
def WishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!!")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!!")
    else:
        speak("Good Evening!!")  
    
    speak("I am Jarvis Sir. Please tell me how I may help you.")

#Sending Email
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('akashsharma1098256@gmail.com','Shyam@7114')
    server.sendmail('kumaraakash393@gmail.com', to, content)
    server.close()

#For News Updates
def news():
    main_url = 'http://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=d96c8e214a9441a0987d63d008ede18d'

    main_page = requests.get(main_url).json()
    #print(main_page)
    articles = main_page["articles"]
    # print(articles)
    head = []
    day = ["first","second","third","fourth","fifth","sixth","seventh","eighth","ninth","tenth"]
    for ar in articles:
        head.append(ar["title"])
    for i in range(len(day)):
        # print(f"today's {day[i]} news is: ", head[i])
        speak(f"today's {day[i]} news is: {head[i]}")

# For Reading PDF
def pdf_reader():
    book = open('book.pdf','rb')
    pdfreader = PyPDF2.PdfFileReader(book)
    pages = pdfreader.numPages
    speak(f"total numbers of pages in this book  {pages} ")
    speak("sir, please enter the page number i have to read")
    pg = int(input("Please enter the page number: "))
    page = pdfreader.getPage(pg)
    text = page.extractText()
    speak(text)

class MainThread(QThread):
    def __init__(self):
        super(MainThread,self).__init__()

    def run(self):
        self.TaskExecution()

    #Taking Input from User
    def takeCommand(self):
        # It takes input from Microphone and returns output as String.
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening....")
            r.pause_threshold = 1
            audio = r.listen(source)
        
        try:
            print("Recognizing....")
            query = r.recognize_google(audio, language='en-in')
            print(f"User said: {query}\n")
        
        except Exception as e:
            print(e)

            print("Say that again please...")
            return "None"
        return query

    # For Task Executing
    def TaskExecution(self):
        speak("Aakash Sharma")
        WishMe()
        while True:
        #if 1:
            self.query = self.takeCommand().lower()
            # Logic for executing tasks based on query
        # Opening Applications
            if 'wikipedia' in self.query:
                speak("Searching Wikipedia")
                self.query = self.query.replace("wikipedia","")
                results = wikipedia.summary(self.query, sentences=2)
                speak("According to Wikipedia")
                print(results)
                speak(results)
        # Opening Youtube        
            elif 'open youtube' in self.query:
                webbrowser.open("www.youtube.com")
        # Searching on  Google
            elif 'open google' in self.query:
                speak("sir, what should i search on google")
                cm = self.takeCommand.lower()
                webbrowser.open(f"{cm}")
        # Opening Stackoverflow
            elif 'open stackoverflow' in self.query:
                webbrowser.open("www.stackoverflow.com")
        # Opening Github
            elif 'open github' in self.query:
                webbrowser.open("www.github.com")
        # Opening LinkedIn
            elif 'open linkedin' in self.query:
                webbrowser.open("www.linkedin.com")
        # Playing Music
            elif 'play music' in self.query:
                music_dir = 'D:\\Songs'
                songs = os.listdir(music_dir)
                print(songs)
                #rd = random.choice(songs)
                for song in songs:
                    if song.endswith('.mp3'):
                        os.startfile(os.path.join(music_dir, song))
        # Knowing Time
            elif 'the time' in self.query:
                strTime = datetime.datetime.now().startime("%H:%M:%S")
                speak(f"Sir, the time is {strTime}")
        # Opening Notepad        
            elif 'open notepad' in self.query:
                notepadPath = "C:\\Windows\\system32\\notepad.exe"
                os.startfile(notepadPath)
        # Opening Visual Studio Code
            elif 'open code' in self.query:
                codePath = "C:\\Users\\AakashSharma\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
                os.startfile(codePath)
        #Sending Emails
            elif 'send email' in self.query:
                try:
                    speak("What should I say?")
                    content = self.takeCommand()
                    to = 'kumaraakash393@gmail.com'
                    sendEmail(to, content)
                    speak("Email has been sent!")
                except Exception as e:
                    print(e)
                    speak("Sorry Sir, I am not able to send email")
        # Opening Camera
            elif 'open camera' in self.query:
                cap = cv2.VideoCapture(0)
                while True:
                    ret, img = cap.read()
                    cv2.imshow('webcam', img)
                    k = cv2.waitKey(50)
                    if k==27:
                        break
                    cap.release()
                    cv2.destroyAllWindows()
        #Knowing IP Address
            elif 'ip address' in self.query:
                ip = get('https://api.ipify.org').text
                speak(f"Your IP Address is {ip}")
        # Sending Message WhatsApp
            elif 'send message' in self.query:
                kit.sendwhatmsg("+918307031174", "This is Jarvis!!",2,24)
                #Here 2 and 24 are the timings in 24 Hours Format.
        #Playing Specific Songs on Youtube
            elif 'play song on youtube' in self.query:
                kit.playonyt("see you again")
                #Here See you again is the name of the song which we want to play.
        #Closing Jarvis
            elif 'no thanks' in self.query:
                speak("thanks for using me sir, have a good day")
                sys.exit()
        #Closing  Opened Applications
            elif 'close notepad' in self.query:
                speak("okay sir, closing notepad")
                os.system("taskkill /f /im notepad.exe")
            elif 'close code' in self.query:
                speak("okay sir, closing Visual Studio Code")
                os.system("taskkill /f /im Code.exe")
            elif 'close browser' in self.query:
                speak("okay sir, closing notepad")
                os.system("taskkill /f /im firefox.exe")
        #To set an Alarm
            elif 'set alarm' in self.query:
                nn = int(datetime.datetime.now().hour)
                if nn == 22:
                    music_dir = 'D:\\Songs'
                    songs = os.listdir(music_dir)
                    os.startfile(os.path.join(music_dir, songs[0]))
        #To find a joke
            elif 'tell me a joke' in self.query:
                joke = pyjokescli.get_joke()
                speak(joke)
        #To ShutDown the System
            elif 'shutdown' in self.query:
                os.system("shutdown /s /t 5")
        #To Restart the System
            elif 'restart' in self.query:
                os.system("shutdown /r /t 5")
        #To Sleep the System
            elif 'sleep' in self.query:
                os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
        #To Switch the Windows
            elif 'switch' in self.query:
                pyautogui.keyDown("alt")
                pyautogui.press("tab")
                time.sleep(1)
                pyautogui.keyUp("alt")
        #Telling News
            elif 'tell me news' in self.query:
                speak("please wait sir, fetching the latest news")
                news()

        #To check a Instagram Profile Picture
            elif 'instagram profile' in self.query or 'profile on instagram' in self.query:
                speak("sir please enter the user name")
                name = input("Enter UserName here: ")
                webbrowser.open(f"www.instagram.com/{name}")
                speak(f"Sir, here is the profile of the user {name}")
                time.sleep(5)
                speak("sir would you like to download profile picture of this account.")
                condition = self.takeCommand().lower()
                if 'yes' in condition:
                    mod = instaloader.instaloader()
                    mod.download_profile(name, profile_pic_only=True)
                    speak("i am done sir, profile picture is saved in our main folder.now i am ready for the next command.")
                else:
                    pass

        # To take Screenshots
            elif 'screenshot' in self.query:
                speak("sir, please tell me the name of this screenshot file")
                name = self.takeCommand.lower()
                speak("sir, please hold the screen, i am taking screenshot")
                time.sleep(3)
                img = pyautogui.screenshot()
                img.save(f"{name}.png")
                speak("i am done sir, the screenshot is saved in our main folder. now i am ready for the next command.")
        # To Read PDF File
            elif 'read pdf' in self.query:
                pdf_reader()

        #For Hiding Files or Folder
            elif 'hide all files' in self.query or 'hide this folder'  in self.query or 'visible for everyone' in self.query:
                speak('sir please tell me you want to hide this folder or make it visible for everyone')
                condition = self.takeCommand.lower()
                if 'hide' in condition:
                    os.system("attrib +h /s /d") #os module
                    speak("sir, all the files in this folder are now hidden.")
                elif 'visible' in condition:
                    os.system("attrib -h /s /d")
                    speak('sir, all the files in this folder are visible to everyone.')
                elif 'leave it' in condition or 'leave for now' in condition:
                    speak('ok sir')

        # Doing Mathematical Calculations
            elif "do some calculations" in self.query or "can you calculate" in self.query:
                r = sr.Recognizer()
                with sr.Microphone() as source:
                    speak("what do you want to calculate sir, for example: 2 plus 2")
                    print("listening....")
                    r.adjust_for_ambient_noise(source)
                    audio = r.listen(source)
                my_string = r.recognize_google(audio)
                print(my_string)
                def get_operator_fn(op):
                    return {
                        '+' : operator.add, #plus
                        '-' : operator.sub, #minus
                        'x' : operator.mul, #multiplied by
                        'divided' : operator.__truediv__, #divided
                    }[op]
                def eval_binary_expr(op1, oper, op2): # 5 plus 8
                    op1,op2 = int(op1), int(op2)
                    return get_operator_fn(oper)(op1, op2)
                speak("your result is")
                speak(eval_binary_expr(*(my_string.split())))



        #Sending Emails by voice
            elif 'email to akash' in self.query:
                
                speak('sir what should i say')
                self.query = self.takeCommand().lower()
                #Adding Attachments
                if "send a file" in self.query:
                    email = 'akashsharma1098256@gmail.com' #My Email
                    password = 'Shyam@7114' #My Password
                    send_to_email= 'kumaraakash393@gmail.com' #Email of whom you are sending the message to
                    speak('okay sir, what is the subject for this email')
                    self.query = self.takeCommand.lower()
                    subject = self.query # The Subject in the email
                    speak('and sir, what is the message for this email')
                    self.query = self.takeCommand.lower()
                    message = self.query # The Message in the email
                    speak("sir please enter the correct path of the file into the shell")
                    file_location = input("please enter the path here: ")   #The File Attachment Address in the mail

                    speak("please wait, i am sending email now")

                    msg = MIMEMultipart()
                    msg['From'] = email
                    msg['To'] = send_to_email
                    msg['Subject'] = subject

                    msg.attach(MIMEText(message, 'plain'))

                    #Setup the attachment 
                    filename = os.path.basename(file_location)
                    attachment = open(file_location, "rb")
                    part = MIMEBase('application', 'octet-stream')
                    part.set_payload(attachment.read())
                    encoders.encode_base64(part)
                    part.add_header('Content_Disposition', 'attachment; filename= %s' % filename)

                    #Attach the attachment to the MIMEMultipart object
                    msg.attach(part)

                    server = smtplib.SMTP('smtp.gmail.com', 587)
                    server.starttls()
                    server.login(email,password)
                    text = msg.as_string()
                    server.sendmail(email, send_to_email, text)
                    server.quit()
                    speak('email has been sent.')

                else:
                    email = 'akashsharma1098256@gmail.com' #My Email
                    password = 'Shyam@7114' #My password
                    send_to_email = 'kumaraakash393@gmail.com' #Email of whom you are sending the message
                    message = self.query #The Message in email

                    server = smtplib.SMTP('smtp.gmail.com' , 587)
                    server.starttls() #Use TLS
                    server.login(email, password) # Login to email server
                    server.sendmail(email, send_to_email, message) #Send the email
                    server.quit() #Logout of the email server
                    speak('email has been sent.')

startExecution = MainThread()


class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Widget()
        self.ui.setupUi(self)
        self.ui.RUN_Button.clicked.connect(self.startTask)
        self.ui.Exit_Button.clicked.connect(self.close)

    def startTask(self):
        self.ui.movie = QtGui.QMovie("Data/main_gif.gif")
        self.ui.Main_GIF.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("Data/init_system.gif")
        self.ui.Init_System.setMovie(self.ui.movie)
        self.ui.movie.start()
        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(1000)
        startExecution.start()

    def showTime(self):
        current_time = QTime.currentTime()
        current_date = QDate.currentDate()
        label_time = current_time.toString('hh:mm:ss')
        label_date = current_date.toString(Qt.ISODate)
        self.ui.Date.setText(label_date)
        self.ui.Time.setText(label_time)




app = QApplication(sys.argv)
jarvis = Main()
jarvis.show()
exit(app.exec_())




        








