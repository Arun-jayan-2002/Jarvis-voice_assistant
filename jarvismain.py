import pyttsx3
import speech_recognition as sr
import datetime
import os
import wikipedia
import webbrowser
import requests
from bs4 import BeautifulSoup
import time
import threading
import psutil
import pywhatkit as kit
from pyautogui import moveTo,write,leftClick
import pyautogui
import pyjokes

import sys
from PyQt5.QtCore import QThread
from PyQt5.QtWidgets import QWidget, QMainWindow
from PyQt5.QtWidgets import QApplication
from PyQt5 import QtGui

from jarvisGUI import Ui_Widget

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    ui.updateMovieDynamically("speaking")
    engine.say(audio)
    engine.runAndWait()

def weather():
    speak("Checking the details for weather...")
    URL = "https://weather.com/weather/today/l/26.62,87.36?par=google&temp=c"
    header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}
    page = requests.get(URL, headers=header)
    soup = BeautifulSoup(page.content, 'html.parser')
    temperature = soup.find(class_="CurrentConditions--tempValue--MHmYY").get_text()
    description = soup.find(class_="CurrentConditions--location--1YWj_").get_text()
    temp = f"Sir, the temperature is {temperature} Celsius and it is {description} outside."
    speak(temp)
    if int(temperature[:-1]) < 20:
        speak("It will be better if you wear woolen clothes, sir.")
    elif int(temperature[:-1]) <= 14:
        speak("Sir, it is very cold outside. If you want to go outside, wear woolen clothes.")
    elif int(temperature[:-1]) >= 25:
        speak("Sir, you don't need to wear woolen clothes to go outside.")

def news():
    main_url = 'http://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=e8e69c4d59884053995882906c16cce9'

    main_page = requests.get(main_url).json()
    # print(main_page)
    articles = main_page["articles"]
    print(articles)
    head = []
    day=["first","second","third","fourth","fifth","sixth","seventh","eighth","ninth","tenth"]
    for ar in articles:
        head.append(ar["title"])
    for i in range (len(day)):
        print(f"today's {day[i]} news is: ", head[i])
        speak(f"today's {day[i]} news is: {head[i]}")

def battery():
    battery = psutil.sensors_battery()
    battery_percentage = str(battery.percent)
    plugged = battery.power_plugged
    speak(f"Sir, it is {battery_percentage} percent.")
    if plugged:
        speak("and It is charging....")
    if not plugged:
        if battery_percentage <= "95%":
            speak("Sir, plug charger.")

def send_whatsapp_message(number, message):
    kit.sendwhatmsg_instantly(f"+91{number}", message)

def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak(f"Sir, the current year is {year}, current month is {month} and the current date is {date}")


