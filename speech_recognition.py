import speech_recognition
import pyttsx3

recognizer=speech_recognition.Recognizer()

while True:

    try:
        with speech_recognition.Microphone() as mic:
            recognizer.adjust_for_ambient_noise(mic,duration=0.3)
            audio = recognizer.listen(mic)

            txt = recognizer.recognize_google(audio)
            txt=txt.lower()

            print(f"Recognized: {txt}")
    except speech_recognition.UnknownValueError():

        recognizer = speech_recognition.Recognizer()
        continue
