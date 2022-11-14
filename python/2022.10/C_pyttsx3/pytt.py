import pyttsx3

voice_engine = pyttsx3.init()
voices = voice_engine.getProperty('voices')
voice = voice_engine.getProperty('voices') #get the available voices
# eng.setProperty('voice', voice[0].id) #set the voice to index 0 for male voice
voice_engine.setProperty('voice', voice[1].id) #changing voice to index 1 for female voice
voice_engine.say("Im saying hello to this beautiful world!")


voice_engine.runAndWait()