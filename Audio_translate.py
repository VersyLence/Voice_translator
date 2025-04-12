from googletrans import Translator

class Translate():
    async def translate_text(text):
        translator = Translator()
        result = await translator.translate(text, dest='en')
        return result.text