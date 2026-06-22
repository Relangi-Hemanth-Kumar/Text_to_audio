from gtts import gTTS
from googletrans import Translator
text="please enter what do you want to convert"
s=gTTS(text)
s.save("audio.mp3")
"""this will save text in audio format"""
"""to convert tinglish to english"""
trans=Translator()
tinglish="ekkada unnavu annaya"
c=trans.translate(tinglish,dest="en")
print(c.text)
ting=gTTS(c.text)
ting.save("tinglish.mp3")
