import pyttsx3 as ps 

def multi_linw():

    content = ["hello im asri","how aare you","do u wanna help"]
    engine = ps.init()
    engine.setProperty('voice','en+f3')

    for m in content:
        engine.say(m)
        engine.runAndWait()

multi_linw()
