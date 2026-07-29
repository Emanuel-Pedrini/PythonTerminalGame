# import pyttsx3
# vPyttsx3_PyttsxEngine = pyttsx3.init()

# vPyttsx3_PyttsxEngine.say("EMILLIA likes eating hot chocolate and milk!.")
# vPyttsx3_PyttsxEngine.runAndWait()

from gtts import gTTS
import playsound

tts = gTTS(text="Emillia likes playing alien basketball with her alien friends!.", lang="en", tld="co.uk")
tts.save("Outputs\\output.wav")
playsound.playsound("Outputs\\output.wav")