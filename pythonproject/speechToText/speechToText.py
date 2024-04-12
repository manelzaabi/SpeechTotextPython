import pyttsx3

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Set properties (optional)
engine.setProperty('rate', 130)    
engine.setProperty('volume', 1.0)  

# Input the text you want to convert to speech
text = "Hello how are you?"

# Convert text to speech and play it
engine.say(text)
engine.runAndWait()
