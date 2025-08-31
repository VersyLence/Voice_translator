from gtts import gTTS
import pygame
import time
import os

class Speak():
	

	def __init__(self, language = 'en'):
		pygame.mixer.init()
		self.language = language


	def play_speech(self):
		'''play_speech() воспроизводит звук с файла speech.mp3 расчитывая время +- котоорое нужно на воспроизведение звука и устанавливает на это время time.sleep()
		вам эта функция врое как не нужна'''
		pygame.mixer.music.stop()
		pygame.mixer.music.unload()
		pygame.mixer.music.load("speech.mp3")  
		pygame.mixer.music.play()
		running_time = os.path.getsize('speech.mp3')
		time.sleep(running_time/8096)


	def ongoing(self, text_to_speech, language = None):
		'''ongoing(текст на впороизведение, язык(по умолчанию английский)) создает файл "speech.mp3" подготавливает его для звучания, отправляет запрос на преобразование текста в речь и записывает в файл, после чего воспроизводит его
		P.S. видимо функция калл потому что нихуя не возвращает'''
		if language is None:
			language = self.language
		if os.path.exists("speech.mp3"):
			pygame.mixer.music.stop()
			pygame.mixer.music.unload()
			time.sleep(0.2)
		tts = gTTS(text_to_speech, lang = language)
		tts.save('speech.mp3')
		self.play_speech()

