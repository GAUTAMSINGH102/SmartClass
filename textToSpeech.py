import pyttsx3

def textToSpeech(text):
    player = pyttsx3.init()
    player.setProperty('rate', 150)
    voices = player.getProperty('voices')
    player.setProperty('voice', voices[1].id)
    player.say(text)
    player.runAndWait()

# text = "hello Everyone"
# textToSpeech(text)