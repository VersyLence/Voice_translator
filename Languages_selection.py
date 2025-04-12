def get_selected_languages(self):
        
        language_map = {
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

        input_lang = self.inlang.get()
        output_lang = self.outlang.get()
        
        if input_lang == "Выбери Язык1" or output_lang == "Выбери Язык2":
            self.windowtext.delete("1.0", "end")
            self.windowtext.insert("1.0", "Пожалуйста, выберите языки")
            return None, None
        
        src_lang = language_map.get(input_lang, "auto") 
        dest_lang = language_map.get(output_lang, "en")  
        
        return src_lang, dest_lang