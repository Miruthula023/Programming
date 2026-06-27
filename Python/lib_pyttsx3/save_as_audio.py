import pyttsx3 as ps
import pdb

pdb.set_trace()
def save_in_file(text,filename=""):
    engine = ps.init()
    engine.save_to_file(text,filename)
    engine.runAndWait()

save_in_file("Hello","audio.mp3")
