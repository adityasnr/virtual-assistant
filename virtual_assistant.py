import pyttsx3

#initialise Text-to-speech engine
engine = pyttsx3.init()

#convert this text to speech
text = "hello, I am Jarvis and what is you name"
voices = engine.getProperty("voices")
engine.setProperty("voice" , voices[1].id)
engine.say(text)

#play the speech
engine.runAndWait()

text2 = input("what is your name: ")

text3 = "hello", text2 , " how can I help you? "
engine.say(text3)
engine.runAndWait()