class jarvismainFile(QThread):
    def __init__(self):
        super(jarvismainFile, self).__init__()
        print("maingui")

    def run(self):
        self.jarvis()



    def commands(self):
        ui.updateMovieDynamically("listening")
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            r.pause_threshold = 1
            r.adjust_for_ambient_noise(source, duration=1)
            audio = r.listen(source)

        try:
            ui.updateMovieDynamically("loading")
            print("Wait for few Moments..")
            self.query = r.recognize_google(audio, language='en-in')
            print(f"You just said: {self.query}\n")

        except Exception as e:
            print(e)
            speak("Please tell me again")
            self.query = "none"
        return self.query

    def wishings(self):
        ui.updateMovieDynamically("speaking")
        hour = int(datetime.datetime.now().hour)
        if hour >= 0 and hour < 12:
            print("Jarvis: Good Morning BOSS")
            speak("Good Morning BOSS")
        elif hour >= 12 and hour < 17:
            print("Jarvis: Good Afternoon BOSS")
            speak("Good Afternoon BOSS")
        elif hour >= 17 and hour < 21:
            print("Jarvis: Good Evening BOSS")
            speak("Good Evening BOSS")
        else:
            print("Jarvis: Good Night BOSS")
            speak("Good Night BOSS")
    def wakeUpCommands(self):
        ui.updateMovieDynamically("sleeping")
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Jarvis is Sleeping...")
            r.pause_threshold = 1
            r.adjust_for_ambient_noise(source, duration=1)
            audio = r.listen(source)
        try:
            self.query = r.recognize_google(audio, language='en-in')
            print(f"User said: {self.query}\n")
        except Exception as e:
            self.query = "none"
        return self.query

    def jarvis(self):
        while True:
            self.query = self.wakeUpCommands().lower()
            if 'wake up' in self.query or 'jarvis' in self.query or 'makeup' in self.query or 'backup' in self.query:
                self.wishings()
                speak("Yes BOSS What can I do for you!")
                while True:
                    self.query = self.commands().lower()
                    if 'wikipedia' in self.query:
                        speak("Searching in Wikipedia")
                        try:
                            self.query = self.query.replace("wikipedia", "")
                            results = wikipedia.summary(self.query, sentences=1)
                            speak("According to Wikipedia,")
                            print(results)
                            speak(results)
                        except:
                            speak("No Results found Sir...")
                            print("No results Found")

                    elif 'open youtube' in self.query:
                        speak("opening Youtube")
                        webbrowser.open("youtube.com")

                    elif 'time' in self.query:
                        strTime = datetime.datetime.now().strftime("%H:%M:%S")
                        speak(f"Sir, the time is {strTime}")

                    elif 'mute' in self.query or 'sleep' in self.query or 'take rest' in self.query or 'rest' in self.query:
                        speak("I'm Muting Sir...")
                        break
                    #elif 'exit program' in self.query or 'exit the program' in self.query or 'leave' in self.query :
                        #speak("I'm Leaving Sir, Byeee...")
                        #quit()
                    elif "open notepad" in self.query:
                        speak("Opening Notepad Application sir...")
                        os.startfile('C:\\Windows\\System32\\notepad.exe')
                        while True:
                            self.notepad.query = self.commands().lower()
                            if "paste" in self.notepad.query:
                                pyautogui.hotkey('ctrl', 'v')
                                speak("Done Sir!")
                            elif "save this file" in self.notepad.query:
                                pyautogui.hotkey('ctrl', 's')
                                speak("Sir, Please Specify a name for this file")
                                self.notepadSaving.query = self.commands()
                                pyautogui.write(self.notepadSaving.query)
                                pyautogui.press('enter')
                            elif 'type' in self.notepad.query:
                                speak("Please Tell me what should I Write...")
                                while True:
                                    writeInNotepad = self.commands()
                                    if writeInNotepad == 'exit typing':
                                        speak("Done Sir.")
                                        break
                                    else:
                                        pyautogui.write(writeInNotepad)

                            elif "exit notepad" in self.notepad.query or 'close notepad' in self.notepad.query:
                                speak('quiting Notepad Sir...')
                                pyautogui.hotkey('ctrl', 'w')
                                break

                    elif 'open google' in self.query:
                        speak("Opening Google Chrome Sir")
                        os.startfile("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")
                        while True:
                            self.chrome.query = self.commands().lower()
                            if "search" in self.chrome.query:
                                self.youtube.query = self.chrome.query
                                self.youtube.query = self.youtube.query.replace("search", "")
                                pyautogui.write(self.youtube.query)
                                pyautogui.press('enter')
                                speak('Searching...')

                            elif 'close chrome' in self.chrome.query or "exit chrome" in self.chrome.query or "exit google" in self.chrome.query or "close window" in self.chrome.query or "close this window" in self.chrome.query:
                                pyautogui.hotkey('ctrl', 'w')
                                speak("Closing Google Chrome Sir...")
                                break


                    elif "what can you do for me" in self.query:
                        speak('Yes sir, Nice Question')
                        speak('As per my Program, Im a bot which can perform tasks through your voice commands')

                    elif "cool" in self.query or "nice" in self.query or "awsome" in self.query or "thank you" in self.query:
                        speak("Yes sir, That's my Pleasure!")

                    elif 'minimize' in self.query or 'minimise' in self.query:
                        speak('Minimizing Sir')
                        pyautogui.hotkey('win', 'down', 'down')

                    elif 'maximize' in self.query or 'maximise' in self.query:
                        speak('Maximizing Sir')
                        pyautogui.hotkey('win', 'up', 'up')

                    elif 'close the window' in self.query or 'close the application' in self.query:
                        speak('Closing Sir')
                        pyautogui.hotkey('ctrl', 'w')

                    elif 'screenshot' in self.query:
                        speak("Taking Screenshot sir...")
                        pyautogui.hotkey('win', 'prtsc')

                    elif 'play song' in self.query or 'sing a song' in self.query or 'play a song' in self.query or 'play music' in self.query or 'play a music' in self.query:
                        speak("Yes Sir Please Wait a moment")
                        songs = os.listdir('D:\music')  # Use the path of your file here
                        os.startfile(os.path.join('D:\music', songs[0]))  # Use the path of your file here
                    elif 'pause' in self.query or 'pass' in self.query:
                        pyautogui.press('space')
                        speak('Done Sir')
                    elif 'joke' in self.query:
                        jarvisJoke = pyjokes.get_joke()
                        print(jarvisJoke)
                        speak(jarvisJoke)

                    elif 'what is the weather' in self.query or 'tell me the temperature' in self.query or "what's the temperature" in self.query:
                        weather()
                    elif 'tell me news' in self.query or 'what is the news' in self.query or 'tell me' in self.query or 'news' in self.query or 'nose' in self.query:
                        speak("please wait sir, feteching the latest news")
                        news()
                    elif 'battery condition' in self.query or 'percentage in battery' in self.query or 'percent in my pc' in self.query:
                        battery()
                    elif "send a whatsapp message" in self.query:
                        speak('On what number should I send the message sir? Please tell: ')
                        number = self.commands().lower()
                        speak("What is the message sir?")
                        message = self.commands().lower()
                        send_whatsapp_message(number, message)
                        speak("I've sent the message sir.")

                    elif 'tell me the date' in self.query or 'tell me date' in self.query:
                        date()

                    elif "open spotify" in self.query:
                        speak("Opening Spotify sir...")
                        os.startfile('C:\\Users\\arunj\\AppData\\Local\\Microsoft\\WindowsApps\\Spotify.exe')


                    elif "song on youtube" in self.query:
                        kit.playonyt("jill jill")

                    elif 'voice' in self.query:
                        if 'female' in self.query:
                            engine.setProperty('voice', voices[1].id)
                        else:
                            engine.setProperty('voice', voices[0].id)
                        speak("Hello Sir, I have switched my voice. How is it?")

                    elif 'stands for' in self.query:
                        speak('J.A.R.V.I.S stands for JUST A RATHER VERY INTELLIGENT SYSTEM')

                    elif 'remember me' in self.query:
                        speak("what should i remember sir")
                        rememberMessage = self.commands()
                        speak("you said me to remember" + rememberMessage)
                        remember = open('data.txt', 'w')
                        remember.write(rememberMessage)
                        remember.close()

                    elif 'do you remember anything' in self.query:
                        remember = open('data.txt', 'r')
                        speak("you said me to remember that" + remember.read())

                    elif "open command prompt" in self.query:
                        os.system("start cmd")


