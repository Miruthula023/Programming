import pyttsx3

engine = pyttsx3.init()
engine.setProperty('voice','en+f3')
engine.say("Hello,get started ur program")
engine.runAndWait()

