import pyaudio
import wave
import speech_recognition as sr
import subprocess
from queryprocessor import QueryProcessor

Run = True
CHUNK = 1024

def say(text):
    subprocess.call('say ' + text, shell=True)

# To play wave file
def play_audio(filename):
    global Chunk 
	# Media files need to be opened in binary mode
    wf = wave.open(filename, 'rb')  
    pa = pyaudio.PyAudio()  

    # creating a stream
    stream = pa.open(
        format = pa.get_format_from_width(wf.getsampwidth()),
        channels = wf.getnchannels(),
        rate = wf.getframerate(),
        output = True
    )
    
    data = wf.readframes(chunk)

    while data:
        stream.write(data)
        data = wf.readframes(chunk)

    stream.close()
    pa.terminate()


r = sr.Recognizer()
cmd = QueryProcessor()


def initSpeech():
	global Run
    print("Listening..")
    play_audio('audio/beep.wav')

    with sr.Microphone() as source:
        print("Say...")
        audio = r.listen(source, timeout = 5) # had issue with this so gave timeout otherwise it never stops listening  

    play_audio("audio/beep.wav") 
    command = ""

    try:
        command = r.recognize_google(audio)
        print(command)
    except:
        command = "Sorry...Couldn't get you!"
	# if user says quit - exit
    if "quit" in command:
        Run = False
        cmd.respond("Bye Bye")
    else:
        cmd.discover(command)

while Running is True:
    initSpeech()
