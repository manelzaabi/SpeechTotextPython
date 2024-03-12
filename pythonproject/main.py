import speech_recognition as sr

recognizer = sr.Recognizer()

with sr.Microphone() as source:
    try:
        print("Please say something...")
        audio = recognizer.listen(source, timeout=5) 
        print("Recognizing...")

        text = recognizer.recognize_google(audio)
        print("You said:", text)

    except sr.WaitTimeoutError:
        print("Timeout waiting for audio input")
    except sr.UnknownValueError:
        print("Sorry, could not understand audio.")
    except sr.RequestError as e:
        print("Error fetching results; {0}".format(e))
    except Exception as e:
        print("An error occurred:", e)

