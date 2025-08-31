from googletrans import Translator

class Translate():
    async def translate_text(text,seclang):
        translator = Translator()
        result = await translator.translate(text, dest=seclang)
        return result.text 