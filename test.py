# -*- coding: utf-8 -*-
"""
Created on Tue May 21 16:13:35 2019

@author: rajak
"""
import pyttsx3
import datetime
import speech_recognition as sr
engine=pyttsx3.init("sapi5")
engine.setProperty("rate",150)
current_time=datetime.datetime.now().strftime("%H:%M:%S")
def Wish():
    hour=datetime.datetime.now().hour
    if(hour>=6 and hour<12):
       engine.say("Good morning Sir")
       engine.say(f"sir the time is {current_time}")
    elif(hour>=12 and hour<15):
        engine.say("good afternoon sir")
        engine.say(f"sir the time is {current_time}")
    else:
        engine.say("Good evening sir")
        engine.say(f"sir the time is {current_time}")
def takeMessage():
    engine.say("Please give your message")
    message=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        message.pause_threshold=1
        message=message.listen(source)
    try:
        print("Recognising....")
        query=r.recognize_google(audio, language='en-in')
        print("User said ", query)
    except Exception as e:
         print("plase say that again....")
         return 'None'
    return query 
def takeKey():
    engine.say("please give your key")
    key=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        key.pause_threshold=1
        key=key.listen(source)
def Encryption():
    Wish()
    takeMessage()
    takeKey()