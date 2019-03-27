from gtts import gTTS
import wikipedia as wiki

# wiki
query = input("What would you like to hear about?\n")
result = wiki.page(title=query)
print("Got " + result.title + ", now encoding into mp3")
# tts
tts = gTTS(text=result.content,lang='en')
tts.save(result.title + '.mp3')
