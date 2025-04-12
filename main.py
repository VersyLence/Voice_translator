from tkinter import *
from tkinter import ttk
from Audio_translate import Translate
from Voice_record import Record
import asyncio


class ProjectApp:
    def __init__(self, rot):
        self.flag = False
        self.root = rot
        self.root.title("TranslaterShowSubtitles")
        self.root.geometry("500x500")
        self.record_btn = ttk.Button(self.root, text="Записать голос", command=self.clickrecording)
        self.record_btn.pack(pady=10)

        languages = ["Английский", "Китайский", "Испанский", "Хинди", "Арабский",
                     "Бенгальский", "Португальский", "Русский", "Японский",
                     "Немецкий", "Французский", "Итальянский", "Турецкий",
                     "Корейский", "Польский", "Украинский"]

        self.inlang = ttk.Combobox(self.root, values=languages)
        self.inlang.set("Выбери Язык1")
        self.inlang.pack(pady=5)

        self.outlang = ttk.Combobox(self.root, values=languages)
        self.outlang.set("Выбери Язык2")
        self.outlang.pack(pady=5)

        self.windowtext = Text(self.root, wrap=WORD, width=50, height=10)
        self.windowtext.pack(pady=0)

    def clickrecording(self):
        self.flag = not self.flag
        if self.flag:
            self.record_btn["text"] = "Стоп запись"
            asyncio.run(self.main())
        else:
            self.record_btn["text"] = "Начать запись"

    async def main(self):
        text = await Record.voice_recorder(self)
        translated_text = await Translate.translate_text(text)
        self.windowtext.delete("1.0", END)
        self.windowtext.insert("1.0",translated_text)


if __name__ == "__main__":
    root = Tk()
    app = ProjectApp(root)
    root.mainloop()
