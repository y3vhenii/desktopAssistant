import sounddevice as sd
import soundfile as sf
from scipy.io.wavfile import write
import speech_recognition as sr

# Recognize voice command and return text
def recognizeVoice():
    fs = 44100  # Sample rate
    seconds = 4  # Duration of recording
    sd.default.dtype='int32', 'int32'   # Need to set to int32 to avoid trouble with recognize_google

    myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=1)
    sd.wait()  # Wait until recording is finished
    write('command.wav', fs, myrecording)  # Save as WAV file 
    filename = 'command.wav'

    # Extract data from file
    data, fs = sf.read(filename, dtype='int32')  

    # Recognize the sound
    r = sr.Recognizer()
    tempVoice = sr.AudioFile('command.wav')
    with tempVoice as source:
        audio = r.record(source)
    text = r.recognize_google(audio)
    print(text)
    return str(text)