class Ui_JARVIS(QMainWindow):
    def __init__(self):
        super(Ui_JARVIS, self).__init__()
        self.jarvisUI = Ui_Widget()
        self.jarvisUI.setupUi(self)

        self.jarvisUI.exit.clicked.connect(self.close)
        #self.jarvisUI.enter.clicked.connect(self.maualCodeFromTerminal)
        self.runAllMovies()

    #def maualCodeFromTerminal(self):
        #if self.jarvisUI.command.text():
        #cmd = self.jarvisUI.command.text()
        #self.jarvisUI.command.clear()
        #self.jarvisUI.Terminal.appendPlainText(f"User type -> {cmd}")
        '''
            if cmd == 'exit':
                self.close()
            elif cmd == 'help':
                self.terminalPrint("Ican do every thimg")
            else:
                pass '''

    #def terminalPrint(self, text):
        #self.jarvisUI.Terminal.appendPlainText(text)
        #self.jarvisUI.Terminal.clear()
    
    def updateMovieDynamically(self, state):
        if state == "sleeping":
            self.jarvisUI.sleep.raise_()
            self.jarvisUI.sleep.show()
            self.jarvisUI.speak.hide()
            self.jarvisUI.listen.hide()
            self.jarvisUI.load.hide()

        elif state == "speaking":
            self.jarvisUI.speak.raise_()
            self.jarvisUI.speak.show()
            self.jarvisUI.sleep.hide()
            self.jarvisUI.listen.hide()
            self.jarvisUI.load.hide()

        elif state == "listening":
            self.jarvisUI.listen.raise_()
            self.jarvisUI.listen.show()
            self.jarvisUI.sleep.hide()
            self.jarvisUI.speak.hide()
            self.jarvisUI.load.hide()

        elif state == "loading":
            self.jarvisUI.load.raise_()
            self.jarvisUI.load.show()
            self.jarvisUI.sleep.hide()
            self.jarvisUI.listen.hide()
            self.jarvisUI.speak.hide()



    def runAllMovies(self):
        self.jarvisUI.codingMovie = QtGui.QMovie("C:\\Users\\arunj\\PycharmProjects\\Jarvis1\\GUI files\\B.G_Template_1.gif")
        self.jarvisUI.pg.setMovie(self.jarvisUI.codingMovie)
        self.jarvisUI.codingMovie.start()

        self.jarvisUI.backMovie = QtGui.QMovie("C:\\Users\\arunj\\PycharmProjects\\Jarvis1\\GUI files\\background-cropped.gif")
        self.jarvisUI.bg1.setMovie(self.jarvisUI.backMovie)
        self.jarvisUI.backMovie.start()

        self.jarvisUI.sleepMovie = QtGui.QMovie("C:\\Users\\arunj\\PycharmProjects\\Jarvis1\\GUI files\\sleepmode.gif")
        self.jarvisUI.sleep.setMovie(self.jarvisUI.sleepMovie)
        self.jarvisUI.sleepMovie.start()

        self.jarvisUI.listenMovie = QtGui.QMovie("C:\\Users\\arunj\\PycharmProjects\\Jarvis1\\GUI files\\listening.gif")
        self.jarvisUI.listen.setMovie(self.jarvisUI.listenMovie)
        self.jarvisUI.listenMovie.start()

        self.jarvisUI.speakMovie = QtGui.QMovie("C:\\Users\\arunj\\PycharmProjects\\Jarvis1\\GUI files\\speaking.gif")
        self.jarvisUI.speak.setMovie(self.jarvisUI.speakMovie)
        self.jarvisUI.speakMovie.start()

        self.jarvisUI.loadMovie = QtGui.QMovie("C:\\Users\\arunj\\PycharmProjects\\Jarvis1\\GUI files\\tech loading.gif")
        self.jarvisUI.load.setMovie(self.jarvisUI.loadMovie)
        self.jarvisUI.loadMovie.start()

        self.jarvisUI.arcMovie = QtGui.QMovie("C:\\Users\\arunj\\PycharmProjects\\Jarvis1\\GUI files\\techcircle.gif")
        self.jarvisUI.anim.setMovie(self.jarvisUI.arcMovie)
        self.jarvisUI.arcMovie.start()






if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = Ui_JARVIS()
    ui.show()

    startExecution = jarvismainFile()
    startExecution.start()
    sys.exit(app.exec_())