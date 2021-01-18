import speech_recognition as sr

from utils import convert_to_wav


AUDIO_FILE = './data/raw/mp3/aps-smp.mp3'
if AUDIO_FILE.rsplit('.')[1] != 'mp3':
    AUDIO_FILE = convert_to_wav(AUDIO_FILE)
    print('successfully audio converted!')

r = sr.Recognizer()
with sr.AudioFile(AUDIO_FILE) as source:
    audio = r.record(source)

result = r.recognize_google(audio, language='ja-JP')

try:
    print('Google Speech Recognition thinks you said:')
    print(result)
except sr.UnknownValueError:
    print('Google Speech Recognition could not understand audio')
except sr.RequestError as e:
    print('Could not request results from Google Speech Recognition service; {0}'.format(e))
