from gtts import gTTS
from playsound import playsound

filePath = r"myText.txt"

with open(filePath, 'rt', encoding='UTF8') as f:
    readFile = f.read()
    
text = "hi. this is me"

# tts = gTTS(text=text, lang='en')
tts = gTTS(text=readFile, lang='en')

tts.save(r"/Users/jeonghyunahn/Jeong's Folder/금호타이어/convert text to speech.mp3")

playsound(r"/Users/jeonghyunahn/Jeong's Folder/금호타이어/convert text to speech.mp3")
