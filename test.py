#from playsound import playsound
#playsound('01_Nathan_Statement.mp3')

from pydub import AudioSegment
from pydub.playback import play

#song = AudioSegment.from_mp3("01_Nathan_Statement.mp3")
#play(song)

while True:
    sound = input("Type something: ")
    try:
        play(AudioSegment.from_mp3((sound + ".mp3")))
    except:
        print("Uh no")
