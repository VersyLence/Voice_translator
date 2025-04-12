from gtts import gTTS
import pygame
import time
import os

class Speak():
	

	def __init__(self, language = 'en'):
		pygame.mixer.init()
		self.language = language


	def play_speech(self):
		pygame.mixer.music.stop()
		pygame.mixer.music.unload()
		pygame.mixer.music.load("speech.mp3")  
		pygame.mixer.music.play()
		running_time = os.path.getsize('speech.mp3')
		time.sleep(running_time/8096)


	def ongoing(self, text_to_speech, language = None):
		if language is None:
			language = self.language
		if os.path.exists("speech.mp3"):
			pygame.mixer.music.stop()
			pygame.mixer.music.unload()
			time.sleep(0.2)
		tts = gTTS(text_to_speech, lang = language)
		tts.save('speech.mp3')
		self.play_speech()

