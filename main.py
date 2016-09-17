# obtain path to "english.wav" in the same folder as this script
from os import path
import speech_recognition as sr

AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), "test_fr.wav")

# IBM Speech to Text creds
IBM_USERNAME = ""
IBM_PASSWORD = ""

if __name__ == '__main__':

    speechRecognize = sr.Recognizer()

    with sr.AudioFile(AUDIO_FILE) as source:
        audio = speechRecognize.record(source) # read the entire audio file

        try:
            # for testing purposes, we're just using the default API key
            # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
            # instead of `r.recognize_google(audio)`
            print("Google Speech Recognition thinks you said " + speechRecognize.recognize_google(audio, language='fr-FR'))
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))

