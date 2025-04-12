import speech_recognition as sr

class Record():
    async def voice_recorder(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            try:
                audio = r.listen(source)
                r.adjust_for_ambient_noise(source)
                text = r.recognize_google(audio, language='ru-RU')
                text = text.lower()
                return text
            except sr.UnknownValueError:
                return "Could not understand audio"