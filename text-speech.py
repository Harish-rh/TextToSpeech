from gtts import gTTS  # Import this module for text to speech
import os

abc = open("sample.txt")
# To open a file

text = abc.read()
# Text that you want to convert

language = 'en'
# en is for english language

obj = gTTS(text=text, lang=language, slow=False)
# slow=False because the converted video will have high speed

obj.save("sample.mp3")
os.system("sample.mp3")
