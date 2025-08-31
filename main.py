import customtkinter as ctk
from Voice_The_Text import Speak
from Audio_translate import Translate
from Voice_record import Record
from Languages_selection import LanguageSelector
import asyncio


class ProjectApp:
    def __init__(self, root):
        self.flag = False
        self.root = root

        # Настройка темы
        ctk.set_appearance_mode("light")
        ctk.set_default_color_theme("coffee.json")
        self.root.configure(fg_color="#d8c0a0")

        self.root.title("TranslaterShowSubtitles")
        self.root.geometry("500x500")
        self.root.resizable(False, False)

        languages = ["Английский", "Китайский", "Испанский", "Хинди", "Арабский",
                     "Бенгальский", "Португальский", "Русский", "Японский",
                     "Немецкий", "Французский", "Итальянский", "Турецкий",
                     "Корейский", "Польский", "Украинский"]

        # исходный язык
        self.outlang = ctk.CTkComboBox(
            self.root,
            values=languages,
            state="readonly"
        )
        self.outlang.set("Исходный язык")
        self.outlang.pack(pady=10)

        # Кнопка записи голоса
        self.record_btn = ctk.CTkButton(
            self.root,
            text="Записать голос",
            command=self.clickrecording
        )
        self.record_btn.pack(pady=10)

        # поле ввода
        self.windowtext = ctk.CTkTextbox(
            self.root,
            width=400,
            height=200,
            font=("Helvetica", 14),
            wrap="word"
        )
        self.windowtext.pack(pady=10)

        # язык перевода
        self.inlang = ctk.CTkComboBox(
            self.root,
            values=languages,
            state="readonly"
        )
        self.inlang.set("Язык перевода")
        self.inlang.pack(pady=10)

        # Кнопка озвучки
        self.voice_btn = ctk.CTkButton(
            self.root,
            text="Озвучить текст",
            command=self.voicetext
        )
        self.voice_btn.pack(pady=10)

        self.languagesel = LanguageSelector()

    def change_theme(self, choice):
        """Изменение цветовой темы"""
        ctk.set_default_color_theme(choice)
        self.current_theme = choice

    def clickrecording(self):
        self.flag = not self.flag
        if self.flag:
            self.record_btn.configure(text="Стоп запись")
            asyncio.run(self.main())
        else:
            self.record_btn.configure(text="Записать голос")

    async def main(self):
        firstlang, seclang = self.languagesel.get_selected_languages(self)
        text = await Record.voice_recorder(self, firstlang)
        translated_text = await Translate.translate_text(text, seclang)

        speaker = Speak(language=seclang)
        self.windowtext.delete("1.0", "end")
        self.windowtext.insert("1.0", translated_text)

    def voicetext(self):
        current_text = self.windowtext.get("1.0", "end").strip()
        if current_text:
            firstlang, seclang = self.languagesel.get_selected_languages(self)
            speaker = Speak(language=seclang)
            speaker.ongoing(current_text)


if __name__ == "__main__":
    root = ctk.CTk()
    app = ProjectApp(root)
    root.mainloop()