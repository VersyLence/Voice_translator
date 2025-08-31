class LanguageSelector:
    def __init__(self):
        self.language_map = {
            "Английский": "en",
            "Китайский": "zh-cn",
            "Испанский": "es",
            "Хинди": "hi",
            "Арабский": "ar",
            "Бенгальский": "bn",
            "Португальский": "pt",
            "Русский": "ru",
            "Японский": "ja",
            "Немецкий": "de",
            "Французский": "fr",
            "Итальянский": "it",
            "Турецкий": "tr",
            "Корейский": "ko",
            "Польский": "pl",
            "Украинский": "uk"
        }
    #app_instance - экземпляр класса ProjectApp, нужен чтобы можно было работать с inlang, outlang, windowtext (его сами передаем)
    def get_selected_languages(self, app_instance):
        input_lang = app_instance.inlang.get()
        output_lang = app_instance.outlang.get()
        
        if input_lang == "Выбери Язык1" or output_lang == "Выбери Язык2":
            app_instance.windowtext.delete("1.0", "end")
            app_instance.windowtext.insert("1.0", "Пожалуйста, выберите языки")
            return None, None
        
        src_lang = self.language_map.get(input_lang, "auto")
        dest_lang = self.language_map.get(output_lang, "en")
        
        # src_lang = код исходного языка, dest_lang = код языка на который надо переводить 
        return src_lang, dest_lang