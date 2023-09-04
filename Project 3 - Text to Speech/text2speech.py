from gtts import gTTS
text = "hi. this is me"

tts = gTTS(text=text, lang='en')
tts.save(r"convert text to speech.mp3")